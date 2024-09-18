from django.contrib import admin

from .models import Facility, FacilityCategory, Feedback, Park, Photo, SubArea


@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "latitude",
        "longitude",
    )
    ordering = ("name",)
    search_fields = ["name"]


@admin.register(SubArea)
class SubAreaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "park",
    )
    ordering = ("name",)
    search_fields = ["name", "park"]


@admin.register(FacilityCategory)
class FacilityCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    search_fields = ["name"]


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "facility_category",
    )
    ordering = ("name",)
    search_fields = ["name", "facility_category"]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "sub_area",
        "facility",
        "description",
        "created_at",
    )
    ordering = ("sub_area",)
    search_fields = ["sub_area", "facility", "description"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "feedback",
        "file",
    )
    ordering = ("feedback",)
