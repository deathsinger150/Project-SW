from django.db import models


class Club(models.Model):
    id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Clubs'


class User(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Admin', 'Admin'),
        ('ClubMember', 'ClubMember'),
        ('ClubBoardMember', 'ClubBoardMember'),
    ]
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    joined_clubs = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    Users_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    Users_password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Users'


class Admin(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'Admins'


class ClubBoardMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)

    class Meta:
        db_table = 'ClubBoardMembers'


class ClubCommittee(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    committee_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'ClubCommittees'


class ClubMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    committee = models.ForeignKey(ClubCommittee, on_delete=models.SET_NULL, blank=True, null=True, db_column='Club_member_committee')

    class Meta:
        db_table = 'ClubMembers'


class ClubAchievement(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    achievement = models.TextField()
    date_awarded = models.DateField()

    class Meta:
        db_table = 'ClubAchievements'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True, db_column='Events_description')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    staff_list = models.TextField(blank=True, null=True)
    sponsors = models.TextField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True, db_column='Events_date')

    class Meta:
        db_table = 'Events'


class Session(models.Model):
    track_sessions = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, db_column='instructor_id')
    schedule = models.TextField(blank=True, null=True, db_column='Sessions_schedule')
    attendance_count = models.IntegerField(blank=True, null=True)
    material_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Sessions'


class Collaboration(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    applying_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='applied_club', db_column='applying_club_id')
    receiving_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='received_club', db_column='receiving_club_id')
    applying_admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='applied_admin', db_column='applying_admin_id')
    receiving_admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='received_admin', db_column='receiving_admin_id')
    description = models.TextField(blank=True, null=True, db_column='collaboration_description')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', db_column='collaboration_status')
    application_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Collaboration'