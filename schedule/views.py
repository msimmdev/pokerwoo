from rest_framework import viewsets, permissions, views, response, status
from schedule.models import Session, SessionPlayer
from schedule.serializers import SessionSerializer, SessionPlayerSerializer
from datetime import date

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

class NextSession(views.APIView):
    def get(self, request):
        sessions = Session.objects.filter(schedule_date__gte=date.today().strftime("%Y-%m-%d 00:00:00")).order_by('schedule_date')
        if len(sessions) > 0:
            serializer = SessionSerializer(sessions[0], context={'request': request})
            return response.Response(serializer.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)