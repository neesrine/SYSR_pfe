from django.db import models

# Modèle Admin
class Admin(models.Model):
    nom_admin = models.CharField(max_length=100)
    email_admin = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    class Meta:
        app_label = 'djezzy_app'



class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100)
    description = models.TextField()
    wilaya = models.ForeignKey('Wilaya', on_delete=models.SET_NULL, null=True)
    langues = models.ManyToManyField('Langue')
    competences = models.ManyToManyField('Competence')

    specialite = models.ManyToManyField('Specialite')

class Wilaya(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Modèle Compétence
class Competence(models.Model):
    nom = models.CharField(max_length=100)
    

# Modèle Domaine
class Domaine(models.Model):
    nom = models.CharField(max_length=100)


# Modèle Specialité
class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name="specialites")


# Modèle Langue
class Langue(models.Model):
    nom = models.CharField(max_length=50)


# Modèle Offre d'emploi
class Offre(models.Model):
    id_offre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    exigences = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE, related_name='offres')


# Modèle Candidature
class Candidature(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE)
    offre = models.ForeignKey('Offre', on_delete=models.CASCADE)
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE)
    date_postulation = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')


# Modèle Formation
class Formation(models.Model):
    titre = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    niveau = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE, related_name="formations")


# Modèle Expérience
class Experience(models.Model):
    entreprise = models.CharField(max_length=200)
    poste = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE, related_name="experiences")

