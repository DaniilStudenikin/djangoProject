from django.shortcuts import render


# Create your views here.
def testfunc(request):
    array = list(request.GET.items())
    context = {'helloworld': 'Hi, Mike, what`s up',
               'get_result': array}
    bbb = request.GET.get('bbb', None)
    if bbb is not None:
        context['get_result'].append(bbb * 10)

    return render(request, 'testest.html', context=context)
