from django.contrib import admin
from notes.models import Notes
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'notes']

admin.site.register(Notes, NotesAdmin)
