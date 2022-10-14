from django.urls import path
from cor.views import store, card, checkout

urlpatterns = [

    path('', store , name='store'),
    path('card/', card, name='card'),
    path('checkout/', checkout, name='checkout'),
]