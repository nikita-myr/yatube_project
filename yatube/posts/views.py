from django.http import HttpResponse

def index(request):
    return HttpResponse('THE HOME PAGE WILL BE HERE SOON')

def group_posts(request, slug):
    return HttpResponse('AND HERE WILL BE USERS POSTS')