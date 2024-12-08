We used here Fast API, DRF, Celery, Redis  
Start Fast App server: uvicorn main:app --reload  
Start redis server using exe  
Start Celery server: celery -A django_app worker -l info -P eventlet  
Start Django project server: python manage.py runserver 8001
