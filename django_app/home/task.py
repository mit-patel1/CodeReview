from celery import Celery
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