from rest_framework import serializers

from app.park.models import Feedback, Park


class FeedbackSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Feedback
        fields = (
            "id",
            "park",
            "facility",
            "comments",
            "photos",
        )

    def get_photos(self, obj):
        photos = obj.photo_feedback.all()
        return [
            photo.file_url if photo.file_url else photo.file.url for photo in photos
        ]


class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = (
            "id",
            "name",
            "url",
            "latitude",
            "longitude",
            "image",
            "small_image"
        )


class ParkDetailSerializer(ParkSerializer):
    feedback = serializers.SerializerMethodField()

    class Meta:
        model = Park
        fields = (
            "id",
            "name",
            "url",
            "latitude",
            "longitude",
            "image",
            "small_image",
            "feedback",
        )

    def get_feedback(self, obj):
        return FeedbackSerializer(obj.feedback, many=True).data
