import datetime
import random

from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum
from usermanager.models import Centre

User = get_user_model()


class PatientState(Enum):
    ENREGISTRE: str = "Enregistré"
    OBSERVATION: str = "En observation"
    REJETE: str = "Rejeté"
    FINALISE: str = "Finalisé"


class Patient(models.Model):

    SEXE_CHOICE = [
        ('M', 'Homme'),
        ('F', 'Femme')
    ]

    code = models.CharField(max_length=15,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    state = models.CharField(max_length=100,
                            choices=[(state.name, state.value) for state in list(PatientState)]
                            )
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patient_adds')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commune = models.CharField(max_length=100, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    sexe = models.CharField(max_length=100, choices=SEXE_CHOICE)
    photo = models.ImageField(upload_to='image_patients/', null=True, blank=True)
    place_birth = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    enfants = models.IntegerField(choices=[(n,n) for n in range(10) ])
    matrimoniale = models.CharField(max_length=100, choices=[('Marie','Marie'),('Celibataire','Celibataire'),('En couple','En_couple')])

    def save(self, **kwargs):
        self.code = random.randrange(0,9999999999, 1000)
        return super(Patient, self).save(**kwargs)


class Vaccin(models.Model):
    nom = models.CharField(max_length=100)
    nlot = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, blank=True)
    quantite = models.PositiveIntegerField(default=0)
    actif = models.BooleanField(default=True)
    exp = models.DateField(verbose_name="Date d'expirartion")
    created_at = models.DateTimeField(auto_now_add=True)


class Vaccination(models.Model):
    vaccin = models.ForeignKey(Vaccin, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="")


class TestSero(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    datetest = models.DateField()
    igg = models.IntegerField()
    igm = models.IntegerField()
    laboratoire = models.CharField(max_length=150)
    dateajout = models.DateField()
    fichier = models.FileField(upload_to='testsero/', null=True, blank=True)


class Enquete(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    poids = models.FloatField()
    taille = models.FloatField()
    created_at = models.DateTimeField()
    temp = models.FloatField(verbose_name="Temperature")
    positifcov = models.BooleanField(default=False)
    datepositive = models.DateField(null=True, blank=True)
    testsero = models.ForeignKey(TestSero, null=True, blank=True, on_delete=models.SET_NULL)
    maladies = models.TextField(default="", blank=True)
    vaccine = models.BooleanField(default=False)
    signeclinique = models.TextField(default="")

