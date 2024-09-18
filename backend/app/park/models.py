from django.db import models


class Park(models.Model):
    name = models.TextField()
    url = models.URLField()
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class SubArea(models.Model):
    name = models.TextField()
    park = models.ForeignKey(
        Park, related_name="subarea_park", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class FacilityCategory(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "facility categories"

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.TextField()
    facility_category = models.ForeignKey(
        FacilityCategory,
        related_name="facility_facilitycategory",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "facilities"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    sub_area = models.ForeignKey(
        SubArea, related_name="feedback_subarea", on_delete=models.CASCADE
    )
    facility = models.ForeignKey(
        Facility, related_name="feedback_facility", on_delete=models.CASCADE
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "feedback"


class Photo(models.Model):
    feedback = models.ForeignKey(
        Feedback, related_name="photo_feedback", on_delete=models.CASCADE
    )
    file = models.TextField()
