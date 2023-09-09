# storytelling/models.py
from django.db import models
from django.contrib.auth.models import User

# Define a model for representing stories
class Story(models.Model):
    # Define fields for the Story model
    title = models.CharField(max_length=255)  # Title of the story
    description = models.TextField()           # Description or summary of the story
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who created the story
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the story was created

    # Define a user-friendly string representation of the Story model
    def __str__(self):
        return self.title

# Define a model for representing decisions made within a story
class Decision(models.Model):
    # Define fields for the Decision model
    story = models.ForeignKey(Story, on_delete=models.CASCADE)  # Link to the story where the decision was made
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who made the decision
    text = models.TextField()           # The text of the decision made by the user
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the decision was made

    # Define a user-friendly string representation of the Decision model
    def __str__(self):
        return f'Decision by {self.author.username} in {self.story.title}'
