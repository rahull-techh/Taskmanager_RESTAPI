from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to the Task Manager API!")