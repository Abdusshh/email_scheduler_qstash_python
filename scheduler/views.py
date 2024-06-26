from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.email_scheduler import schedule_email
from .utils.send_email import send_email

@csrf_exempt
def schedule_email_view(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        delay = int(request.POST.get('delay', 0))
        
        email_data = {
            'to_email': to_email,
            'subject': subject,
            'content': content
        }
        
        schedule_email(email_data, delay)
        return HttpResponseRedirect(reverse('schedule-email'))
    
    return render(request, 'schedule_email.html')

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
