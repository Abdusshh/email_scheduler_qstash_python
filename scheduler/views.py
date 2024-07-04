from croniter import croniter
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.email_scheduler import schedule_email, schedule_email_cronjob
from .utils.send_email import send_email

@csrf_exempt
def schedule_email_view(request):
    email_scheduled = False
    
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        schedule_date_str = request.POST.get('schedule_date')
        cron_string = request.POST.get('cron_string')

        email_data = {
            'to_email': to_email,
            'subject': subject,
            'content': content
        }

        if cron_string:
            # Validate cron string format
            if not croniter.is_valid(cron_string):
                return render(request, 'schedule_email.html', {
                    'email_scheduled': email_scheduled,
                    'error': 'Invalid cron string format. Please enter a valid cron string.'
                })
            # Schedule with cron string
            schedule_email_cronjob(email_data, cron_string)
            email_scheduled = True

        elif schedule_date_str:
            # Schedule with specific date and time
            schedule_date = datetime.strptime(schedule_date_str, '%Y-%m-%dT%H:%M')
            current_date = datetime.now()

            # Check if schedule date is in the past
            if schedule_date < current_date:
                return render(request, 'schedule_email.html', {
                    'email_scheduled': email_scheduled,
                    'error': 'Schedule date cannot be in the past.'
                })
            
            # Check if schedule date is in the future more than a week
            if (schedule_date - current_date).total_seconds() > 604800:
                return render(request, 'schedule_email.html', {
                    'email_scheduled': email_scheduled,
                    'error': 'Schedule date cannot be more than a week in the future for free pricing.'
                })
            
            delay = int((schedule_date - current_date).total_seconds())
            schedule_email(email_data, delay)
            email_scheduled = True
            
        else:
            return render(request, 'schedule_email.html', {
                'email_scheduled': email_scheduled,
                'error': 'Please provide either a schedule date or a cron string.'
            })

        return render(request, 'schedule_email.html', {'email_scheduled': email_scheduled})
    
    return render(request, 'schedule_email.html', {'email_scheduled': email_scheduled})

@csrf_exempt
def send_email_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_email = data['to_email']
        subject = data['subject']
        content = data['content']
        
        response = send_email(to_email, subject, content)
        return JsonResponse({'status': response.status_code})
    return JsonResponse({'error': 'Invalid request'}, status=400)
