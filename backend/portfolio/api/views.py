from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Q
from datetime import date
from core.models import PersonalInfo, Skill, Project, Experience, Certification, SocialLink
from api.serializers import *

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    
    def list(self, request):
        # Return first personal info entry
        instance = self.queryset.first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
    def list(self, request):
        skills_by_category = {}
        for skill in self.queryset:
            category = skill.get_category_display()
            if category not in skills_by_category:
                skills_by_category[category] = []
            skills_by_category[category].append(SkillSerializer(skill).data)
        
        return Response(skills_by_category)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer

@api_view(['GET'])
def portfolio_stats(request):
    """Get portfolio statistics"""
    total_projects = Project.objects.count()
    total_certifications = Certification.objects.count()
    
    # Calculate total experience in years
    experiences = Experience.objects.all()
    total_months = 0
    for exp in experiences:
        end_date = exp.end_date if exp.end_date else date.today()
        total_months += (end_date.year - exp.start_date.year) * 12 + (end_date.month - exp.start_date.month)
    
    total_years = total_months // 12
    
    stats = {
        'total_projects': total_projects,
        'total_certifications': total_certifications,
        'total_experience_years': total_years,
        'skills_by_category': Skill.objects.values('category').annotate(count=Count('id'))
    }
    
    return Response(stats)