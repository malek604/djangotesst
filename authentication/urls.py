from django.urls import path
from . import views 



urlpatterns = [
    path('sighnup/',views.signup,name='signup'),
]