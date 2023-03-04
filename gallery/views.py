from django.shortcuts import render, get_object_or_404

from gallery.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("-id").filter(publicar=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-id").filter(publicar=True)

    if 'buscar' in request.GET:
        txt_a_buscar = request.GET['buscar']
        if txt_a_buscar:
            fotografias = fotografias.filter(nome__icontains=txt_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})