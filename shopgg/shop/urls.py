from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', general_view, name='general_view'),
    path('company/', company_view, name='company_view'),
    path('company/contacts/', contacts_view, name='contacts_view'),
    path('company/places/', places_view, name='places_view'),
    path('items/', items_view, name='items_view'),
    path('items/category/', category_view, name='category_view'),
    path('items/all/', all_view, name='all_view'),
    path('basket/', basket_view, name='basket_view')
]
