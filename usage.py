from venzoscf.models import TransitionManager
from venzoscf.views import scftransition



TransitionManager.objects.create(type = "PROGRAM")


# initiating a transition


@scftransition(type = "PROGRAM")
def myfunc():
    return "data"


### sample  functions   ###