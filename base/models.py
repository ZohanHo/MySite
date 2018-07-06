from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta():
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self): # Даем строковое представление обьекта, а именно записи в базе
        try:    # Если не возникнит ошибки в блоке try, он выполнится, иначе блок except
            return "Имя пользователя: {}".format(self.name)    # Может быть ошибка если поле name не найдено, тогда except
        except:
            return "{} {}".format(self.id, self.pk)   # Id всегда есть, так же можно выводить пару полей