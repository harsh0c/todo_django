from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Display list of To-Do tasks
def task_list(request):
    tasks = Task.objects.all().order_by('priority', 'due_date')  # Sort by priority, then due date
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# Add a new To-Do task
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', None)
        priority = request.POST.get('priority', 'Medium')
        completed = request.POST.get('completed', 'off') == 'on'
        
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date if due_date else None,
            priority=priority,
            completed=completed
        )
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

# Edit a particular To-Do task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.due_date = request.POST.get('due_date', None)
        task.priority = request.POST.get('priority', 'Medium')
        task.completed = request.POST.get('completed', 'off') == 'on'
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task': task})

# Delete a particular To-Do task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

# Delete all To-Do tasks
def delete_all_tasks(request):
    Task.objects.all().delete()
    return redirect('task_list')
