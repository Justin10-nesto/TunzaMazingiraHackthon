from django.urls import path, include
from . import views
urlpatterns = [
    path('addSchedule', views.addSchedule, name = 'addSchedule'),
    path('', views.viewSchedule, name = 'viewSchedule'),
        path('deleteSchedule/<str:id>', views.deleteSchedule, name ='deleteSchedule'),

]
