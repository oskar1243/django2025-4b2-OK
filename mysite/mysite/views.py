from django.http import HttpResponse




def landing_page(request):
    
    return HttpResponse("you are on the landing page")
