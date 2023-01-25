from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle  made from combination of wheat, water or eggs',
        'falafel': 'Falafel are deep fried patties or balls made fr...',
        'cheesecake': 'Cheesecake is a type of dessert made with cr...'
    }
    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)