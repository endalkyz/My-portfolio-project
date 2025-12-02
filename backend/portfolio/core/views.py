from django.shortcuts import render, redirect
from django.db.models import Count
from datetime import date
from django.contrib import messages
from core.models import PersonalInfo, Skill, Project, Experience, Certification, SocialLink, Education

def home(request):
    try:
        # Get all data from database
        personal_info = PersonalInfo.objects.first()
        education = Education.objects.all().order_by('-start_date') 
        skills = Skill.objects.all()
        projects = Project.objects.all()
        experience = Experience.objects.all().order_by('-start_date')
        certifications = Certification.objects.all().order_by('-issue_date')
        social_links = SocialLink.objects.all().order_by('display_order')
        
        # Group skills by category
        skills_by_category = {}
        for skill in skills:
            category_display = skill.get_category_display()
            if category_display not in skills_by_category:
                skills_by_category[category_display] = []
            skills_by_category[category_display].append(skill)
        
        # Calculate statistics
        projects_count = projects.count()
        certifications_count = certifications.count()
        
        # Calculate total experience in years
        total_months = 0
        for exp in experience:
            end_date = exp.end_date if exp.end_date else date.today()
            total_months += (end_date.year - exp.start_date.year) * 12 + (end_date.month - exp.start_date.month)
        experience_years = total_months // 12
        
        context = {
            'personal_info': personal_info,
            'education': education,
            'skills_by_category': skills_by_category,
            'projects': projects,
            'experience': experience,
            'certifications': certifications,
            'social_links': social_links,
            'projects_count': projects_count,
            'certifications_count': certifications_count,
            'experience_years': experience_years,
        }
        
        return render(request, 'portfolio.html', context)
    
    except Exception as e:
        print(f"Error in home view: {e}")
        # Return a basic template even if there's an error
        return render(request, 'portfolio.html', {})
    

 
def contact_submit(request):
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send email
        # 3. etc.
        
        print(f"Contact form received: {name}, {email}, {subject}, {message}")
        
        # Redirect back to home with success message
        return redirect('home')
    
    # If not POST, redirect to home
    return redirect('home')