from django.urls import path
from .views import schedule_email_view, send_email_view

urlpatterns = [
    path('schedule-email', schedule_email_view, name='schedule-email'),
    path('send-email', send_email_view, name='send-email'),
]
