"""URLs controller thing"""

from django.conf import settings # new
from django.urls import path #, include # new
from django.conf.urls.static import static # new

from . import views

app_name = 'algs_site'
urlpatterns = [
    # path('alg', views.index, name='index'),
    path('oauth', views.oauth, name='oauth'),
    path('', views.puzzle_list, name='puzzle_list'),
    path('alg/<str:puzzle_name>/', views.algorithm_sets, name='algorithm_sets'),
    path('alg/<str:puzzle_name>/<str:algorithm_set_name>',
         views.algorithm_set,
         name='algorithm_set'),
    path('alg/<str:puzzle_name>/<str:algorithm_set_name>/<str:algorithm_name>',
         views.algorithm_set,
         name='algorithm'),
    path('new_algorithm', views.new_algorithm, name='new_algorithm'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
