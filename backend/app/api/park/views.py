import uuid

from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from app.park.models import Facility, Feature, Feedback, Park, Photo
from app.park.utils import get_feedback_features, get_query_features

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

        feedback = obj.feedback_park.all().order_by("-id")

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
        park_id = request.data.get("park")
        facility, created = Facility.objects.get_or_create(
            name=request.data.get("facility"), park_id=park_id
        )

        # add features
        comments = request.data.get("comments")
        feature_names = get_feedback_features(comments)
        features = Feature.objects.filter(name__in=feature_names)
        for feature in features:
            facility.features.add(feature)

        feedback = Feedback.objects.create(
            park_id=park_id,
            facility=facility,
            comments=request.data.get("comments"),
        )

        # Save photos and link to Feedback
        for photo in request.FILES.getlist("photos"):
            # Generate a random filename
            photo.name = f"{uuid.uuid4()}.{photo.name.split('.')[-1]}"

            Photo.objects.create(feedback_id=feedback.id, file=photo)

        # Refetch the Feedback object
        response_serializer = self.get_serializer(feedback)

        headers = self.get_success_headers(response_serializer.data)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get("q")
        if not query:
            return Response(
                {"error": "Missing query parameter"}, status=status.HTTP_400_BAD_REQUEST
            )

        feature_names = get_query_features(query)

        features = Feature.objects.filter(name__in=feature_names)

        if features.exists():
            parks = Park.objects.filter(facilities__features__in=features).distinct()
        else:
            parks = Park.objects.none()

        serialized_parks = []
        for park in parks:
            park_features = set(
                park.facilities.values_list("features__name", flat=True)
            )
            matched_features = list(park_features.intersection(feature_names))

            park_data = ParkSerializer(park).data
            park_data["tags"] = matched_features

            serialized_parks.append(park_data)

        return Response(serialized_parks, status=status.HTTP_200_OK)
