from django.contrib import admin
from jobsapp.models import Job, Favorite, Applicant


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "salary",
        "location",
        "type",
        "category",
        "company_name",
        "last_date",
        "created_at",
        "filled",
        "user",
    ]
    list_filter = ["salary", "last_date", "created_at", "user"]
    date_hierarchy = "created_at"
admin.site.register(Favorite)
admin.site.register(Applicant)