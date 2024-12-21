
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class Club(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, through='ClubMembership')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clubs'

class ClubMembership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='member')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'club_memberships'
        unique_together = ('user', 'club')


# serializers.py
from rest_framework import serializers
from django.core.validators import EmailValidator
import re

class ClubAccessSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    password = serializers.CharField(write_only=True)
    club_id = serializers.UUIDField()

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter")
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("Password must contain at least one number")
        return value

# backend.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


# views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Club, ClubMembership
from .serializers import ClubAccessSerializer
import logging

logger = logging.getLogger(__name__)

class ClubAccessView(APIView):
    def post(self, request):
        serializer = ClubAccessSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {"error": "Invalid input", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Authenticate user
            user = authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )

            if not user:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Validate club existence
            club_id = serializer.validated_data['club_id']
            try:
                club = Club.objects.get(id=club_id)
            except Club.DoesNotExist:
                return Response(
                    {"error": "Club does not exist"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Check club membership
            membership = ClubMembership.objects.filter(user=user, club=club).first()
            if not membership:
                return Response(
                    {"error": "User is not a member of this club"},
                    status=status.HTTP_403_FORBIDDEN
                )

            # Success response
            return Response({
                "message": "Access granted",
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "role": membership.role
                },
                "club": {
                    "id": str(membership.club.id),
                    "name": membership.club.name
                }
            })

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response(
                {"error": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# urls.py
from django.urls import path
from my_app.views import ClubAccessView

urlpatterns = [
    path('api/club-access/', ClubAccessView.as_view(), name='club-access'),
]
