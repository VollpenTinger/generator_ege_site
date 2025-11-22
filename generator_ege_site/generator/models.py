from django.db import models

class Task(models.Model):
    local_id = models.AutoField(primary_key=True, verbose_name="Локальный ID")
    global_id = models.CharField(max_length=50, unique=True, verbose_name="Глобальный ID")
    variant_number = models.IntegerField(verbose_name="Номер варианта")
    answer = models.CharField(max_length=100, verbose_name="Ответ")
    
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ['variant_number', 'global_id']
    
    def get_image_path(self):
        """Генерирует путь к изображению на основе global_id"""
        return f"tasks/{self.variant_number}/{self.global_id}.jpg"
    
    def __str__(self):
        return f"{self.global_id} (Вариант {self.variant_number})"