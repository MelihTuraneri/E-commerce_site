from django.contrib import admin
from .models import person
from .models import Todo
from .models import ortak
# Register your models here.

admin.site.register(Todo)

admin.site.register(person)

admin.site.register(ortak)
