from django.contrib import admin
from .models import *

# Enregistrement simple
admin.site.register(Admin)
admin.site.register(Candidat)
admin.site.register(Offre)
admin.site.register(Candidature)
admin.site.register(Competence)
admin.site.register(Domaine)
admin.site.register(Specialite)
admin.site.register(Langue)
admin.site.register(Formation)
admin.site.register(Experience)

