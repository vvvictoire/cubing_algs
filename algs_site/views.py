"""Web application views"""

import json
import requests

from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Puzzle, AlgorithmSet, Algorithm

# Create your views here.

def index(request):
    """Home page"""
    return render(request, 'algs_site/index.html')

def puzzle(request):
    """List stored puzzles"""
    puzzle_list = Puzzle.objects.order_by('name')
    context = {'puzzle_list': puzzle_list}
    return render(request, 'algs_site/puzzle.html', context)

def algorithm_set(request, puzzle_name):
    """List algorithm sets for a given puzzle"""
    puzzle_object = get_object_or_404(Puzzle, name=puzzle_name)
    algorithm_set_list = AlgorithmSet.objects.filter(Q(puzzle=puzzle_object)).order_by('-name')
    context = {
        'puzzle_name': puzzle_name,
        'algorithm_set_list': algorithm_set_list}
    return render(request, 'algs_site/algorithm_set.html', context)

def algorithm_list(request, puzzle_name, algorithm_set_name):
    """List algorithms sets for a given get"""
    puzzle_object = get_object_or_404(Puzzle, name=puzzle_name)
    algorithm_set_list = get_object_or_404(AlgorithmSet, name=algorithm_set_name, puzzle=puzzle_object)
    algorithm_list_object = Algorithm.objects.filter(Q(algorithm_set=algorithm_set_list)).order_by('-name')
    context = {
        'puzzle_name': puzzle_name,
        'algorithm_set_name': algorithm_set_name,
        'algorithm_list_object': algorithm_list_object}
    return render(request, 'algs_site/algorithm_set_single.html', context)

def new_algorithm(request):
    """Upload a new algorithm"""
    return render(request, 'algs_site/new_algorithm.html')

def oauth(request):
    """Get information from the WCA provided token"""
    request_get_parameters = request.GET
    code = request_get_parameters['code']
    params_code = {'code': code,
                   'grant_type': 'authorization_code',
                   'client_secret': '8TRe0YAlodZrWMiMOiAvB8B6k6MJdeck36KxRUsg7m8',
                   'client_id': 'v9dN8Ur6pv4Q3esrDXq-wM6yWxa9sqE2PqDOG6LH91c',
                   'redirect_uri': 'http://localhost:8000/oauth'}
    token_request = requests.post('https://www.worldcubeassociation.org/oauth/token',
                                  data=params_code)
    token_response = token_request.text
    access_token = json.loads(token_response)
    #{  "access_token": "token",
    #   "token_type": "Bearer",
    #   "expires_in": 7200,
    #   "refresh_token": "refresh_token",
    #   "scope": "public",
    #   "created_at": 1597077406 }
    token = access_token['access_token']
    header = {'Authorization': 'Bearer ' + token}
    details = requests.get('https://www.worldcubeassociation.org/api/v0/me', headers=header)
    details_response = json.loads(details.text)
    #{ "me": {
    #   "class": "user",
    #   "url": "https://www.worldcubeassociation.org/persons/2000FOOB42",
    #   "id": 1337,
    #   "wca_id": "2000FOOB42",
    #   "name": "Qux Foobar",
    #   "gender": "f",
    #   "country_iso2": "FR",
    #   "delegate_status": null,
    #   "created_at": "2000-01-01T13:37:42.000Z",
    #   "updated_at": "2020-08-01T00:46:09.000Z",
    #   "teams": [ ],
    #   "avatar": {
    #       "url": "https://www.worldcubeassociation.org/uploads/user/avatar/2000FOOB42/avatar.jpg",
    #       "thumb_url": "https://www.worldcubeassociation.org/uploads/user/avatar/2000FOOB42/avatar_thumb.jpg",
    #       "is_default": false
    #   }
    # } }
    return HttpResponse('Logged in with ' + details_response['me']['wca_id'])
