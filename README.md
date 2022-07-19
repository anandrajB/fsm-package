
# SCF_FSM_PACKAGE

a resuable django application that can handle transition and workflow's in your project .


## Authors

- [@anandrajB](https://github.com/anandrajB)
- [@Mohamed-Sheik-Ali](https://github.com/Mohamed-Sheik-Ali)


## Installation

Install scf_fsm_package with pip

```bash
pip install django-venzo-scf==1.0.5
```
    
## Usage/Examples

```python
from venzoscf.views import Venzoscf

myhandler = Venzoscf()

#simple function

**required arguments -> type , action ,stage , id(optional)

def index():
    myhandler.transition(type = "PROGRAM",action = "submit" ,stage = 0)
    return HttpResponse({"data"})

```


## Tech Stack

    1. Python
    2. Django==3.2.5
    3. Django-rest-framework


## API 

#### Get all transition models

```http
  GET localhost/model/
```


