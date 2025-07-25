from django.contrib import admin
from .models import beginner,intermediate,pro
# Register your models here.
admin.site.register(beginner)
admin.site.register(intermediate)
admin.site.register(pro)
