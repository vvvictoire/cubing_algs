from django.contrib import admin

from .models import Puzzle, AlgorithmSet, Algorithm, Case

# Register your models here.

admin.site.register(Puzzle)
admin.site.register(AlgorithmSet)
admin.site.register(Case)
admin.site.register(Algorithm)
