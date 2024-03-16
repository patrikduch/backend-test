# Generated by Django 5.0.3 on 2024-03-16 20:11

from django.db import migrations
from django.utils import timezone
from django.contrib.auth.models import User

def get_users_data():
    return [
        {'username': 'admin1', 'password': 'password123', 'email': 'admin1@example.com', 'date_joined': timezone.datetime(2023, 7, 1)},
        {'username': 'admin2', 'password': 'password123', 'email': 'admin2@example.com', 'date_joined': timezone.datetime(2023, 6, 2)},
    ]


def add_past_admin_users(apps, schema_editor):
    # List of users to add
    users_to_create = get_users_data()

    for user_data in users_to_create:
        user = User.objects.create_superuser(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        user.date_joined = user_data['date_joined']
        user.save()

def remove_past_admin_users(apps, schema_editor):
    # Remove the users created above
    User.objects.filter(username__in=[user['username'] for user in get_users_data()]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_get_registered_users_pr'),
    ]

    operations = [
        migrations.RunPython(add_past_admin_users, remove_past_admin_users),
    ]
