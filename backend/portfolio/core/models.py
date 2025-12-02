from django.db import models
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Skills'),
        ('Softskils', 'Soft Skills'),

    ]
    
    skill_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'display_order', 'skill_name']

    def __str__(self):
        return f"{self.skill_name}"  # Fixed this line

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.TextField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

    class Meta:
        ordering = ['-featured', '-start_date']

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current_job = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('website', 'Personal Website'),
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
    ]
    
    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    url = models.URLField()
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.get_platform_display()}: {self.url}"


class Education(models.Model):
    DEGREE_CHOICES = [
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('associate', 'Associate Degree'),
        ('bachelor', 'Bachelor\'s Degree'),
        ('master', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ]
    
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='bachelor')
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_studying = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    institution_logo = models.ImageField(upload_to='education_logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"