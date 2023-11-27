from django.urls   import path
from weather.views import main_page, page_not_found, answer_page


urlpatterns = [
    path('', main_page),
    path('answer/', answer_page, name='answer_page'),
]
