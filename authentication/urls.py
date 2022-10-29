from .views import Registration
from django.urls import path,include
urlpatterns = [
    path('register',Registration.as_view(),name='register')
]
