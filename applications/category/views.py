from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import Category
from .serializers import CategorySerializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()