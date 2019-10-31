from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hithere': 'Hello Visitor'})


def count(request):
    fulltext = request.GET['fulltext']
    a = fulltext.split()
    b = {}

    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1



    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(a), 'b': b.items()})


def about(request):
    return render(request, 'about.html', {'hello': 'This is the about section'})
