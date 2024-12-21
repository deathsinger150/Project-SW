from django.urls import path
from django.views.generic import TemplateView
from my_app import views   # Correct import, no need for 'my_project' in the import

from my_app.views import  (
    UserList, ClubList, AdminList, ClubBoardMemberList, ClubCommitteeList,
    ClubMemberList, ClubAchievementList, EventList, SessionList, CollaborationList, home_view
)

urlpatterns = [
    # API paths
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/clubs/', ClubList.as_view(), name='club-list'),
    path('api/admins/', AdminList.as_view(), name='admin-list'),
    path('api/club-board-members/', ClubBoardMemberList.as_view(), name='club-board-member-list'),
    path('api/club-committees/', ClubCommitteeList.as_view(), name='club-committee-list'),
    path('api/club-members/', ClubMemberList.as_view(), name='club-member-list'),
    path('api/club-achievements/', ClubAchievementList.as_view(), name='club-achievement-list'),
    path('api/events/', EventList.as_view(), name='event-list'),
    path('api/sessions/', SessionList.as_view(), name='session-list'),
    path('api/collaborations/', CollaborationList.as_view(), name='collaboration-list'),
    
    # Other Pages
    path('', TemplateView.as_view(template_name='test1.html'), name='home'),  # Home page pointing to test1.html
    path('about-us/', TemplateView.as_view(template_name='about us.html'), name='about'),
    path('accept-member/', TemplateView.as_view(template_name='accept_member.html'), name='accept_member'),
    path('club-achievements/', TemplateView.as_view(template_name='club-achievements.html'), name='club_achievements'),
    path('create-event/', TemplateView.as_view(template_name='create_event.html'), name='create_event'),
    path('events/', TemplateView.as_view(template_name='events.html'), name='events'),
    path('gdg-sessions/', TemplateView.as_view(template_name='gdg_sessions.html'), name='gdg_sessions'),
    path('handle-collaboration/', TemplateView.as_view(template_name='Handel Collaboration.html'), name='handle_collaboration'),
    path('home/', TemplateView.as_view(template_name='Home.html'), name='homepage'),
    path('icpc-sessions/', TemplateView.as_view(template_name='icpc_sessions.html'), name='icpc_sessions'),
    path('leave-club/', TemplateView.as_view(template_name='Leave Club.html'), name='leave_club'),
    path('manage-academic-achievements/', TemplateView.as_view(template_name='Manage acadmic achivements html.html'), name='manage_academic_achievements'),
    path('manage-club-members/', TemplateView.as_view(template_name='Manage Club Members.html'), name='manage_club_members'),
    path('manage-events/', TemplateView.as_view(template_name='Manage events.html'), name='manage_events'),
    path('manage-sessions/', TemplateView.as_view(template_name='Manage sessions.html'), name='manage_sessions'),
    path('reason-leave/', TemplateView.as_view(template_name='reason_leave.html'), name='reason_leave'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('rpm-sessions/', TemplateView.as_view(template_name='rpm_sessions.html'), name='rpm_sessions'),
    path('sessions/', TemplateView.as_view(template_name='sessions.html'), name='sessions'),
    path('achievements/', views.achievements_view, name='achievements'),
    path('student/', TemplateView.as_view(template_name='Student.html'), name='student'),
    path('test1/', TemplateView.as_view(template_name='test1.html'), name='home'),
    
    
    path('', views.home_view, name='home'),
    
    path('test1/', views.test1_view, name='test1'),
    
    path('access-club/', views.access_club_view, name='access_club'),  # Correct path for access club
    
    path('about/', views.about_us_view, name='about'),
    
    path('accept-member/', views.accept_member_view, name='accept_member'),
    
    # Club Achievements page
    path('club-achievements/', views.club_achievements_view, name='club_achievements'),
    
    # Create Event page
    path('create-event/', views.create_event_view, name='create_event'),
    
    # Events page
    path('events/', views.events_view, name='events'),
    
    # GDG Sessions page
    path('gdg-sessions/', views.gdg_sessions_view, name='gdg_sessions'),
            
    # ICPC Sessions page
    path('icpc-sessions/', views.icpc_sessions_view, name='icpc_sessions'),
    
    path('manage-club-members/', views.manage_club_members_view, name='manage_club_members'),
    
    path('manage-events/', views.manage_events_view, name='manage_events'),
    
    path('manage-sessions/', views.manage_sessions_view, name='manage_sessions'),
    
    path('handle-collaboration/', views.handle_collaboration_view, name='handle_collaboration'),
    
    path('manage-academic-achievements/', views.manage_academic_achievements_view, name='manage_academic_achievements'),
    
    path('leave-club/', views.leave_club_view, name='leave_club'),
    
    # Reason Leave page
    path('reason-leave/', views.reason_leave_view, name='reason_leave'),
    
    # Register page
    path('register/', views.register_view, name='register'),
    
    # RPM Sessions page
    path('rpm-sessions/', views.rpm_sessions_view, name='rpm_sessions'),
    
    # Sessions page
    path('sessions/', views.sessions_view, name='sessions'),
    
    path('access-club-hub/', views.access_club_view, name='access_club_hub'),
    
    path('admin-login/', views.admin_login_view, name='admin_login'),
    
    path('student-login/', views.student_login_view, name='student_login'),
    
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

        # Manage Club Members page
    path('manage-club-members/', views.manage_club_members_view, name='manage_club_members'),
    
    # Accept Member page (requires member ID)
    path('accept-member/<int:member_id>/', views.accept_member_view, name='accept_member'),
    
    # Admin dashboard
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),

    path('accept-member/', views.accept_member_view, name='accept_member'),

    path('icpc-achievements/', views.icpc_achievements_view, name='icpc_achievements'),
    
    path('rpm-achievements/', views.rpm_achievements_view, name='rpm_achievements'),
    
    path('gdg-achievements/', views.gdg_achievements_view, name='gdg_achievements'),

    path('remove-member/', views.remove_member_view, name='remove_member'),
]
