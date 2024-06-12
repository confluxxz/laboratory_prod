from goods.models import Items
from experiments.models import Experiment
from django.http import JsonResponse
from django.template.loader import render_to_string
from experiments.utilts import get_user_experiments
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def experiment_add(request):

    item_id = request.GET.get("item_id")

    item = Items.objects.get(id=item_id)

    if request.user.is_authenticated:
        experiments = Experiment.objects.filter(user=request.user,
                                                item=item,
                                                )

        if experiments.exists():
            experiment = experiments.first()
            if experiment:
                experiment.quantity += 1
                experiment.save()
        else:
            Experiment.objects.create(user=request.user,
                                      item=item,
                                      quantity=1)


    else:
        experiments: Experiment.objects.filter(
            session_key=request.session_key,
            item=item,

        )
        if experiments.exists():
            experiment: experiments.first()
            if experiment:
                experiment.quantity += 1
                experiment.save()

        else:
            Experiment.objects.create(session_key=request.session.session_key,
                                      item=item,
                                      quantity=1)

    messages.success(request, "Предмет добавлен")
    return HttpResponseRedirect(reverse('main:index'))



def experiment_change(request):
    experiment_id = request.GET.get("experiment_id")
    quantity = request.GET.get("quantity")

    experiment = Experiment.objects.get(id=experiment_id)

    experiment.quantity = quantity
    experiment.save()

    experiment = get_user_experiments(request)
    experiment_items_html = render_to_string(
        "experiments/includes/included_experiment.html", {"experiments": experiment}, request=request
    )

    response_data = {
        'message': 'Количество изменено',
        'experiment_items_html': experiment_items_html
    }

    return JsonResponse(response_data)


def experiment_remove(request):

    experiment_id = request.GET.get("experiment_id")

    experiment = Experiment.objects.get(id=experiment_id)
    quantity = experiment.quantity
    experiment.delete()

    # user_experiment = get_user_experiments(request)
    # experiment_items_html = render_to_string(
    #     "experiments/includes/included_experiment.html", {"experiments": user_experiment}, request=request
    # )
    # response_data = {
    #     "message": 'Предмет удалён из эксперимента',
    #     "experiment_items_html": experiment_items_html,
    #     "quantity_deleted": quantity,
    # }
    #
    # return JsonResponse(response_data)
    messages.success(request, "Предмет удалён")
    return HttpResponseRedirect('/works/create-work/')
