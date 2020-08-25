"""Describes the application models"""

from django.db import models

# Create your models here.

class Puzzle(models.Model):
    """Describes a puzzle"""
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/puzzle/', null=True, blank=True)
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name

class AlgorithmSet(models.Model):
    """Linked to a Puzzle, describes a set of algorithms for this puzzle"""
    name = models.CharField(max_length=100)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/algorithm_set', null=True, blank=True)
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.puzzle.name + " " + self.name

    class Meta:
        unique_together = ['name', 'puzzle']

class Case(models.Model):
    """Linked to a Puzzle and AlgorithmSet, describes a puzzle state to be solved"""
    name = models.CharField(max_length=100)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    algorithm_sets = models.ManyToManyField(AlgorithmSet)
    image = models.ImageField(upload_to='images/case', null=True, blank=True)
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.puzzle.name + " " + self.name

    class Meta:
        unique_together = ['name', 'puzzle']

class Algorithm(models.Model):
    """Linked to a case, describes a single algorithm"""
    sequence = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/algorithm', null=True, blank=True)
    alt_text = models.CharField(max_length=100, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.case.puzzle.name + " " + self.case.name + " " + self.name

    class Meta:
        unique_together = ['name', 'case']
