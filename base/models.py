from django.db import models

class InfoUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)  # При создании нового екзесмпляра будет подставлена текущаяя дата

    # def save(self, **kwargs):
    #     super(Test, self).save()

    class Meta():
        verbose_name = "Инфо Юзера"
        verbose_name_plural = "Инфо Юзеров"

    def __str__(self): # Даем строковое представление обьекта, а именно записи в базе
        try:    # Если не возникнит ошибки в блоке try, он выполнится, иначе блок except
            return "Имя пользователя: {} {}".format(self.name, self.id)    # Может быть ошибка если поле name не найдено, тогда except
        except:
            return "{} {}".format(self.id, self.pk)   # Id всегда есть. Mожно выводить пару полей, пример еще pk

class MaxInfoUser(models.Model):
    viber = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=50)
    infouser = models.ForeignKey(InfoUser, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Инфа юзера")
    date = models.DateField(auto_now_add=True) # При создании нового екзесмпляра будет подставлена текущаяя дата

    class Meta():
        verbose_name = "Полная Информация"
        verbose_name_plural = "Полная Информация"

    # def __unicode__(self):
    #     return self.pk or self.phone


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES) #С помощью етой конструкции можно добавить список