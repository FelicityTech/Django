from django.shortcuts import render

# Create your views here.

def about(request):
    about_content = {'about': "Based in Atlanta, chicago, Illinois, Little lemon is a family owned Mediterrancean"}
    return render(request, "about.html", about_content)