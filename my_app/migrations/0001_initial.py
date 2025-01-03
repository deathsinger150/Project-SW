# Generated by Django 5.1.4 on 2024-12-20 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('joined_clubs', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Admin', 'Admin'), ('ClubMember', 'ClubMember'), ('ClubBoardMember', 'ClubBoardMember')], default='Student', max_length=20)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Clubs',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='my_app.user')),
            ],
            options={
                'db_table': 'Admins',
            },
        ),
        migrations.CreateModel(
            name='ClubBoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.user')),
            ],
            options={
                'db_table': 'ClubBoardMembers',
            },
        ),
        migrations.CreateModel(
            name='ClubCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee_name', models.CharField(max_length=100)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.club')),
            ],
            options={
                'db_table': 'ClubCommittees',
            },
        ),
    ]
