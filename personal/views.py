from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/index.html')

def contact(request):
    content_dict = {'content': ['Email me at:','joe@protonmail.com']}
    return render(request, 'personal/contact.html', context=content_dict)
