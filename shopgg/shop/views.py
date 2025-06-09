from django.shortcuts import render

# Create your views here.
def general_view(request):
    return render(request, 'general.html')

def company_view(request):
    return render(request, 'company.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def places_view(request):
    return render(request, 'places.html')

def items_view(request):
    return render(request, 'items.html')

def category_view(request):
    return render(request, 'category.html')

def all_view(request):
    return render(request, 'all.html')

def basket_view(request):
    return render(request, 'basket.html')

