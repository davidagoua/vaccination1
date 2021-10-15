from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.contrib.auth.models import UserManager


class UserRole(Enum):
    ADMIN: str = "admin"
    CHEFCENTRE: str = "Chef de centre"
    ENREGISTREUR: str = "Agent enregitreur"
    OBSERVATEUR: str = "Agent observateur"
    MEDECIN: str = "Medecin"
    PATIENT: str = "Patient"


#Manager
class MedecinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.MEDECIN)


class ChefcentreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.CHEFCENTRE)


class EnregistreurManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.ENREGISTREUR)


class ObservateurManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.OBSERVATEUR)


class PatientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.PATIENT)


class Location(models.Model):
    emplacement = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


class District(Location, models.Model):
    region = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)

    def __str__(self): return f"{self.nom} ({self.region})"


class Centre(Location, models.Model):
    nom = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, choices=[
        ('Hopital','Hopital'),
        ('Equipe mobile','Equipe mobile'),
        ('District sanitaire','District sanitaire')
    ])

    def __str__(self): return f"{self.nom} ({self.district.nom})"


class User(AbstractUser):
    role = models.CharField(max_length=100,
                    choices=[(role.name, role.value) for role in list(UserRole)]
                )
    contact = models.CharField(max_length=100)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    place_birth = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    fonction = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()
    medecins = MedecinManager()
    observateurs = ObservateurManager()
    chefcentres = ChefcentreManager()
    enregistreurs = EnregistreurManager()
    patients = PatientManager()


def setup_users(centre: Centre, user_per_role: dict, password: str = '12345'):
    """
    Generer des utilisateurs
    :param centre:
    :param user_per_role:
    :param password:
    :return:
    """
    for key, value in user_per_role.items():
        for i in range(value):
            # create medecin
            uid = f'{ str(key.name).lower() }{centre.id}_{i+1}'
            user = User(
                email=f'{uid}@gmail.com',
                username=uid,
                role=key.name,
                centre_id=centre.pk,
                contact='0'
            )
            user.set_password(password)
            user.save()


@receiver(models.signals.post_save, sender=Centre)
def on_centre_created(sender, instance, created, **kwargs):
    """
    Setup agents each time center is created
    :param sender:
    :param instance:
    :param created:
    :return:
    """
    if created:
        setup_users(instance, {
         UserRole.MEDECIN: 1,
         UserRole.OBSERVATEUR: 1,
         UserRole.CHEFCENTRE: 1,
         UserRole.ENREGISTREUR: 3
        })