
from django.db import models

class Park(models.Model):
    name = models.TextField()
    url = models.URLField()
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '%s: %s' % (self.key, self.name)

class SubArea(models.Model):
    name = models.TextField()
    park = models.ForeignKey(Park, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '%s: %s' % (self.key, self.name)
    
class FacilityCategory(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '%s: %s' % (self.key, self.name)

class Facility(models.Model):
    name = models.TextField()
    facility_category = models.ForeignKey(FacilityCategory, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('name', )

    def __str__(self):
        return '%s: %s' % (self.key, self.name)

class Feedback(models.Model):
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    file = models.TextField()
