from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, redirect
from goods.models import Items
from goods.utilts import query_search
from experiments.forms import CreateExperimentForm
from experiments.models import Experiment
from django.contrib import auth, messages


def store(request, category_slug=None):
    page = request.GET.get('page', 1)
    existence = request.GET.get('existence', None)
    not_existence = request.GET.get('not_existence', None)
    # готово к работе;
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('query', None)

    if category_slug == 'all':
        goods = Items.objects.all()
    elif query:
        goods = query_search(query)
    else:
        goods = get_list_or_404(Items.objects.filter(category__slug=category_slug))

    if existence:
        goods = goods.filter(existence=True)

    if not_existence:
        goods = goods.filter(existence=False)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, per_page=6) #выводим по 3 предмета
    current_page = paginator.page(int(page))

    context = {
        'title': 'Склад',
        'goods': current_page,
        'slug_url':category_slug,

    }
    return render(request, 'goods/store.html', context)


def item(request, item_slug):
    item = Items.objects.get(slug=item_slug)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateExperimentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            Experiment.objects.create(user=request.user,
                                      item=item,
                                      quantity=form.cleaned_data.get('quantity'),
                                      units=form.cleaned_data.get('units'),
                                      date=form.cleaned_data.get('date'),
                                      )
            messages.success(request, "Предмет добавлен")
            return HttpResponseRedirect("/works/create-work/")

    else:
        form = CreateExperimentForm()
    return render(request, 'goods/item.html', {'form': form, 'item':item})



    # item = Items.objects.get(slug=item_slug)
    #
    # context = {
    #     'item': item,
    #
    # }
    #
    # return render(request, 'goods/item.html', context=context)

