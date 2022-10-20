from django.urls import path
from cor.views import store, card, checkout, updateItem, processOrder

urlpatterns = [

    path('', store , name='store'),
    path('card/', card, name='card'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name= 'update_item'),
    path('proccess_order/', processOrder, name= 'proccess_order'),

]