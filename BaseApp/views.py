from django.shortcuts import render

def HomePage(request):
    return render(request, 'home.html')
    

def SearchPage(request):
    return render(request, 'Search_Page.html')


def Compare_Page(request):
    return render(request, 'Compare_Page.html')


