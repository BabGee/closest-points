from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Point

import json
from django.http import JsonResponse

import math

@csrf_exempt
def points_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            points_data = data.get('points', '')
            points_list = points_data.split(';')
            points = []
            for point_str in points_list:
                x, y = map(int, point_str.split(','))
                points.append(Point(x=x, y=y))
            Point.objects.bulk_create(points)

            closest_points = find_closest_points(points)
            response = {'closest_points': [str(point) for point in closest_points]}
            return JsonResponse(response)
        except (json.JSONDecodeError, ValueError) as e:
            return JsonResponse({'error': 'Invalid points data format'})

    return JsonResponse({'error': 'Invalid request method'})


def find_closest_points(points):
    closest_distance = math.inf
    closest_points = []

    # Iterate over all pairs of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            
            # If the distance is smaller than the current closest distance, update the closest distance and points
            if distance < closest_distance:
                closest_distance = distance
                closest_points = [points[i], points[j]]
            # If the distance is equal to the current closest distance, append the points to the closest points list
            elif distance == closest_distance:
                closest_points.extend([points[i], points[j]])

    return closest_points


def calculate_distance(point1, point2):
    x1, y1 = point1.x, point1.y
    x2, y2 = point2.x, point2.y
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

