from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'personal-info', views.PersonalInfoViewSet, basename='personalinfo')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'experience', views.ExperienceViewSet, basename='experience')
router.register(r'certifications', views.CertificationViewSet, basename='certification')
router.register(r'social-links', views.SocialLinkViewSet, basename='sociallink')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/stats/', views.portfolio_stats, name='portfolio-stats'),
]