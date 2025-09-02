from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.db import DatabaseError

def Product_list(request):
    try:
        products=Product.objects.all()
        return render(request, "products/products_list.html", {"products":products})
    except DatabaseError as e:
        print(f"Database error:{e}")
        return HttpResponse("Sorry, we are experiencing database issues.", status=500)
    except Exception as e:
        print(f"Unexpected error:{e}")
        return HttpResponse("An unexpected error occurred.", status=500)
def product_detail(request, product_id):
    try:
        product=get_object_or_404(product, id=product_id)
        return render(request, "products/product_detail.html", {"product":product})
    except Product.DoesNotExist:
        return HttpResponse("Product Not Found.", status=400)
    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse("Something went wrong.", status=500)