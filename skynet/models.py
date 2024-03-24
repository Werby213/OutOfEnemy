from django.db import models

# Create your models here.

class Meta:
    verbose_name = "Услуга"
    verbose_name_plural = "Услуги"

class Services(models.Model):
    title = models.TextField(max_length=255, verbose_name="Заголовок")
    content = models.CharField(blank=True, max_length=200,verbose_name="Контент")
    photo = models.ImageField(upload_to="skynet/images",verbose_name="Изображение")
    time_c = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    time_u = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    is_p = models.BooleanField(default=True, verbose_name="Публикация")