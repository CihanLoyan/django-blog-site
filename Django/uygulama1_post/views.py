from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import yazi
from .forms import CreateForm
from  django.utils.text import slugify
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def postliste_view(request):

    kelime = request.GET.get("kelime")
    if kelime:
        yazi_listesi = yazi.objects.filter(baslik__contains=kelime)
    else:
        yazi_listesi = yazi.objects.all()
    paginator = Paginator(yazi_listesi, 5)  # Show 5 contacts per page.

    page = request.GET.get('page')
    yazilar = paginator.get_page(page)

    return render(request, "liste.html", {"yazilar": yazilar})


def postcreate_view(request):
    form = CreateForm()

    return render(request, "create.html", {"form": form})


def postdelete_view(request, id):
    yaziNesne = yazi.objects.get(id = id)
    yaziNesne.delete()

    return HttpResponseRedirect("/uygulama1_post")


def postupdate_view(request, id):
    if request.GET.get("baslik"):
        yeniBaslik = request.GET.get("baslik")
        yeniMetin = request.GET.get("metin")


        yaziNesne = yazi.objects.get(id = id)

        yaziNesne.baslik = yeniBaslik
        yaziNesne.metin = yeniMetin
        yaziNesne.save()
    else:
        yaziNesne = yazi.objects.get(id = id)
    return render(request, "update.html", {"yazi": yaziNesne})


def postdetail_view(request, slug):
    yaziNesne = yazi.objects.get(slug = slug)

    yorumlar = yaziNesne.yorumlar.all()
    return render(request, "detail.html", {"yazi": yaziNesne, "yorumlar": yorumlar})


def formdoldur_view(request):
    form = CreateForm(request.POST, request.FILES)

    if form.is_valid():
        yaziNesne = form.save()

    """yaziBasligi = request.GET.get("baslik")
    yaziMetni = request.GET.get("metin")

    yazi.objects.create(baslik = yaziBasligi, metin = yaziMetni)
    """
    return render(request, "gonderildi.html", {})

# Create your views here.
