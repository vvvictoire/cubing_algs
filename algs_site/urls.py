"""URLs controller thing"""

from django.conf import settings # new
from django.urls import path #, include # new
from django.conf.urls.static import static # new

from . import views

app_name = 'algs_site'
urlpatterns = [
    # index, redirects to the puzzle list
    path('', views.puzzle, name='index'),
    # oauth
    path('oauth', views.oauth, name='oauth'),
    # main page, list puzzles
    path('', views.puzzle, name='puzzle'),
    # alg sets for a given puzzle
    path('alg/<str:puzzle_name>/', views.algorithm_set, name='algorithm_set'),
    # cases for a given alg set
    path('alg/<str:puzzle_name>/<str:algorithm_set_name>', views.case, name='case'),
    # lists algorithms for a given case
    path(
        'alg/<str:puzzle_name>/<str:algorithm_set_name>/<str:case_name>',
        views.algorithm_list,
        name='algorithm_list'),
    path('new_algorithm', views.new_algorithm, name='new_algorithm'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
