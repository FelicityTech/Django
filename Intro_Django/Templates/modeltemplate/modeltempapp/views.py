from django.shortcuts import render
from .models import Menu
# Create your views here.
# def menu(request):
#     newmenu = {'pricechart': [
#         {'name':'falafel', 'price': '12'},
#         {'name': 'shawarma', 'price': '15'},
#         {'name': 'gyro', 'price': "10"},
#         {'name': "hummus", 'price':'5'},
#     ]}
#     return render(request, 'menu.html', newmenu)


def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)