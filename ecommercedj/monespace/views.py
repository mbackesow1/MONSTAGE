from datetime import datetime

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .formusers import UsersForm, FormLogin, Formodifie
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Users, Entreprise, DmdCredit, Product, Commande, DétailsCommande, Precommande, Compte


#from .models import Product
#from ..ecommercedj.settings import DEFAULT_FROM_EMAIL
#from  ..ecommercedj.settings import DEFAULT_FROM_EMAIL
def index(request , idpro):
    idpro = idpro
    formi = FormLogin()
    return render(request, 'index.html', {'form': formi, 'idpro':idpro})
def creationUser(request):
    form = UsersForm()

    return render(request, 'crercompte.html', {'form': form})

#Creer  utilisateur
def  traitercompte(request):
    if request.method == "POST":
        #form = EmployeeForm(request.POST , request.FILES)
        form= UsersForm(request.POST , request.FILES)
        if form.is_valid() :

            #try:
                form.save()
                formi = FormLogin()
                #return render(request, 'index.html', {'form': formi})
                return  redirect("/monespace")
    else:
        form = UsersForm()
    return render(request,'crercompte.html',{'form':form})
def connecterUser(request, id):
    userbn = Users.objects.get(emailu=id)
    return render(request, 'bienvenue.html', {'userbn': userbn})
def loginin(request):
    if request.method == 'POST':
        email = request.POST['emailu']
        password = request.POST['mdpu']
        idpro=request.POST['idpro']
        try:
            user = Users.objects.get(emailu=email, mdpu=password)
            pro=Product.objects.get(idpro=idpro)
            return render(request, 'ajouter.html', {'userlog':user, 'products': pro})
            userlog=user
        except Users.DoesNotExist:
            # L'utilisateur n'existe pas
            error_message = 'Cet email n\'est pas enregistré.'
            return render(request, 'index.html', {'error_message': error_message})
        error_message = 'Mot de passe incorrect. Veuillez réessayer.'
        formi = FormLogin()
    return render(request, 'index.html', {'form': formi},{'error_message': error_message})

### Modification de  profil
def update_user(request, idu):
    userup= Users.objects.get(idu=idu)
    #delattr(userup, 'image')
    formuserup= Formodifie(instance=userup)
    #formuserup= Formodifie()
    return render(request, 'updatepro.html', {'userup': formuserup})
def trateupdate(request):
    userup=Users.objects.get(emailu=request.POST['emailu'])
    if request.method == 'POST':
        emailu= request.POST['emailu']
        nompreu = request.POST['nompreu']
        mdpu = request.POST['mdpu']
        adresseu= request.POST['adresseu']
        entreprise = request.POST['entreprise']
        sectu = request.POST['sectu']
        postu= request.POST['postu']
        #image=request.POST['image']
        # Cganger
        userup.emailu=emailu
        userup.nompreu = nompreu
        userup.mdpu = mdpu
        userup.entreprise = entreprise
        userup.adresseu = adresseu
        userup.sectu = sectu
        userup.postu=postu = emailu
        #userup.image=image
        #sauvegarder
        userup.save()
        return render(request, 'bienvenue.html', {'userlog': userup})

    else:
        form = UsersForm(instance=userup)
        return render(request, 'updatepro.html', {'userup': form})
## Traitemnt mdpoub
def mdpu(request):
    if request.method == 'POST':

        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save(
                request=request,
                from_email=DEFAULT_FROM_EMAIL,
                email_template_name='mdpoub.html',
                subject_template_name='mdpoubsubject.txt',
            )
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()

    return render(request, 'mdpoub.html', {'form': form})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products':1})
def lstpro(request):
    products = [
        {
            "idpro": 1,
            "mimage": "image1.jpg",
            "price": 10.99,
            "description": "Description du produit 1"
        },
        {
            "idpro": 2,
            "mimage": "image2.jpg",
            "price": 19.99,
            "description": "Description du produit 2"
        },
        {
            "idpro": 3,
            "mimage": "image3.jpg",
            "price": 5.99,
            "description": "Description du produit 3"
        }
    ]
    return  render(request, 'product_list.html', {'products': products})
##traitement du panier
def ajouter(request):
    for product in products:
        # Vérifier si l'ID du produit correspond à l'ID recherché
        if product['idpro'] == request.Post['idpro']:
            # Si l'ID correspond, vous pouvez accéder à l'élément ici
            #print(product)
            product_details = product
            return render(request, 'ajouter.html', {'products':product_details})
            #break  # Sortir de la boucle une fois que l'élément est trouvé





#####Gestion entreprise
def indexentre(request):
   # idpro = idpro
    #formi = FormLogin()
    #return render(request, 'index.html', {'form': formi, 'idpro':idpro})
    return render(request, 'indexentre.html')
