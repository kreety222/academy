from django.shortcuts import render

# Create your views here.
def about(request):
    context = {'about' : 'active'}
    return render(request, 'core/about.html', context)
