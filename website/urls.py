from django.urls import path
from website.views import home
app_name = 'website'

urlpatterns = [
    path('', home, name='home_light'),
    path('<str:theme>/', home, name='home_theme'),
]