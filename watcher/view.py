from django.shortcuts import render
from django.template.context_processors import csrf

from .lookup import look_up


def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'hello.html', context)


def query_data(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.POST:
        print(request.POST['question'])
        ctx['rlt'] = look_up(request.POST['question'], int(request.POST['subtask']))
        ctx['qu'] = request.POST['question']
    return render(request, "data_search_post.html", ctx)
