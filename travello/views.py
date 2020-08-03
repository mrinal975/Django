from django.shortcuts import render
from .models import designation
# Create your views here.
def index(request):

    des1 = designation()
    des1.name = "Dhaka"
    des1.price = 300
    des1.img = "destination/1.png"
    des2 = designation()

    des2.name = "Rajshahi"
    des2.price = 200
    des2.img = "destination/2.png"
    des3 = designation()

    des3.name = "Comilla"
    des3.price = 210
    des3.img = "destination/2.png"
    dess = [des1, des2, des3]
    return render(request, 'index.html', { 'dess':dess } )
