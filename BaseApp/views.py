import requests
from bs4 import BeautifulSoup
from django.shortcuts import render





def HomePage(request):
    return render(request, 'home.html')
    

def SearchPage(request):
    return render(request, 'Search_Page.html')


def Compare_Page(request):
    search_term = request.GET.get('search_term', 'laptop')  # Default to "laptop" if search term is not provided

    # Create a list of Amazon URLs with the search term
    urls = [
        f'https://www.amazon.de/s?k={search_term}&ref=nb_sb_noss_2',
        f'https://www.amazon.co.uk/s?k={search_term}&ref=nb_sb_noss_2',
        f'https://www.amazon.com.be/s?k={search_term}&ref=nb_sb_noss_2',
        f'https://www.amazon.fr/s?k={search_term}&ref=nb_sb_noss_2'
    ]

    results = []  # List to store search results

    # Loop through the URLs and scrape the search results
    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('div', {'data-component-type': 's-search-result'})
        for item in items:
            title_element = item.find('h2', {'class': 'a-size-mini'})
            title = title_element.text.strip() if title_element else ''

            price_element = item.find('span', {'class': 'a-price-whole'})
            price = price_element.text.replace(',', '.') if price_element else 'N/A'

            image_element = item.find('img', {'class': 's-image'})
            image_url = image_element['src'] if image_element else ''

            url_element = item.find('a', {'class': 'a-link-normal'})
            product_url = url_element['href'] if url_element else ''

            currency_symbol_element = item.find('span', {'class': 'a-price-symbol'})
            currency_symbol = currency_symbol_element.text.strip() if currency_symbol_element else ''

            results.append({
                'title': title,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'currency_symbol': currency_symbol
            })
    # Create a dictionary to pass to the template
    context = {
        'search_term': search_term,
        'results': results,
    }

    # Render the template with the context
    return render(request, 'Compare_Page.html', context)
