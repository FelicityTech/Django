# Path Parameter
** URL http://localhost:8000/getuser/John/1 **

The URL dispatcher should identify John as the name parameter and 1 as the id parameter. 

This pattern is mapped to the --pathview()-- function with the following path in the URL patterns list in the app’s --url.py-- file.

```
path('getuser/<name>/<id>', views.pathview, name='pathview'), 
```

Next, add the --pathview()-- function in --views.py-- file.

```
from django.http import HttpResponse 
def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
```