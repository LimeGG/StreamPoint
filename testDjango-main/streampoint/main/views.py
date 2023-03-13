from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    user_id = request.user.id
    print(user_id)
    response = HttpResponse()
    response.set_cookie('user_id', user_id)  # устанавливаем куки с id пользователя
    return render(request, "main/index.html")

