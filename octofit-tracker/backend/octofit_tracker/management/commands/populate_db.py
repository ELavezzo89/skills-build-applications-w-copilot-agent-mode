from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User(email='tony@stark.com', username='IronMan', team=marvel, is_superhero=True),
            User(email='steve@rogers.com', username='CaptainAmerica', team=marvel, is_superhero=True),
            User(email='bruce@wayne.com', username='Batman', team=dc, is_superhero=True),
            User(email='clark@kent.com', username='Superman', team=dc, is_superhero=True),
        ]
        for user in users:
            user.save()

        # Create Workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', suggested_for='All'),
            Workout(name='Running', description='Cardio endurance', suggested_for='All'),
        ]
        for workout in workouts:
            workout.save()

        # Create Activities
        activities = [
            Activity(user=users[0], activity_type='Pushups', duration_minutes=10, points=50),
            Activity(user=users[1], activity_type='Running', duration_minutes=30, points=100),
            Activity(user=users[2], activity_type='Pushups', duration_minutes=15, points=70),
            Activity(user=users[3], activity_type='Running', duration_minutes=25, points=90),
        ]
        for activity in activities:
            activity.save()

        # Create Leaderboard
        for idx, user in enumerate(users):
            total_points = sum(a.points for a in Activity.objects.filter(user=user))
            Leaderboard.objects.create(user=user, total_points=total_points, rank=idx+1)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
