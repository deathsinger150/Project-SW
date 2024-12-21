import hashlib
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
import logging
from .models import User, Club, Admin, ClubBoardMember, ClubCommittee, ClubMember, ClubAchievement, Event, Session, Collaboration
from .serializers import (
    UserSerializer, ClubSerializer, AdminSerializer, ClubBoardMemberSerializer,
    ClubCommitteeSerializer, ClubMemberSerializer, ClubAchievementSerializer,
    EventSerializer, SessionSerializer, CollaborationSerializer
)
logger = logging.getLogger(__name__)

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ClubList(APIView):
    def get(self, request):
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)


class AdminList(APIView):
    def get(self, request):
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)


class ClubBoardMemberList(APIView):
    def get(self, request):
        board_members = ClubBoardMember.objects.all()
        serializer = ClubBoardMemberSerializer(board_members, many=True)
        return Response(serializer.data)


class ClubCommitteeList(APIView):
    def get(self, request):
        committees = ClubCommittee.objects.all()
        serializer = ClubCommitteeSerializer(committees, many=True)
        return Response(serializer.data)


class ClubMemberList(APIView):
    def get(self, request):
        club_members = ClubMember.objects.all()
        serializer = ClubMemberSerializer(club_members, many=True)
        return Response(serializer.data)


class ClubAchievementList(APIView):
    def get(self, request):
        achievements = ClubAchievement.objects.all()
        serializer = ClubAchievementSerializer(achievements, many=True)
        return Response(serializer.data)


class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class SessionList(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)


class CollaborationList(APIView):
    def get(self, request):
        collaborations = Collaboration.objects.all()
        serializer = CollaborationSerializer(collaborations, many=True)
        return Response(serializer.data)
    
# Home Page (test1.html)
def home_view(request):
    return render(request, 'test1.html', {})

def test1_view(request):
    return render(request, 'test1.html')

def access_club_view(request):
    return render(request, 'Access Your Club Hub.html')

# About Us Page
def about_us_view(request):
    return render(request, 'about us.html', {})

def accept_member_view(request):
    return render(request, 'accept_member.html')

# Club Achievements Page
def club_achievements_view(request):
    return render(request, 'club-achievements.html')

# Create Event Page
def create_event_view(request):
    return render(request, 'create_event.html')

# Events Page
def events_view(request):
    return render(request, 'events.html')

# GDG Sessions Page
def gdg_sessions_view(request):
    return render(request, 'gdg_sessions.html')

# Handle Collaboration Page
def handle_collaboration_view(request):
    return render(request, 'Handel Collaboration.html')

# Home Page (duplicate for Home.html)
def main_home_view(request):
    return render(request, 'Home.html')

# ICPC Sessions Page
def icpc_sessions_view(request):
    return render(request, 'icpc_sessions.html')

# Reason Leave Page
def reason_leave_view(request):
    return render(request, 'reason_leave.html')

# Register Page
def register_view(request):
    return render(request, 'register.html')

# RPM Sessions Page
def rpm_sessions_view(request):
    return render(request, 'rpm_sessions.html')

# Sessions Page
def sessions_view(request):
    return render(request, 'sessions.html')

def manage_club_members_view(request):
    return render(request, 'Manage Club Members.html')

def manage_events_view(request):
    return render(request, 'Manage events.html')

def manage_sessions_view(request):
    return render(request, 'Manage sessions.html')

def handle_collaboration_view(request):
    return render(request, 'Handel Collaboration.html')

def achievements_view(request):
    return render(request, 'achievements.html')


def manage_academic_achievements_view(request):
    return render(request, 'Manage acadmic achivements html.html')

def leave_club_view(request):
    return render(request, 'Leave Club.html')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

logger = logging.getLogger(__name__)

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Admin-Username')
        password = request.POST.get('password_user')
        admin_id = request.POST.get('user_id')

        # Hash the password entered by the user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        print(f"Username: {username}, Password: {password}, Hashed: {hashed_password}, Admin ID: {admin_id}")

        # Try to find the user in the database
        user = User.objects.filter(user_name=username, Users_password=hashed_password, Users_role="Admin").first()

        if user:
            print(f"User found: {user}")
            return redirect('admin_dashboard')
        else:
            print("No admin found with these credentials.")
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('access_club_hub')

    return render(request, 'access_club_hub.html')



def student_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Student-Username')
        password = request.POST.get('password_student')

        # Hash the password entered by the user
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        print(f"Username: {username}, Password: {password}, Hashed: {hashed_password}")

        # Try to find the user in the database with a role not equal to "Admin"
        user = User.objects.exclude(Users_role="Admin").filter(
            user_name=username,
            Users_password=hashed_password
        ).first()

        if user:
            print(f"User found: {user}")
            return redirect('student_dashboard')
        else:
            print("No student found with these credentials.")
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('access_club_hub')

    return render(request, 'access_club_hub.html')



def admin_dashboard(request):
    return render(request, 'admin.html')


def student_dashboard(request):
    return render(request, 'student.html')

def your_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username_field')
        password = request.POST.get('password_field')
        print("Received username:", username)
        print("Received password:", password)

        user = User.objects.filter(username=username).first()
        if user:
            print("User found:", user.username)
            # Add password verification logic here
        else:
            print("No user found")

        return redirect('some_success_url')  # Or handle failure

# Accept Member view
def accept_member_view(request):
    return render(request, 'accept_member.html')

# Admin dashboard view
def admin_dashboard_view(request):
    return render(request, 'admin.html')

def icpc_achievements_view(request):
    return render(request, 'icpc_achiv.html')

def rpm_achievements_view(request):
    return render(request, 'rpm_achiv.html')

def gdg_achievements_view(request):
    return render(request, 'gdg_achiv.html')

def remove_member_view(request):
    student_id = request.GET.get('id')
    if student_id:
        try:
            user = User.objects.get(id=student_id)
            user.delete()
            messages.success(request, f"Member with ID {student_id} has been successfully removed.")
        except User.DoesNotExist:
            messages.error(request, "Member not found.")
    else:
        messages.error(request, "No ID provided.")
    return redirect('admin_dashboard')