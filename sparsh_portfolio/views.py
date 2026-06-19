from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
 
 
def home(request):
    projects = [
        {
            'id': 1,
            'title': 'Brand Identity',
            'category': 'Design',
            'year': '2024',
            'description': 'Complete brand system for a luxury lifestyle brand.',
            'tags': ['Branding', 'Typography', 'Motion'],
        },
        {
            'id': 2,
            'title': 'E-Commerce Platform',
            'category': 'Development',
            'year': '2024',
            'description': 'Full-stack web application with real-time inventory.',
            'tags': ['Django', 'React', 'PostgreSQL'],
        },
        {
            'id': 3,
            'title': 'Mobile UI System',
            'category': 'UI/UX',
            'year': '2023',
            'description': 'Design system and prototypes for iOS application.',
            'tags': ['Figma', 'iOS', 'Design System'],
        },
        {
            'id': 4,
            'title': 'Photography Portfolio',
            'category': 'Creative',
            'year': '2023',
            'description': 'Cinematic visual storytelling through street photography.',
            'tags': ['Photography', 'Editing', 'Curation'],
        },
    ]
    return render(request, 'home.html', {'projects': projects})
 
 
def about(request):
    skills = [
        {'name': 'UI/UX Design', 'level': 90},
        {'name': 'Web Development', 'level': 85},
        {'name': 'Django / Python', 'level': 80},
        {'name': 'Brand Identity', 'level': 75},
        {'name': 'Motion Design', 'level': 70},
        {'name': 'Photography', 'level': 85},
    ]
    return render(request, 'about.html', {'skills': skills})
 
 
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
 
        if name and email and message:
            messages.success(request, f"Thanks {name}! Your message has been received. I'll be in touch soon.")
        else:
            messages.error(request, 'Please fill in all required fields.')
        return redirect('contact')
 
    return render(request, 'contact.html')
