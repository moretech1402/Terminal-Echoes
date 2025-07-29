from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hello from my first Django application: main_app!")