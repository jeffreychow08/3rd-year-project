from django.urls import path

from . import views

app_name = 'calendar_ting'

urlpatterns = [
  path('', views.home, name='home'),
  path('signin/', views.sign_in, name='signin'),
  path('calendar/', views.calendar, name='calendar'),
  path('callback/', views.callback, name='callback'),
  path('signout/', views.sign_out, name='signout'),
  path('calendar/new/', views.newevent, name='newevent'),
  path('calendar/event/<str:eid>', views.event, name='event'),
]
