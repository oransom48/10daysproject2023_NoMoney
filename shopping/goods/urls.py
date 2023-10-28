from django.contrib import admin
from django.urls import path, include
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:product_id>/', views.details, name='details'),
    path('searched/', views.searched, name='searched'),

    # sign up & log in
    path("signup/", SignUpView.as_view(), name="signup"),
    path('accounts/', include("django.contrib.auth.urls")),

    # cart
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart_detail/", views.cart_detail, name="cart_detail"),

    # cart summary and save order
    path("order_summary/", views.order_summary, name="order_summary"),
    path("save_order/", views.save_order, name="save_order"),

    # payment
    path("payment/", views.payment, name="payment"),

    # for shop admin
    path("order_list/", views.ordered_list, name="ordered_list"),
    path("order_detail/<int:ordered>", views.order_detail, name="order_detail"),
]