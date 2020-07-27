from django.shortcuts import render,redirect
from .models import UserProfile,Category,Product
from django.contrib.auth.models import User
# Create your views here.
def seller(request):
    return render(request,"welcomeSeller.html")


def add_product(request):
    Catobjs = Category.objects.all()
    if request.method == 'POST':
        pname = request.POST['pname']
        price = request.POST['price']
        qty = request.POST['qty']
        desc = request.POST['desc']
        pic = request.FILES['pic']
        catid = request.POST['catid']

        uobj = UserProfile.objects.get(user__username = request.user)
        catobj = Category.objects.get(id=catid)

        p = Product(pname = pname,price = price, qty = qty, desc = desc,pic = pic, added_by = uobj, category = catobj)
        p.save()
        return redirect('/seller/add_product/')
    return render(request,'add_product.html',{'data':Catobjs})