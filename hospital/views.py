from django.shortcuts import render
from django.views import View
# Create your views here.


def index(request):
    return render(request, "hospital/index.html")


def HelloDoctView(request):
    return render(request, 'hospital/doctorclick.html')


class doctorLoginView(View):
    def get(self, request):
        return render(request, "hospital/doctorlogin.html")

    def post(self, request):
        pass


class doctorsigninView(View):
    def get(self, request):
        return render(request, "hospital/doctorsignup.html")

    def post(self, request):
        pass
