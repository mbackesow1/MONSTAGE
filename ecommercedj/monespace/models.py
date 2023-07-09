from django.db import models

from django.db import models

from django.db import models


class Users(models.Model):
    entreprise1 = "ccbm"
    entreprise2 = "orbit"
    ROLE_CHOICES = (
        (entreprise1, 'ccbm'),
        (entreprise2, 'orbit'),
    )

    idu = models.BigAutoField(primary_key=True)
    nompreu = models.CharField(max_length=100, null=True, verbose_name="Votre  Nom")
    emailu = models.EmailField(null=True, verbose_name=" Votre Email", unique=True)
    teleu = models.CharField(max_length=15, null=True, verbose_name="Votre Télephone")
    mdpu = models.CharField(max_length=128, null=True, verbose_name="Votre  Mot de Passse")
    # entreu = models.CharField(max_length=128,null=True)
    entreprise = models.CharField(max_length=30, choices=ROLE_CHOICES)
    postu = models.CharField(max_length=128, null=True, verbose_name="Poste")
    sectu = models.CharField(max_length=128, null=True, verbose_name="Secteur")
    adresseu = models.CharField(max_length=15, null=True, verbose_name="Votre Adresse")
    dateinsu = models.DateTimeField("date creation", null=True, auto_now_add=True)
    # image = models.CharField(max_length=128, null=True)
    image = models.FileField(upload_to='photos', verbose_name="Profil")

    class Meta:
        db_table = "orbituser"

    # Create your models here.
    def __str__(self):
        return str(self.dateinsu)




class Entreprise(models.Model):
    ident = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    mdpent = models.CharField(max_length=255)
    class Meta:
        db_table = "orbitentreprise"

    def __str__(self):
        return self.nom




class DmdCredit(models.Model):
    iddmd = models.AutoField(primary_key=True)
    idclt = models.IntegerField(default=1)
    nomclt = models.CharField(max_length=255,null=True)
    noment = models.CharField(max_length=255 , null=True)
    status = models.IntegerField(default=0)
    idpro = models.IntegerField()

    class Meta:
        db_table = 'dmdcredit'


class Product(models.Model):
    idpro = models.AutoField(primary_key=True)
    mimage = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Product {self.idpro}: {self.description}"
    class Meta:
        db_table = 'product'



class Commande(models.Model):
    idcom = models.AutoField(primary_key=True)
    idlct = models.IntegerField(null=False)
    idpro = models.IntegerField(null=False)
    action = models.CharField(max_length=100, default='direct')
    class Meta:
        db_table = 'commande'







