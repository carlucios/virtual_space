from django.shortcuts import render, get_object_or_404

from gallery.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("-id").filter(publicar=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})