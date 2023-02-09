from django.shortcuts import render

def HomePage(request):
    return render(request, 'home.html')
    

def SearchPage(request):
    return render(request, 'Search_Page.html')


def Compare_Page(request):
    return render(request, 'Compare_Page.html')


    """need to change it to the tample of the search page here
    for example:
        def best_to_compare(request):
            amazonSites = Member.objects.all().values()
            template = loader.get_template('amazon_sites.html')
            context = {
                'amazonSites': amazonSites,
            }
            return HttpResponse(template.render(context, request))
    """

