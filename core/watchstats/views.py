from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.


# @csrf_exempt
# def get_total_movie_watch_time(request, slug):
#     if slug in slugs:
#         return JsonResponse({'message': f'{slugs[slug]}'}, status=200)
#     else:
#         return JsonResponse({'error': 'slug not found'}, status=404)

# @csrf_exempt
# def get_user_total_watch_time(request, user_name):
#     if user_name in users:
#         return JsonResponse({'message': f'{users[user_name]}'}, status=200)
#     else:
#         return JsonResponse({'error': 'user not found'}, status=404)

# @csrf_exempt
# def user_movie_watch_time(request, user_name, slug):
#     if user_name in users:
#         if slug in slugs:
#             filtered_slug = []
#             for item in users[user_name]:
#                 if item.get('slug') == slug:
#                     filtered_slug.append(item.get('at'))
#             return JsonResponse({'message': f'{filtered_slug}'}, status=200)
#         else:
#             return JsonResponse({'error': 'slug not found'}, status=404)    
#     else:
#         return JsonResponse({'error': 'user not found'}, status=404)

# @csrf_exempt
# def movie_last_moment(request, user_name, slug):
#     if user_name in users:
#         if slug in slugs:
#             last_moment = 0
#             for item in users[user_name]:
#                 if item.get('slug') == slug:
#                     last_moment += int(item.get('at'))
#             return JsonResponse({'message': f'{last_moment}'}, status=200)
#         else:
#             return JsonResponse({'error': 'slug not found'}, status=404)
#     else:
#         return JsonResponse({'error': 'user not found'}, status=404)