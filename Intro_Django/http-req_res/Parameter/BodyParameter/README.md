# Body parameters

Let’s construct a simple form containing two text input elements. Then, save it as --form.html-- in the --templates-- folder.

```
<form action="/myapp/getform/" method="POST>
    {% csrf_token %} 
    <p>Name: <input type="text" name="id"></p> 
    <p>UserID :<input type="name" name="name"></p> 
    <input type="submit"> 
</form> 
```

The --{% csrf_token %}-- tag is necessary to prevent cross-site forgery attacks. You’ll learn more about this later on in the course.

Next, you’ll need to provide a view that will render this form:

```
def showform(request): 
    return render(request, "form.html") 
```

The URL patterns list must be updated using the following path:

```
path("showform/", views.showform, name="showform"), 
```

The http://localhost:8000/myapp/showform/ URL displays this form to the user:
![bodyparameter](/BodyParameter/img/output-body.png)

The form data that the user posts becomes part of the request body. 

Therefore, the name attribute of each form element becomes a body parameter and the data entered becomes its value. 

The view function passes these body parameters from the --request.POST-- dictionary-like attribute.


```
def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 
```
Complete the form and submit it. The --getform()-- function returns the data as its response. 
![getformoutput](/BodyParameter/img/LEO7ufS6R_6qwT8HPgqdXQ_cdf67e17917843daaa9d6a54c3f7bce1_C5M2L2_Itm05_2.png)