def loginentre(request):
    if request.method == 'POST':
        noment = request.POST['noment']
        password = request.POST['mdpent']
        try:
            ent= Entreprise.objects.get(nom=noment, mdpent=password)

            return render(request, 'bienvenueentre.html', {'ent':ent})
            userlog=user
        except Users.DoesNotExist:
            # L'utilisateur n'existe pas
            error_message = 'Cet email n\'est pas enregistré.'
            return redirect("indexent ")
            #return render(request, 'index.html', {'error_message': error_message})
        error_message = 'Mot de passe incorrect. Veuillez réessayer.'
        #formi = FormLogin()
    return redirect("indexent ")
def listecredit(request , nom) :
    #lst=DmdCredit.objects.get(noment=nom, status=1)
    lst = DmdCredit.objects.filter(noment=nom, status=1)
    #usercre = Users.objects.filter(idu=lst.values('idclt'))
    #usercre = Users.objects.get(idu=lst.idclt)
    return  render(request,'listecredit.html' , {'usercre':lst, 'noment':nom})

def listenotific(request, nom):
        # lst=DmdCredit.objects.get(noment=nom, status=1)
        lst = DmdCredit.objects.filter(noment=nom, status=0)
        # usercre = Users.objects.filter(idu=lst.values('idclt'))
        # usercre = Users.objects.get(idu=lst.idclt)
        return render(request, 'listenoti.html', {'usercre': lst, 'noment': nom})
def voircpt(request , idclt) :
    userup = Users.objects.get(idu=idclt)
    return render(request, 'voircpt.html', {'usercpt': userup})



    #return render(request, 'index.html', {'form': formi},{'error_message': error_message})
def ajoucom_view(request, lstcom):
        # Divisez la chaîne de caractères en une liste d'éléments
        ma_liste = lstcom.split(',')
        # Créez un nouvel objet Commande en utilisant les éléments de la liste
        nouvelle_commande = Commande(idlct=ma_liste[0], idpro=ma_liste[1], action=ma_liste[2])
        # Sauvegardez l'objet Commande dans la base de données
        nouvelle_commande.save()
        return  redirect("")


def commande(request, idpro, idclt) :
    return  render(request, "formqt.html",{"idpro":idpro , "idclt":idclt})
def precommande(request, idpro, idclt) :
    return  render(request, "formnbrjour.html",{"idpro":idpro , "idclt":idclt})

def traitecommande(request) :
    idpro = request.POST['idpro']
    idclt = request.POST['idclt']
    qt=request.POST['qt']
    pro= Product.objects.get(idpro=idpro)
    usercmd=Users.objects.get(idu=idclt)
    #com=Commande()
    commande = Commande(date=datetime.now(), etat=0, total= int(pro.price)  * qt, vandor="v9096", idclt=idclt , idpro=idpro, action="direct")
    commande.save()
    details_commande = DétailsCommande.objects.create(
        commande=commande,
        idpro=idpro,
        quantite=qt,
        prix_unitaire=pro.price
    )
    details_commande.save()


    #com.idclt=idclt
    #com.action="direct"
    #com.idpro=idpro
    #com.total= int(pro.price ) * qt
    #com.save()
    #comsauv=com.objects.latest('idcom')
    #deta=DétailsCommande()
    ##deta.idpro=idpro
    #deta.quantite=qt
    #deta.prix_unitaire=pro.price
    #deta.commande=comsauv.idcom
    #deta.save()
    lst= Commande.objects.filter(idclt=idclt)
    return   render(request , "affichecomm.html" , {"deta" : details_commande , "com": commande , "usercmd":usercmd , "lst":lst})
def voirdlt( request  ,  idcom) :
   det=DétailsCommande.objects.get(commande_id =4)
   com=Commande.objects.get(idcom =det.commande_id)
   user=Users.objects.get(idu=com.idclt)
   pro=Product.objects.get(idpro=com.idpro)
   return  render(request, "detailcom.html" , {"detcom":det, "com":com,"pro":pro,"user":user})
def traiteprecommande(request) :
    idpro = request.POST['idpro']
    idclt = request.POST['idclt']
    nbrj=request.POST['nbrj']
    pro= Product.objects.get(idpro=idpro)
    usercmd=Users.objects.get(idu=idclt)
    lst = Commande.objects.filter(idclt=idclt)
    precom=Precommande( idpro =idpro,idclt = idclt  , nbrjour = nbrj ,prix=pro.price, description=pro.description)
    precom.save()
    lstpre= Precommande.objects.filter(idclt=idclt)
    return render(request, "afficheprecomm.html", {"com": commande, "usercmd": usercmd, "lstpre": lstpre})
def voircompte(request , idu) :
    ucom=Users.objects.get(idu=idu)
    cpt=Compte.objects.get(idclt=idu)
    return  render(request, "affichecompte.html",{"ucom":ucom, "cpt":cpt})


























