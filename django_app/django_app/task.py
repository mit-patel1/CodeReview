from celery import Celery
from django.core.files.base import ContentFile
from django.utils import timezone
from home.models import TaskStatus, RepoData
import base64
import time
import requests
from groq import Groq
from celery import shared_task

# Set up Celery in Django
app = Celery('django_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
from home.utils.ai_agent import analyze_pr
 

# Celery task for processing file content and analyzing it
@shared_task
def analyze_repo_task(owner, repo, github_token=None):
    result = analyze_pr(owner, repo, github_token=None)
    return result