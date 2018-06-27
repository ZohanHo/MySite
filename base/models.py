from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta():
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"