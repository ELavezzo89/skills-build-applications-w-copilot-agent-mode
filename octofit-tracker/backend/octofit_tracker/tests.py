from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        self.assertEqual(str(user), 'TestUser')
    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        activity = Activity.objects.create(user=user, activity_type='Run', duration_minutes=30, points=100)
        self.assertEqual(str(activity), 'TestUser - Run')
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout')
        self.assertEqual(str(workout), 'Test Workout')
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='TestUser', team=team)
        leaderboard = Leaderboard.objects.create(user=user, total_points=100, rank=1)
        self.assertEqual(str(leaderboard), 'TestUser - 100 pts')
