from django.shortcuts import render
from .models import Hastalik

def hastalik_tespit_view(request):

    # Model ile ilgili tespit işlemleri burada yapılacak
    # Sonuçlar context'e eklenecek ve template'e gönderilecek
   
    hastaliklar = Hastalik.objects.all()
    context = {'hastaliklar': hastaliklar}
    return render(request, 'hastalik_tespiti/hastalik_tespit.html', context)
