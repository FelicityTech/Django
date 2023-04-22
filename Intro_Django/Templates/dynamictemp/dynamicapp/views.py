from django.shortcuts import render

# Create your views here.
def menu(request):
    # menuitem = {'name': 'Greek Salad'}
    newmenu = {'mains': [
        {'name':"falafel", 'price': "12"},
        {'name': "shawarma", 'price': '15'},
        {'name':'gyro', 'price': '10'},
        {'name':'hummus', 'price':'5'},
    ]}
    return render(request, 'menu.html', newmenu)
