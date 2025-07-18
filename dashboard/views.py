from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UserDashboard
from .serializers import UserDashboardSerializer

class UserDashboardViewSet(viewsets.ModelViewSet):
    queryset = UserDashboard.objects.all()
    serializer_class = UserDashboardSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def share(self, request, pk=None):
        dashboard = self.get_object()
        # 分享邏輯 (可加發信或權限設定)
        return Response({'status': f'Dashboard "{dashboard.title}" shared.'})

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
