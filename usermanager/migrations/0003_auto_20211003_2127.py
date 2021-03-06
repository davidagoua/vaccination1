# Generated by Django 3.2.7 on 2021-10-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0002_auto_20211002_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre',
            name='emplacement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='emplacement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('CHEFCENTRE', 'Chef de centre'), ('ENREGISTREUR', 'Agent enregitreur'), ('OBSERVATEUR', 'Agent observateur'), ('MEDECIN', 'Medecin'), ('PATIENT', 'Patient')], max_length=100),
        ),
    ]
