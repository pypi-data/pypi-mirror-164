"""
Trainer classes.
"""

# Imports ---------------------------------------------------------------------

import numpy as np
import torch

from torch import nn
from torch.utils.data import DataLoader

# Trainer class ---------------------------------------------------------------

class Trainer():

    def __init__(
        self, 
        model, 
        model_path,
        train_dataset,
        val_dataset,
        loss_func,
        optimizer,
        metrics=[],
        best_metric=None,
        device=None):

        # Set known instance properties
        self.model = model
        self.model_path = model_path
        self.train_dataset = train_dataset
        self.val_dataset = val_dataset
        self.loss_func = loss_func
        self.optimizer = optimizer
        self.metrics = metrics
        self.best_metric = best_metric

        # Create instnce properties for training
        self.train_dataloader = None
        self.val_dataloader = None
        self.monitor = None

        # Set up device
        if device == None:
            if torch.cuda.is_available():
                device = "cuda:0"
            elif torch.backends.mps.is_available():
                device = "mps"
            else:
                device = "cpu"

        self.device = torch.device(device)

    def train(
        self,
        batch_size,
        epochs,
        restore_best_weights=True):

        # Set up device
        print(f"Training on {self.device}\n")
        self.model.to(self.device)

        # Create dataloaders
        self.train_dataloader = DataLoader(
            self.train_dataset, 
            batch_size=batch_size, 
            shuffle=True)
        
        self.val_dataloader = DataLoader(
            self.val_dataset, 
            batch_size=batch_size, 
            shuffle=True)

        # Set up training monitor
        self.monitor = TrainingMonitor(
            self.model,
            self.model_path,
            self.metrics,
            self.best_metric)

        # Training loop
        for epoch in range(epochs):
            print(f"Epoch {epoch + 1}")
            self.train_epoch()
            self.eval_epoch()

        # Restore best weights
        if restore_best_weights == True:
            self.model.load_state_dict(torch.load(self.model_path))

    def train_epoch(self):

        n_batches = len(self.train_dataloader)
        running_loss = 0

        # Loop over batches and backprop gradients       
        for batch, (x, y) in enumerate(self.train_dataloader, start=1):

            # Move data to device
            x = x.to(self.device)
            y = y.to(self.device)

            # Prediction and loss
            pred = self.model(x)
            loss = self.loss_func(pred, y)

            # Backpropagation
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            # Calculate metrics       
            loss = loss.item()
            running_loss += loss
            average_loss = running_loss / batch
            
            # Report status
            report = self.monitor.train_update(batch, n_batches, average_loss)
            print(report, end="\r")

    def eval_epoch(self):

        n_batches = len(self.val_dataloader)
        running_loss = 0 
        targets = []
        predictions = []
        
        # Predict and calculate loss (with training processes disabled)
        self.model.eval()
        with torch.no_grad():
            for x, y in self.val_dataloader:
                x = x.to(self.device)
                y = y.to(self.device)
                pred = self.model(x)
                running_loss += self.loss_func(pred, y).item()
                targets.append(y.cpu().numpy())
                predictions.append(pred.cpu().numpy())
        self.model.train()

        loss = running_loss / n_batches
        targets = np.concatenate(targets)
        predictions = np.concatenate(predictions)

        report = self.monitor.eval_update(loss, targets, predictions)        
        print(report)

    def predict(self, dataset):
        dataloader = DataLoader(dataset)
        targets = []
        predictions = []
        self.model.eval()
        with torch.no_grad():
            for x, y in dataloader:
                x = x.to(self.device)
                y = y.to(self.device)
                pred = self.model(x)
                targets.append(y.cpu().numpy())
                predictions.append(pred.cpu().numpy())
        self.model.train()
        targets = np.concatenate(targets)
        predictions = np.concatenate(predictions)
        return targets, predictions

# Training monitor class ------------------------------------------------------

class TrainingMonitor():

    def __init__(
        self, 
        model, 
        model_path, 
        metrics=[], 
        best_metric=None):
        
        self.model = model
        self.model_path = model_path
        self.metrics = metrics
        self.best_metric = self.get_best_metric(metrics, best_metric)
        self.best_metric_loss = np.inf

    def get_best_metric(self, metrics, best_metric):
        metrics = {metric.name: metric for metric in metrics}
        if best_metric in metrics.keys():
            return metrics[best_metric]
        else:
            return None

    def get_metric_loss(self, loss, targets, predictions):
        if self.best_metric != None:
            return self.best_metric.get_metric_loss(targets, predictions)
        else:
            return loss

    def train_update(self, batch, n_batches, average_loss):
        return self.train_report(batch, n_batches, average_loss)

    def train_report(self, batch, n_batches, average_loss):
        counter_size = len(str(n_batches))
        report = \
            f"Training loss: {average_loss:.4f}  " \
            f"[{batch:{counter_size}} | {n_batches:{counter_size}}]" \
            f"         "
        return report

    def eval_update(self, loss, targets, predictions):
        metric_loss = self.get_metric_loss(loss, targets, predictions)
        updated = False
        if metric_loss < self.best_metric_loss:
            self.best_metric_loss = metric_loss
            torch.save(self.model.state_dict(), self.model_path)
            updated = True
        report = self.eval_report(loss, targets, predictions, updated)
        return report

    def eval_report(self, loss, targets, predictions, updated):
        metrics_report = ""
        for metric in self.metrics:
            metrics_report += metric.get_reported_metric(targets, predictions)
        updated_flag = "✓" if updated == True else ""
        report = \
            f"\nEvaluation loss: {loss:.4f}" \
            f", {metrics_report}" \
            f" {updated_flag}" \
            f"         \n"
        return report