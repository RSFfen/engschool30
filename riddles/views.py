from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Riddle, Option


def homePageView(request):
    return HttpResponse("Привет, мир!")


def index(request):
    return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5]})


def detail(request, riddle_id):
    return render(request, "answer.html", {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Ответ не найден в базе знаний'})
    else:
        if option.correct:
            return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5], "message": "Отлично! Выберите другую загадку!"})
        else:
            return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Неправильный ответ!'})
