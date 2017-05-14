from django.contrib import admin

from .models import Subject, Student

class CInline(admin.TabularInline):
    model = Student
    extra = 10

class QAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['semester_text']}),
        (None,               {'fields': ['subject_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [CInline]
    list_display = ('subject_text', 'pub_date')

admin.site.register(Subject, QAdmin)
