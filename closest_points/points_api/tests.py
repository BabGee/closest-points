from django.test import TestCase

from .models import Point
from .views import find_closest_points, calculate_distance


class ClosestPointsTestCase(TestCase):
    def setUp(self):
        self.points = [
            Point.objects.create(x=2, y=2),
            Point.objects.create(x=-1, y=30),
            Point.objects.create(x=20, y=11),
            Point.objects.create(x=4, y=5),
        ]

    def test_calculate_distance(self):
        point1 = Point(x=2, y=2)
        point2 = Point(x=4, y=5)
        expected_distance = 3.605551275463989
        self.assertAlmostEqual(calculate_distance(point1, point2), expected_distance)

    def test_find_closest_points(self):
        expected_closest_points = [self.points[0], self.points[3]]
        closest_points = find_closest_points(self.points)
        self.assertCountEqual(closest_points, expected_closest_points)
