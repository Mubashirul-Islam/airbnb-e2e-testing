from django.contrib import admin

from testing.models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("test_id", "test_case", "passed", "url", "comment")
    list_filter = ("test_id", "passed")
    search_fields = ("test_id", "test_case", "comment")
    ordering = ("test_id", "passed")
