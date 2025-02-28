import json
from django.shortcuts import render, redirect
from ecommerceapp.models import Contact, Product, Orders, OrderUpdate
from django.contrib import messages
from math import ceil
# Home Page View
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')

    # Extract unique categories
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        if n > 0:  # Ensure there are products in the category
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides + 1), nSlides])

    params = {'allProds': allProds}
    return render(request, "index.html", params)


# Contact Page View
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        phonenumber = request.POST.get("phonenumber")

        # Save contact form data
        myquery = Contact(name=name, email=email, desc=desc, phonenumber=phonenumber)
        myquery.save()

        messages.success(request, "We will get back to you soon.")
        return redirect("contact")  # Redirect to avoid form resubmission on refresh

    return render(request, "contact.html")


# About Page View
def about(request):
    return render(request, "about.html")



def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        phone = request.POST.get('phone', "")
        amount = request.POST.get('amt', "")

        # Save order
        order = Orders(items_json=items_json, name=name, email=email, address=address, phone=phone, amount=amount)
        order.save()
        
        # Show success message
        messages.success(request, "Your order has been placed successfully!")

        #  CLEAR CART SESSION
        if 'cart' in request.session:
            del request.session['cart']
            request.session.modified = True  # Ensure changes are saved

        # Redirect to home
        return redirect("/")
    
    return render(request, "checkout.html")

