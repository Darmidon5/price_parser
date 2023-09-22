from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('company_info/<int:company_id>/', company_data),
    path('about', about, name='about')
]
