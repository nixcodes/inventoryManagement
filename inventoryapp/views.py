from logging import exception
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Products
from django.views.defaults import page_not_found

# function to display all the products
def productsView(request):
    products_list = Products.objects.order_by("-ProductID")[:5]
    
    context = {
        "products_list": products_list,
    }

    if request.method=="POST":
        searchValue = request.POST.get("search_value")
        print(searchValue)
        if searchValue != False:
            print("calling product search view")
            return productSearchView(request, searchValue)

    return render(request, "inventoryapp/index.html", context)

# function to display the searched products
def productSearchView(request, searchValue):
    
    products_filterlist = Products.objects.filter(ProductID__icontains=searchValue)
    print(products_filterlist,"++++++++++++++++++++++++++")
    print(products_filterlist)
    context = {
            "products_list": products_filterlist,
    }
    return render(request, "inventoryapp/index.html", context)

# function to show product description
def productDescription(request, productSeq):
    #this function will operate when someone clicks a product id (bearing number) in the index.html page. Will display a page with the details of the product with edit option.

    products_list = Products.objects.get(ProductSeq=productSeq)
    
    if products_list is not None:
        print(products_list)
        return render(request, "inventoryapp/description.html", {"product_desc": products_list})
    else:
        return page_not_found(request, exception, template_name='404.html')
    
# function to modify/delete a product from the product table
def productsModify(request, productSeq=None):
    product = get_object_or_404(Products, ProductSeq = productSeq)

    if request.method=="POST" and request.POST.get("operation") == "update":
        print("Executing Update ---------------")
        product.ProductDesc = request.POST.get("description")
        product.ProductBrand = request.POST.get("brand")
        product.ProductMRP = request.POST.get("mrp")
        product.ProductPurchasePrice = request.POST.get("purchase_price")
        product.save()
        return updateSuccess(request)
    elif request.method=="POST" and request.POST.get("operation") == "delete":
        print("Executing Delete +++++++++++++++++")
        product.delete()
        return deleteSuccess(request)

    return render(request, "inventoryapp/modify.html", {"product": product})

# function to create new product
def productsCreate(request):
    if request.method == "POST" and request.POST.get("operation") == "create":
        productid = request.POST.get("productid")
        desc = request.POST.get("description")
        brand = request.POST.get("brand")
        mrp = request.POST.get("mrp")
        price = request.POST.get("purchase_price")
        print(productid, ",", desc, ",", brand, ",", mrp, ",", price)
        test = Products.objects.get(ProductID = productid)
        if productid == test.ProductID:
            print("printing if -------------------------------------")
            failed = {}
            return render(request, "inventoryapp/create.html", failed)

        products = Products(ProductID = productid, ProductDesc = desc, ProductBrand = brand, ProductMRP = mrp, ProductPurchasePrice = price)
        products.save()
        return render(request, "inventoryapp/create.html", {"message": "success"})  
    return render(request, "inventoryapp/create.html")

# other functions 
def productsDiscountCalc(request):
    return HttpResponse("Page to apply discount % and see the price.")

def updateSuccess(request):
    return HttpResponse(f"UpdatedSuccessfuly.")

def deleteSuccess(request):
    return HttpResponse(f"Deleted Successfuly.")