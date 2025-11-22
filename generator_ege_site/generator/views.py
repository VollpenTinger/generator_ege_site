from django.shortcuts import render
from .services import get_random_tasks_from_variant, get_task_image_path

def generator(request):
    return render(request, 'generator/generator.html')

def generate_variant(request, variant_id):
    tasks = get_random_tasks_from_variant(variant_id, num_tasks=4)
    
    # Добавляем путь к изображению для каждого задания
    for task in tasks:
        task.image_path = get_task_image_path(task)
    
    context = {
        'variant_number': variant_id,
        'tasks': tasks,
    }
    return render(request, 'generator/generate_variant.html', context)