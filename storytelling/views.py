from django.shortcuts import render, redirect
from .models import Story, Decision

def create_story(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        initial_decision = request.POST.get('initial_decision')
        
        # Create a new story in the database
        new_story = Story(title=title, description=description, creator=request.user)
        new_story.save()
        
        # Create the initial decision for the story
        initial_decision = Decision(story=new_story, author=request.user, text=initial_decision)
        initial_decision.save()
        
        # Redirect to the story detail page
        return redirect('story_detail', story_id=new_story.id)

    return render(request, 'storytelling/create_story.html')

def story_detail(request, story_id):
    try:
        story = Story.objects.get(id=story_id)
    except Story.DoesNotExist:
        # Handle the case where the story does not exist
        return redirect('index')
    
    if request.method == 'POST':
        decision_text = request.POST.get('decision')
        
        # Create a new decision for the story
        new_decision = Decision(story=story, author=request.user, text=decision_text)
        new_decision.save()
    
    return render(request, 'storytelling/story_detail.html', {'story': story})

def submit_decision(request, story_id):
    if request.method == 'POST':
        decision_text = request.POST.get('decision')
        # Process the decision, e.g., save it to the database
        decision = Decision(story_id=story_id, author=request.user, text=decision_text)
        decision.save()
    return redirect('story_detail', story_id=story_id)

