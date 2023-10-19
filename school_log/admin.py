from django.contrib import admin

# Register your models here.
from .models import SchoolMessage, Subject

class SchoolMessageAdmin(admin.ModelAdmin):
   list_display = ('title', 'content', 'mark', 'published', 'subject')
   list_display_links = ('title', 'content')
   search_fields = ('title', 'content')

admin.site.register(SchoolMessage, SchoolMessageAdmin)
admin.site.register(Subject)