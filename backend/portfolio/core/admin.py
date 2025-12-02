from django.contrib import admin
from .models import PersonalInfo, Skill, Project, Experience, Certification, SocialLink, Education

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'job_title', 'email', 'updated_at']
    search_fields = ['full_name', 'job_title']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'category', 'display_order']
    list_filter = ['category']
    search_fields = ['skill_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    filter_horizontal = []

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'current_job']
    list_filter = ['current_job', 'start_date']
    search_fields = ['company', 'position']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date']
    list_filter = ['issuing_organization', 'issue_date']
    search_fields = ['name', 'issuing_organization']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'display_order']
    list_filter = ['platform']
    search_fields = ['platform', 'url']




@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'currently_studying']
    list_filter = ['degree', 'currently_studying', 'start_date']
    search_fields = ['institution', 'field_of_study']
    ordering = ['-start_date']