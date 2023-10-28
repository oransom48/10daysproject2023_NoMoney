from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic
from django.urls import path, reverse_lazy
from .models import Goods, Cart, Product, Ordered

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# main page
def main(request):
    return render(request, 'main.html')

def productlist(request):
    mygoods = Goods.objects.all().values()
    template = loader.get_template('productlist.html')
    context = {
        'mygoods': mygoods,
    }
    return HttpResponse(template.render(context, request))

def searched(request):
    if request.method == 'POST':
        keyword = request.POST.get('textfield', None)
        try:
            goods = Goods.objects.filter(goodsname__contains = keyword)
            template = loader.get_template('searched.html')
            context = {
                'goods': goods,
                'keyword': keyword
            }
            return HttpResponse(template.render(context, request))
        except Goods.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'master.html')

def filter(request):
    if request.method == 'POST':
        filtermin = request.POST.get('min')
        filtermax = request.POST.get('max')
        sort = request.POST.get('sort')

        tempmin = 0
        tempmax = 9999999999

        # checkfilter
        if filtermin=='' and filtermax=='':
            return redirect("productlist")
        elif filtermin:
            tempmin = filtermin
        elif filtermax:
            tempmax = filtermax
        else:
            tempmin = filtermin
            tempmax = filtermax

        # checksort
        if sort=='nameasc':
            mygoods = Goods.objects.filter(price__range=(tempmin, tempmax)).order_by('goodsname').values()
        elif sort=='namedsc':
            mygoods = Goods.objects.filter(price__range=(tempmin, tempmax)).order_by('-goodsname').values()
        elif sort=='priceasc':
            mygoods = Goods.objects.filter(price__range=(tempmin, tempmax)).order_by('price').values()
        elif sort=='pricedsc':
            mygoods = Goods.objects.filter(price__range=(tempmin, tempmax)).order_by('-price').values()

        template = loader.get_template('productlist.html')
        context = {
            'mygoods': mygoods,
            'filtermin':filtermin,
            'filtermax':filtermax,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("productlist")

def details(request, product_id):
    goods = Goods.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
    context = {
        "goods": goods,
        "cart_item": cart_item,
    }
    return render(request, "details.html", context)

# cart
@login_required
def add_to_cart(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
    product_price = Goods.objects.get(id=product_id).price
    
    if request.method == "POST":
        amount = request.POST.get('integerfield')
        amount = float(amount)
        if amount == 0:
            return redirect("remove_from_cart", product_id)
        if cart_item:
            cart_item.quantity = amount
            cart_item.sum_price = amount * cart_item.price
            cart_item.save()
            messages.success(request, "Item added to your cart.")
        else:
            product_name = Goods.objects.get(id=product_id).goodsname
            Cart.objects.create(user=request.user,
                                product_id=product_id, 
                                product_name=product_name,
                                price=product_price, 
                                quantity=amount, 
                                sum_price=amount*product_price)
            messages.success(request, "Item added to your cart.")

    return redirect("productlist")

@login_required
def remove_from_cart(request, item_id):
    cart_item = Cart.objects.filter(user=request.user, product_id=item_id)
    # if cart_item.user == request.user:
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")

    return redirect("cart_detail")

def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)


# cart summary and save order
@login_required
def save_order(request):
    in_cart = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.price for item in in_cart)

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        tel = request.POST.get('tel')

        this_order = Ordered(user=request.user,
                            firstname=firstname,
                            lastname=lastname,
                            address=address,
                            tel=tel,
                            total_price=total_price,
                            paid=True,
                            )
        this_order.save()
        for item in in_cart:
            this_order.products.create(product_id=item.product_id, 
                                        product_name=item.product_name,
                                        price=item.price, 
                                        quantity=item.quantity, 
                                        sum_price=item.sum_price)

        # clear cart
        cart_item = Cart.objects.filter(user=request.user)
        cart_item.delete()  
           
    return redirect("payment")

def order_summary(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/order_summary.html", context)

# payment
def payment(request):
    # template = loader.get_template('payment.html')
    return render(request, 'payment.html')

# (dashboard) ordered page
def ordered_list(request):
    orders = Ordered.objects.all()
    # product_order = Product.objects.all()
    template = loader.get_template('shop/ordered.html')
    context = {
        'orders': orders,
        # 'product_order': product_order,
    }
    return HttpResponse(template.render(context, request))

def order_detail(request, ordered):
    orderdetail = Product.objects.filter(ordered=ordered)
    template = loader.get_template('shop/order_detail.html')
    context = {
        'orderdetail': orderdetail
    }
    return HttpResponse(template.render(context, request))