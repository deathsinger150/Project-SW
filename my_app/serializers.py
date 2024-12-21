from rest_framework import serializers
from .models import User, Club, Admin, ClubBoardMember, ClubCommittee, ClubMember, ClubAchievement, Event, Session, Collaboration


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'joined_clubs', 'email', 'role', 'password']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'club_name', 'description']


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id']


class ClubBoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubBoardMember
        fields = ['club', 'user', 'position']


class ClubCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCommittee
        fields = ['id', 'club', 'committee_name']


class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = ['club', 'user', 'committee']


class ClubAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubAchievement
        fields = ['club', 'admin', 'achievement', 'date_awarded']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_id', 'club_name', 'event_name', 'description', 'club',
            'admin', 'location', 'staff_list', 'sponsors', 'event_date'
        ]


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'track_sessions', 'club_name', 'club', 'admin', 'instructor',
            'schedule', 'attendance_count', 'material_file'
        ]


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = [
            'applying_club', 'receiving_club', 'applying_admin', 'receiving_admin',
            'description', 'status', 'application_date'
        ]
