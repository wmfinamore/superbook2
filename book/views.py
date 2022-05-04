from django.http import HttpResponse
from django.views.generic import View


class GreetView(View):
    greeting = "Hello {}!"
    default_name = "World"

    def get(self, request, **kwargs):
        name = kwargs.pop("name", self.default_name)
        return HttpResponse(self.greeting.format(name))


class SuperVillain(GreetView):
    greeting = "We are the future, {}. Not them."
    default_name = "my friend"
