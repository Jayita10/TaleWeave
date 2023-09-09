from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),  # Add URL pattern for the homepage if needed
    path('create_story/', views.create_story, name='create_story'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('submit_decision/<int:story_id>/', views.submit_decision, name='submit_decision'),
]
