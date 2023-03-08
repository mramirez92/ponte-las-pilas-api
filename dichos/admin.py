from django.contrib import admin
from .models import Dicho


class DichoAdmin(admin.ModelAdmin):
    list_display = ('id', 'saying', 'translation', 'category')
    fields = ('saying', 'translation', 'category')


admin.site.register(Dicho, DichoAdmin)
