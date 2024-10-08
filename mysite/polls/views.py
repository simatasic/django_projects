from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Sima. You're at the polls index.")
