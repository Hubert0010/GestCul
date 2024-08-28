from django.shortcuts import redirect,render
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from  .models import membres


# Create your views here.
def list_membres(request):
    membr = membres.objects.all()
    print(membr)
    #pour eviter les surcharge on utilise Paginator pour limiter le nombre de donnee a afficher sur la page
    paginator = Paginator(membr,10)
    page_number = request.GET.get('page')
    membr = paginator.get_page(page_number)
    #print(membres)
    return render(request, 'membres.html', {'membres':membr})

def form_membres(request):
    return render(request,'FormMembres.html')

def add_membre(request):
    if request.method == 'POST':
        try:
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            mot_de_passe = request.POST.get('mot_de_passe')#apres quqnd tu aura le tps renome ;ot_de_pass en password pour eciter des erreur a la saisie a l'avenir
            adresse = request.POST.get('adresse')
            telephone = request.POST.get('telephone')

            # Vérifie que les données sont présentes
            if not all([nom, email, mot_de_passe, adresse, telephone]):
                raise ValidationError("Tous les champs doivent être remplis.")

            hashed_password = make_password(mot_de_passe)

            # Crée et enregistre un nouvel objet membre
            membres = membres(
                nom=nom,
                email=email,
                mot_de_passe=hashed_password,
                adresse=adresse,
                telephone=telephone
)
            membres.save()

            return redirect('list_membres')
        except Exception as e:
            # Gère les erreurs en affichant un message ou en enregistrant l'erreur
            return render(request, 'FormMembres.html', {'error': str(e)})
    return render(request, 'FormMembres.html')