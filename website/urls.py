from django.urls import path, include
from website.views import home_light
app_name = 'website'

urlpatterns = [
    path('', home_light, name='home'),
    path('dark/', home_light, name='home_dark'),

]