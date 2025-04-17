from rest_framework import serializers
from .models import *

class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = '__all__'

class LangueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langue
        fields = '__all__'

class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = '__all__'

class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = '__all__'

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'


class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = '__all__'
