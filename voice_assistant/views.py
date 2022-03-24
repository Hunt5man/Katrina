from django.shortcuts import render

def showmain(request):
    return render(request, 'voice_assistant/base.html', {'title': 'Голосовой помощник "Катрина"'})

def aboutapp(request):
    return render(request, 'voice_assistant/aboutapp.html', {'title': 'О приложении'})

def aboutsite(request):
    return render(request, 'voice_assistant/aboutsite.html', {'title': 'О сайте'})

def aboutdevel(request):
    return render(request, 'voice_assistant/aboutdevel.html', {'title': 'О разработчике'})

def pageNotFound(request, exception):
    return render(request, 'voice_assistant/404.html', {'title': '404 Упс... А такой страницы нет'})

