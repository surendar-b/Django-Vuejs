from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser 
from .models import Categorys,Products
from .serializers import CategorySerializer,ProductSerializer


@csrf_exempt
def CategoryInsert(request):
    if request.method == 'POST':
        category_data= JSONParser().parse(request)
        category_serializer=CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()  #insert to the table
            result = {"success":True,"message": "Category created successfully"}
            return JsonResponse(result,safe=False)
        result = {"success":False,"message": "Failed on creating category"}
        return JsonResponse(result,safe=False)


@csrf_exempt
def InsertProduct(request):
    if request.method == "POST":
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data =product_data)
        if product_serializer.is_valid():
            product_serializer.save() # insert product data
            result = {"success":True,"message":"Product added successfully"}
            return JsonResponse(result,safe=False)
        result = {"success":False,"message":"Failed to add product"}
        return JsonResponse(result,safe=False)

def SelectAllCategorys(request):
    if request.method == "GET":
        categorys = Categorys.objects.all()
        category_serializer = CategorySerializer(categorys,many=True)
        return JsonResponse(category_serializer.data,safe=False)

def SelectAllProducts(request):
    if request.method == "GET":
        products = Products.objects.all()
        product_serializer = ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)

def SelectProduct(request,id=0):
    if request.method == "GET":
        item = Products.objects.filter(category=id)
        item_serializer = ProductSerializer(item,many=True)
        return JsonResponse(item_serializer.data,safe=False) 

def GetProduct(request,id=0):
    if request.method == "GET":
        item = Products.objects.get(id=id)
        item_serializer = ProductSerializer(item,many=False)
        return JsonResponse(item_serializer.data,safe=False) 

@csrf_exempt
def UpdateProduct(request,id=0):
    if request.method == "PUT":
        product_data = JSONParser().parse(request)
        product=Products.objects.get(id=id)
        product_serializer = ProductSerializer(product,data =product_data)
        if product_serializer.is_valid():
            product_serializer.save() # insert product data
            result = {"success":True,"message":"Product updated successfully"}
            return JsonResponse(result,safe=False)
        result = {"success":False,"message":"Failed to updating product"}
        return JsonResponse(result,safe=False)

@csrf_exempt
def UpdateCategory(request,id=0):
    if request.method == 'PUT':
        category_data= JSONParser().parse(request)
        category = Categorys.objects.get(id=id)
        category_serializer=CategorySerializer(category,data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()  #insert to the table
            result = {"success":True,"message": "Category updated successfully"}
            return JsonResponse(result,safe=False)
        result = {"success":False,"message": "Failed on updating category"}
        return JsonResponse(result,safe=False)

@csrf_exempt
def DeleteCategory(request,id=0):
    if request.method == 'DELETE':
        item = Categorys.objects.get(id=id)
        item.delete()
        return JsonResponse("Category deleted succesfully",safe=False)

@csrf_exempt
def DeleteProduct(request,id=0):
    if request.method == 'DELETE':
        item = Products.objects.get(id=id)
        item.delete()
        return JsonResponse("Product deleted succesfully",safe=False)

# Create your views here.
