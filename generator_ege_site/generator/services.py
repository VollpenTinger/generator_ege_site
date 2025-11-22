import random
from .models import Task

def get_random_tasks_from_variant(variant_number, num_tasks=4):
    """
    Берет случайные задания из конкретного варианта
    """
    tasks = list(Task.objects.filter(variant_number=variant_number))
    
    if len(tasks) <= num_tasks:
        return tasks
    else:
        return random.sample(tasks, num_tasks)

def get_available_variants():
    """
    Возвращает список всех вариантов, которые есть в БД
    """
    variants = Task.objects.values_list('variant_number', flat=True).distinct()
    return sorted(variants)

def get_task_image_path(task):
    """
    Возвращает путь к изображению для задания
    Использует global_id для формирования пути
    """
    return f"tasks/{task.variant_number}/{task.global_id}.jpg"