from django.db import models


class Park(models.Model):
    name = models.TextField()
    url = models.URLField()
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)
    image  = models.TextField(blank=True)

    @property
    def small_image(self):
        parts = self.image.rsplit('/', 1)
        if len(parts) >= 2:
            return parts[0] + "/small_" + parts[1]
        else:
            return self.image
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "facilities"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    park = models.ForeignKey(
        Park, related_name="feedback_park", on_delete=models.CASCADE
    )
    facility = models.ForeignKey(
        Facility, related_name="feedback_facility", on_delete=models.CASCADE
    )

    facility = models.CharField(max_length=255)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "feedback"


class Photo(models.Model):
    feedback = models.ForeignKey(
        Feedback, related_name="photo_feedback", on_delete=models.CASCADE
    )
    file_url = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="photos/")

    @property
    def url(self):
        if self.file_url:
            return self.file_url
        if self.file:
            return self.file.url
        return None
