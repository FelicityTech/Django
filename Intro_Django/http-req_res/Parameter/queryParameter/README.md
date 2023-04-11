# Query parameter

** http://localhost:8000/getuser/?name=John&id=1 **

A query string is a sequence of one or more --key=value-- pairs concatenated by the --&-- symbol. Each key is the query parameter. The query string ends with the --?-- symbol after the URL endpoint.

### Query strings are an alternative approach to URL parameters for adding URL configurations.

The URL dispatcher doesn’t parse these parameters. They are fetched by the view from the request object it receives. The request object’s --GET-- property is a dictionary object. 

The key-value pairs in the query string are added to the --request.GET-- property. Hence, the name can be obtained with --request.GET[‘name’]-- expression.

The next step is to add the following path in the --urls.py-- file:
```
path('getuser/', views.qryview, name='qryview') 
```

Declare the --qryview-- function in the --views.py-- file

```
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

```

## Now, start the server and use http://localhost:8000/myapp/?name=John&id=1 as the URL

![queryParameter](/queryParameter/img/TSdtjBW1QoO_StIoAkx34A_64e09bd3d2d5409ba2b622b5af75bbe1_C5M2L2_Itm05_1.png)
