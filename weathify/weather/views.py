from django.shortcuts import render


def main_page(request):
    return render(request, 'pages/home_page.html')


def page_not_found(request, exception):
    return render(request, 'pages/404_page.html', status=404)

