from django.shortcuts import render


def tests(request):
    context = {
        'title': 'Тест',
        'content': 'Перед началом работы, пожалуйста, пройдите тест',
        'text_on_page': "Вопрос №1: Вопрос?"
    }
    return render(request, "tests/test.html", context)

