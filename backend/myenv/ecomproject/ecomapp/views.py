from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    return Response("Hello World")


@api_view(["GET"])
def getProducts(request):
    return Response(products)


@api_view(["GET"])
def get_product_by_id(request, product_id):
    product = [product for product in products if product["id"] == str(product_id)]
    return Response(product[0])


@api_view(["POST"])
def postCart(request):
    data = request.data
    print("Data:", data)
    return Response("Item was added to cart")


@api_view(["GET"])
def getCartItems(request):
    sample_cart = [
        {
            "id": "1",
            "product": {
                "id": "14",
                "title": "Wireless Charger",
                "description": "Fast wireless charging pad",
                "image": "/product_images/Wireless_Charger.jpeg",
                "price": 29.99,
                "created_at": "2023-11-01T10:00:00Z",
                "updated_at": "2023-11-01T10:00:00Z",
            },
            "quantity": 2,
        },
        {
            "id": "2",
            "product": {
                "id": "15",
                "title": "Phone Tripod",
                "description": "Portable phone tripod for video",
                "image": "/product_images/Phone_Tripod.jpeg",
                "price": 22.99,
                "created_at": "2023-11-01T10:00:00Z",
                "updated_at": "2023-11-01T10:00:00Z",
            },
            "quantity": 1,
        },
    ]
    return Response(sample_cart)


@api_view(["DELETE"])
def removeCartItem(request, cart_item_id):
    print("Removing cart item with ID:", cart_item_id)
    return Response(f"Cart item with ID {cart_item_id} was removed")
