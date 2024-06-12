from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from experiments.models import Experiment

from works.forms import CreateWorkForm, UpdateWorkForm
from works.models import Work, WorkItem

from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def create_work(request):
    if request.method == 'POST':
        form = CreateWorkForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    experiment_items = Experiment.objects.filter(user=user)

                    if experiment_items.exists():
                        # Создать работу
                        work = Work.objects.create(
                            user=user,
                            name=form.cleaned_data['name'],
                            description=form.cleaned_data['description'],
                            requires_files=form.cleaned_data['requires_files'],
                            additional_files=form.cleaned_data['additional_files'],
                        )
                        # Создать заказанные предметы эксперимента
                        for experiment_item in experiment_items:
                            item = experiment_item.item
                            name = experiment_item.item.name
                            quantity = experiment_item.quantity

                            if item.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                       В наличии - {item.quantity}')

                            WorkItem.objects.create(
                                work=work,
                                item=item,
                                name=name,
                                quantity=quantity,
                                date=experiment_item.date,
                                units=experiment_item.units,
                            )
                            if item.category_id < 3: #категория 3-оборудование, 4-посуда
                                item.quantity -= quantity
                                item.save()

                        # Очистить эксперимент пользователя после создания работы
                        experiment_items.delete()

                        messages.success(request, 'Эксперимент оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('experiment:work')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }

        form = CreateWorkForm(initial=initial)

    context = {
        'title': 'Оформление работы',
        'form': form,
        'work': True,
    }
    return render(request, 'works/create_work.html', context=context)

@login_required
def upload_results(request):
    if request.method == 'POST':
        form = UpdateWorkForm(request.POST, request.FILES)
        if form.is_valid():
            work = Work.objects.get(id=form.cleaned_data['work'])
            work.results = form.cleaned_data['results']
            work.is_done = True
            work.save()
            messages.success(request, "Результат загружен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UpdateWorkForm()

    context = {
        'title': 'Личный кабинет',
        'form': form,
        'work': True,
    }
    return render(request, 'users/profile.html', context)


