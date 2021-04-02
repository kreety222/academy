from django.shortcuts import render

# Create your views here.
def style(request):
    context = {'style': 'active'}
    return render(request, 'styles/style.html', context)
