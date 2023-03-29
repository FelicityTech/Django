# HttpRequest Object
The request object is characterized by its attributes and methods. They are used extensively in the processing logic of a Django view.

### request.method
The view logic uses this attribute to identify how the client has approached the server. A browser submits its request using any HTTP methods or verbs – POST, GET, DELETE, and PUT.

* request.GET and request.POST
The attributes return a dictionary-like object containing GET and POST parameters, respectively. 

* request.COOKIES
Along with the parameters, the browser also packs the request objects with cookies inserted by the server’s previous interactions. It is a dictionary of string keys and values.

* request.FILES
When the user uploads one or more files with a multipart form, they are present in this attribute in the form of UploadedFile objects. By appropriate logic in the view, these uploaded files are saved in the designated folder on the server.

* request.user
The request object also contains information about the current user. This attribute is an object of django.contrib.auth.models.User class. However, if the user is unauthenticated, it returns AnonymousUser. Inside the view, you can lay down separated separate logic for either of them.
    if request.user.is_authenticated(): 
    # Do something for logged-in users. 
    else: 
    # Do something for anonymous users. 


* request.has_key()
This is a method available to the request object. It helps check whether the GET or POST parameter dictionary has a value for the given key.

Unlike the HttpRequest object, which is supplied by the server’s context, the response object of HttpResponse class is instantiated inside the view function before it is returned to the client. For example:

    from django.http import HttpResponse 
    def index(request): 
        return HttpResponse("Hello World")


Although it is possible to render a hardcoded HTML string as the response, Django offers a better alternative to render a template web page.

    from django.http import HttpResponse 
    from django.template import loader 
    def index(request): 
        template = loader.get_template('demoapp/index.html') 
        context={}  
        return HttpResponse(template.render(context, request))


## HttpResponseObject

Some of the main attributes and methods of the HttpResponse object are:

status_code: returns the HTTP status code corresponding to the response

content: returns the byte string of the response.

    __getitem__(): method that returns the value of a header

    __setitem__(): method used to add a header

    write(): This method creates a file-like object.

The following example demonstrates the attributes of the request and response objects. Add the following view function in views.py of the Django app.
