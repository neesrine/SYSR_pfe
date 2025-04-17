from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Wilaya
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import (
    CandidatSerializer,
    LangueSerializer,
    DomaineSerializer,
    SpecialiteSerializer,
    CompetenceSerializer,
    FormationSerializer,
    ExperienceSerializer,
    OffreSerializer,
    CandidatureSerializer,
)
from django.http import HttpResponse
from django.shortcuts import render 
def home(request):
    return render(request,'djezzy_app/home.html')

class CandidatViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    permission_classes = [IsAuthenticated]

class LangueViewSet(viewsets.ModelViewSet):
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer
    permission_classes = [IsAuthenticated]

class DomaineViewSet(viewsets.ModelViewSet):
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer
    permission_classes = [IsAuthenticated]

class SpecialiteViewSet(viewsets.ModelViewSet):
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    permission_classes = [IsAuthenticated]

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    permission_classes = [AllowAny]  # Permet l'accès à tous
    serializer_class = CompetenceSerializer

class FormationViewSet(viewsets.ModelViewSet):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    permission_classes = [IsAuthenticated]

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    from rest_framework import viewsets
    
from .models import Wilaya
from .serializers import WilayaSerializer

class WilayaViewSet(viewsets.ModelViewSet):
    queryset = Wilaya.objects.all()
    serializer_class = WilayaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OffreViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get']) 
    def candidats(self, request, pk=None):
        offre = self.get_object()
        candidatures = Candidature.objects.filter(offre=offre)
        serializer = CandidatureSerializer(candidatures, many=True)
        return Response(serializer.data)

class CandidatureViewSet(viewsets.ModelViewSet):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def changer_statut(self, request, pk=None):
        candidature = self.get_object()
        statut = request.data.get('statut')

        if statut not in ['en_attente', 'accepte', 'refuse']:
            return Response({'detail': 'Statut invalide'}, status=status.HTTP_400_BAD_REQUEST)

        candidature.statut = statut
        candidature.save()
        return Response({'detail': 'Statut de la candidature mis à jour'}, status=status.HTTP_200_OK)
