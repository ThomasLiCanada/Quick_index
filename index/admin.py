from django.contrib import admin
from .models import Index


class IndexAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Index._meta.get_fields()]
    # class Meta:
    #     model = Index
    #     fields = '__all__'


admin.site.register(Index, IndexAdmin)
