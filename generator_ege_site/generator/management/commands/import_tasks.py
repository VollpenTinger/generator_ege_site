import csv
import os
from django.core.management.base import BaseCommand
from generator.models import Task

class Command(BaseCommand):
    help = 'Импортирует задачи из CSV файла'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к CSV файлу')
    
    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        if not os.path.exists(csv_file_path):
            self.stdout.write(
                self.style.ERROR(f'Файл {csv_file_path} не найден')
            )
            return
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            tasks_created = 0
            tasks_updated = 0
            errors = []
            
            for row_num, row in enumerate(csv_reader, start=2):
                try:
                    # Очистка и преобразование данных из вашего CSV
                    local_num = row['local_num'].strip()
                    bank_num = row['bank_num'].strip()
                    answer = row['answer'].strip().strip('"')  # Убираем кавычки
                    category = row['category'].strip()
                    
                    # Обработка ответа с запятой (например " 4,8" -> "4.8")
                    answer = answer.replace(',', '.').strip()
                    
                    # Создаем данные для задачи
                    task_data = {
                        'global_id': bank_num,
                        'variant_number': int(category),
                        'answer': answer,
                    }
                    
                    # Создаем или обновляем задание
                    task, created = Task.objects.update_or_create(
                        global_id=task_data['global_id'],
                        defaults=task_data
                    )
                    
                    if created:
                        tasks_created += 1
                        self.stdout.write(f"Создано: {task.global_id}")
                    else:
                        tasks_updated += 1
                        self.stdout.write(f"Обновлено: {task.global_id}")
                        
                except Exception as e:
                    errors.append(f"Строка {row_num}: {str(e)} - Данные: {row}")
                    self.stdout.write(
                        self.style.ERROR(f'Ошибка в строке {row_num}: {str(e)}')
                    )
            
            # Вывод итогов
            self.stdout.write(
                self.style.SUCCESS(
                    f'Импорт завершен: {tasks_created} создано, {tasks_updated} обновлено'
                )
            )
            
            if errors:
                self.stdout.write(
                    self.style.WARNING(f'Найдено ошибок: {len(errors)}')
                )
                for error in errors:
                    self.stdout.write(f"  - {error}")