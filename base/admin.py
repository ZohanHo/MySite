from django.contrib import admin
from base.models import InfoUser, MaxInfoUser


# Регистрировать каждую можель нужно отдельно, новой строкой
admin.site.register(InfoUser)
admin.site.register(MaxInfoUser)