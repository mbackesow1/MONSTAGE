from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  *

urlpatterns = [
    path("index/idpro=<int:idpro>/",index, name="indexurl"),
    path("",  lstpro, name="indexurlpro"),

    path("login", loginin , name="connecterurnjjl"),
    path("indexentre", indexentre , name="connecterurlgh"),
path("listcre/nom=<str:nom>", listecredit , name="connecterurlgghhhjh"),
path("listenoti/nom=<str:nom>", listenotific , name="connecterurrfflgghhhjh"),
path("listcre/voircpt/idclt=<int:idclt>", voircpt , name="connecterurrfflgghhhjh"),
#path("ajoucom/<str:lstcom>", voircpt , name="connecterurrfflgghhhjh"),



    path("bienvent", loginentre, name="connecterurl"),
    #path("",  product_list, name="productlist"),
    #path('', include('product_app.urls')),
    path("crercompte/", creationUser, name="crerurl"),
    path("traitecompte",  traitercompte, name="crercompteurl"),
    path('updateuu/idu=<int:idu>', update_user , name="updateu"),
    path('ajouter', ajouter, name="updateu"),
    #path('traiteupdate', trateupdate, name="updateutrou"),
    path('updateuu/traiteupdate', trateupdate, name="updateutr"),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # ...

]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)