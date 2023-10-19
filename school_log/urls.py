from django.urls import path

from .views import index, subject, SchoolMessageCreateView

urlpatterns = [
   path('add/', SchoolMessageCreateView.as_view(), name = 'add'),
   path('<int:subject_id>/', subject, name="subject"),
   path('', index, name="index"),
]