from django.contrib import admin

from .models import Facility, Feedback, Park, Photo


@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "latitude",
        "longitude",
        "image",
    )
    ordering = ("name",)
    search_fields = ["name"]


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ["name"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "park",
        "facility",
        "comments",
        "created_at",
    )
    ordering = ("park", "facility")
    search_fields = ["park", "facility", "comments"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "feedback",
        "url",
    )
    ordering = ("feedback",)
