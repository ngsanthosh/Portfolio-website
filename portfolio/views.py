from django.shortcuts import render

# Create your views here.
def index(request):
    context={

    }
    return render(request, 'index.html', context)

def projects(request):
    context={

    }
    return render(request, 'projects.html', context)

def languages(request):
    context={

    }
    return render(request, 'languages.html', context)