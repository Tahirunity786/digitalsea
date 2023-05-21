from django.urls import path
from .views import main
urlpatterns = [    
    # MAIN URLS
    path('', main, name='Home'),
    
]