"""URLs controller thing"""

from django.conf import settings # new
from django.urls import path #, include # new
from django.conf.urls.static import static # new

from . import views

app_name = 'algs_site'
urlpatterns = [
    # index
    path('alg', views.index, name='index'),
    # oauth
    path('oauth', views.oauth, name='oauth'),
    # main page, list puzzles
    path('', views.puzzle, name='puzzle'),
    # alg sets for a given puzzle
    path('alg/<str:puzzle_name>/', views.algorithm_set, name='algorithm_set'),
    # algorithms for a given alg set
    path('alg/<str:puzzle_name>/<str:algorithm_set_name>',
         views.algorithm_list,
         name='algorithm_list'),
    path('alg/<str:puzzle_name>/<str:algorithm_set_name>/<str:algorithm_name>',
         views.algorithm_set,
         name='algorithm'),
    path('new_algorithm', views.new_algorithm, name='new_algorithm'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
