from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.db.models import Avg, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import Borrel, Entry
from .forms import EntryForm

def index(request):
    borrel_list = Borrel.objects.order_by("-date")[:10]
    return render(request, "borrel/index.html", {'borrel_list': borrel_list})

def detail(request, item_id):
    borrel = get_object_or_404(Borrel, pk=item_id)
    if request.method == "POST":
        form = EntryForm(request.POST)

        def error_render(errors, code):
            return render(
                request,
                "borrel/detail.html",
                {"borrel": borrel, "form": form, "error_message": errors},
                status=code,
            )

        if not request.user.is_authenticated:
            return error_render("you need to be logged in to post a review", 401)
        if not form.is_valid():
            return error_render(form.errors, 400)

        new_item = form.save(commit=False)
        new_item.borrel = borrel
        new_item.person = request.user

        try:
            new_item.save()
        except IntegrityError as e:
            return error_render(e, 400)

        return HttpResponseRedirect(reverse("borrel:detail", args=(borrel.id,)))


    else:
        entry = None
        if request.user.is_authenticated():
            entry = Entry.objects.get(borrel=borrel, person=request.user)

        form = None
        if not entry:
            form = EntryForm()

        return render(request, "borrel/detail.html", {'borrel': borrel, 'form': form, 'entry': entry})

@login_required
@permission_required('borrel.view_result', raise_exception=True)
def result(request, item_id):
    borrel = get_object_or_404(Borrel, pk=item_id)
    stats = {
        "drinks": Entry.objects
            .values('drink')
            .annotate(
                drink__count=Count('drink'),
            )
            .order_by('-drink__count'),
        "foods": Entry.objects
            .values('food')
            .annotate(food__count=Count('food'))
            .order_by('-food__count'),
        "count": Entry.objects.count()
    }
    print(stats)
    return render(request, "borrel/result.html", {
        "borrel": borrel,
        "stats": stats
    })
