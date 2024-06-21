# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('member/dashboard/', views.member_dashboard, name='member_dashboard'),
#     path('finance/officer/dashboard/', views.finance_officer_dashboard, name='finance_officer_dashboard'),
#     # Add more URL patterns as needed
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('do_login/', views.doLogin, name='do_login'),
    path('logout/', views.logout_view, name='logout'),
    path('change_student_password/', views.change_student_password, name='change_student_password'),
    path('change_counsellor_password/', views.change_counsellor_password, name='change_counsellor_password'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_profile/', views.profile_view, name='student_profile'),
    path('counsellor_dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),
    path('counsellor_profile/', views.counsellor_profile_view, name='counsellor_profile'),
    
    # Add more URL patterns as needed
]
