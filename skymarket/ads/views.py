from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdDetailSerializer
    serializers = {"list": AdSerializer}
    pagination_class = AdPagination
    default_permission = [IsAuthenticated]
    permissions = {
        "list": [AllowAny, ],
        "retrieve": [IsAuthenticated, ],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    @action(detail=False, url_path="me", serializer_class=AdSerializer)
    def me(self, request):
        ads = Ad.objects.filter(author_id=request.user.pk)
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination
    default_permission = [IsAuthenticated]
    permissions = {
        "list": [IsAuthenticated, ],
        "retrieve": [IsAuthenticated, ],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
