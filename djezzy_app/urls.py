from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'candidats', CandidatViewSet)
router.register(r'langues', LangueViewSet)
router.register(r'domaines', DomaineViewSet)
router.register(r'specialites', SpecialiteViewSet)
router.register(r'wilayas', WilayaViewSet, basename='wilaya')

router.register(r'competences', CompetenceViewSet)
router.register(r'formations', FormationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'offres', OffreViewSet)  # Ajout de la route pour les offres
router.register(r'candidatures', CandidatureViewSet)
urlpatterns = [
    path('', include(router.urls)),  #  Corrigé : plus de 'api/' ici
]