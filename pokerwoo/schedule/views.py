from rest_framework import viewsets, permissions
from schedule.models import Session, SessionPlayer
from schedule.serializers import SessionSerializer, SessionPlayerSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SessionPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = SessionPlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SessionPlayer.objects.filter(session=self.kwargs['session_pk'])

    def perform_create(self, serializer):
        serializer.save(session=Session.objects.get(pk=self.kwargs['session_pk']))