from django.shortcuts import render, redirect
from django.http import HttpResponse
from seller.models import Product, Category
from ecommerceProject.models import UserProfile
from .models import Cart
from django.db import connection

mycursor = connection.cursor()
# Create your views here.
def home(request):
	pObjs = Product.objects.all()
	catObjs = Category.objects.all()

	uObj = UserProfile.objects.get(user__username = request.user)

	mycursor.execute("SELECT COUNT(*) FROM buyer_cart WHERE user_id={}".format(uObj.id))
	res=mycursor.fetchone()

	return render(request, "WelcomeBuyer.html", {'products' : pObjs, 'catObjs':catObjs,'count':res[0]})

def cart(request, id):
	pObj = Product.objects.get(id=id)
	uObj = UserProfile.objects.get(user__username=request.user)
	url = '/buyer/'
	try:
		c = Cart(product=pObj, user=uObj)
		c.save()
	except:
		return HttpResponse('<script>alert("Product is already in your cart");\
			window.location="{}"</script>'.format(url))

	return HttpResponse('<script>alert("Product has been added in your cart!");\
			window.location="{}"</script>'.format(url))

	return redirect('/buyer/')


def view_cart(request):
	uObj = UserProfile.objects.get(user__username=request.user)
	cartObj = Cart.objects.filter(user_id = uObj)
	proList = []
	for i in cartObj:
		proList.append(Product.objects.get(id = i.product_id))
	return render(request,'cart.html',{'p':proList})

def category(request,id):
	CatProduct = Product.objects.filter(category_id = id)
	print(CatProduct)
	return render(request,"Category.html",{'categoryProds':CatProduct})

def deleteProduct(request,id):
	uObj = UserProfile.objects.get(user__username = request.user)
	cartObj = Cart.objects.get(product_id = id,user_id = uObj)
	cartObj.delete()
	return redirect("/buyer/view_cart/")