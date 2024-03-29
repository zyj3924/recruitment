from django.contrib import admin
from jobs.models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_type', 'job_city', 'create_date', 'modified_date', 'creator')
    exclude = ('create_date', 'modified_date', 'creator')
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Job, JobAdmin)