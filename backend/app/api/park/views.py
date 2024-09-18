import uuid

from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app.park.models import Facility, Feedback, Park, Photo

from .serializers import FeedbackSerializer, ParkDetailSerializer, ParkSerializer


class ParkViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    """
    Handles listing and retrieving park data
    """

    queryset = Park.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ParkDetailSerializer
        return ParkSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()

        # Prefetch related feedback and facilities in a single query
        obj = Park.objects.prefetch_related(
            "feedback_park",
        ).get(pk=obj.pk)

        feedback = obj.feedback_park.all()

        obj.feedback = feedback

        # Serialize the object
        serializer = self.get_serializer(obj)

        return Response(serializer.data, status=status.HTTP_200_OK)


class FeedbackViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    """
    Handles creating feedback and photos
    """

    serializer_class = FeedbackSerializer
    queryset = Park.objects.all()

    def create(self, request, *args, **kwargs):
        facility = Facility.objects.get_or_create(name=request.data.get("facility"))
        request.data["facility"] = facility[0].id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Save photos and link to Feedback
        for photo in request.FILES.getlist("photos"):
            # Generate a random filename
            photo.name = f"{uuid.uuid4()}.{photo.name.split('.')[-1]}"

            Photo.objects.create(feedback_id=serializer.data["id"], file=photo)

        # Refetch the Feedback object
        feedback = Feedback.objects.get(id=serializer.data["id"])
        response_serializer = self.get_serializer(feedback)

        headers = self.get_success_headers(response_serializer.data)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
