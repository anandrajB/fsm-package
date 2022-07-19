
# SCF_FSM_PACKAGE

A resuable django application that can handle transition and workflow's in your project .


## Authors

- [@anandrajB](https://github.com/anandrajB)
- [@Mohamed-Sheik-Ali](https://github.com/Mohamed-Sheik-Ali)


## Installation

Install scf_fsm_package with pip

```bash
pip install django-venzo-scf==1.0.5
```

In your django application , browse to installed_apps section 
and add this ,

```bash
INSTALLED_APPS = [
    'venzoscf'
]
```

now navigate to the middleware section and add the venzoscf middleware


```
MIDDLEWARE = [
    'venzoscf.middleware.TransitionUserMiddleware',
]
```

#### Additional Api (optional)

In your application's urls.py , you can include venzoscf's api urls for browsable api's 

** make sure that you have installed [DjangoRestFramework](https://www.django-rest-framework.org/#installation)


Now add this peice of code in your urls.py

```
urlpatterns = [
    path('', include('venzoscf.urls'))
]
```

## Usage/Examples


1. import your transition function from venzoscf.views 

2. The transition function requires 4 positional arguments :

3.
    |  Arguments   | Data_Type  |
    | ------------- | ------------- |
    | type   | str  |
    | action  | str  |
    | stage  | int  |
    | id (optional) | int  | 


```python
from venzoscf.views import Venzoscf

myhandler = Venzoscf()

# example function

def index():
    myhandler.transition(type = "PROGRAM",action = "submit" ,stage = 0)
    return HttpResponse({"data"})

```


## Tech Stack

    1. Python
    2. Django==3.2.5
    3. Django-rest-framework


## API 

#### Api urls 


| Api URL's  | METHOD | QUERY_PARAMS |
| ------------- | ------------- | ------------- |
| *localhost/model/* | GET  | ?type=PROGRAM |
| *localhost/*action*/* | GET | NONE |
| *localhost/*action*/* | POST | NONE |
| *localhost/*workflowitems*/* | GET | NONE |
| *localhost/workevents/* | GET | NONE |




## Support

For support, email support@venzo.com .

