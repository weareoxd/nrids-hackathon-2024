from django.core.management.base import BaseCommand

from app.park.models import Facility, Feature, Feedback
from app.park.utils import get_feedback_features


class Command(BaseCommand):
    help = "Add features to the parks"

    def handle(self, *args, **options):
        feedbacks = Feedback.objects.all()

        for feedback in feedbacks:
            facility, created = Facility.objects.get_or_create(
                name=feedback.facility.name, park=feedback.park
            )

            comments = feedback.comments
            feature_names = get_feedback_features(comments)
            features = Feature.objects.filter(name__in=feature_names)
            for feature in features:
                facility.features.add(feature)
