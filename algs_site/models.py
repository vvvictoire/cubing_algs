"""Describes the application models"""

from django.db import models

# Create your models here.

class Puzzle(models.Model):
    """Describes a puzzle"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/puzzle/')
    alt_text = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class AlgorithmSet(models.Model):
    """Linked to a Puzzle, describes a set of algorithms for this puzzle"""
    name = models.CharField(max_length=100)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/algorithm_set')
    alt_text = models.CharField(max_length=100)
    def __str__(self):
        return self.puzzle.name + " " + self.name

class Algorithm(models.Model):
    """Linked to an algorithm set, describes a single algorithm"""
    sequence = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    algorithm_set = models.ForeignKey(AlgorithmSet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/algorithm')
    alt_text = models.CharField(max_length=100)
    def __str__(self):
        return self.algorithm_set.puzzle.name + " " + self.algorithm_set.name + " " + self.name
