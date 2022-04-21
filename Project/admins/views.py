from django import urls
from django.conf.urls import url
from user.models import AmazonData, FlipkartData, SnapdealData, ContactDetail
from django.http import request
from django.shortcuts import render, HttpResponseRedirect, redirect
from admins.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import urllib


#---------------------------------------------MAIN----------------------------------------------------------------------------
@login_required
@allowed_users(allowed_roles=['admin'])
def main(request):
    context = {"home":'active'}
    return render(request, 'admins/home.html',context)




# ---------------------------------------------------USER-----------------------------------------------------------------------

# User show
@login_required
@allowed_users(allowed_roles=['admin'])
def user_detail(request):
    data = User.objects.all()
    context = {'user': 'active','Data': data,}
    
    return render(request, 'admins/user_detail.html', context)

# User Add
@login_required
@allowed_users(allowed_roles=['admin'])
def add_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password2 = request.POST['confirm_password']
        form = User(username=username, email=email)
        form.save()
        pi = User.objects.get(username=username, email=email)
        pi.set_password(password)
        pi.save()
        data = User.objects.all()
        context = {'status_add': 'success', 'Data': data}
        return render(request, 'admins/user_detail.html', context)
        
    else:
        return render(request, 'admins/add_user.html')

# User Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_user(request,id):
    pi = User.objects.get(pk=id)
    context = {'Data':pi}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        form = User(username=username, email=email, id=id)
        form.save()
        pi.set_password(password)
        pi.save()
        print(User.objects.get(pk=id))
        data = User.objects.all()
        context = {'status_edit': 'success', 'id': id, 'Data': data}
        return render(request, 'admins/user_detail.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/edit_user.html',context)

# User Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_user(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        data = User.objects.all()
        context = {'status_delete': 'success', 'Data': data}
        return render(request, 'admins/user_detail.html', context)







# ------------------------------------------------CONTACT----------------------------------------------------------------------------


# Contact Show
@login_required
@allowed_users(allowed_roles=['admin'])
def contact_detail(request):
    data = ContactDetail.objects.all()
    context = {'contact': 'active','Data': data,}
    
    return render(request, 'admins/contact_detail.html', context)#

# Contact Add
@login_required
@allowed_users(allowed_roles=['admin'])
def add_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        form = ContactDetail(name=name, email=email, phone=phone, message=message)
        form.save()
        data = ContactDetail.objects.all()
        context = {'status_add': 'success', 'Data': data}
        return render(request, 'admins/contact_detail.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/add_contact.html')

# Contact Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_contact(request,id):
    pi = ContactDetail.objects.get(pk=id)
    context = {'Data':pi}
    if request.method == "POST":
        pi = ContactDetail.objects.get(pk=id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        form = ContactDetail(name=name, email=email, phone=phone, message=message, id=id)
        form.save()
        data = ContactDetail.objects.all()
        context = {'status_edit': 'success', 'id': id, 'Data': data}
        return render(request, 'admins/contact_detail.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/edit_contact.html',context)

# Contact Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_contact(request, id):
    if request.method == "POST":
        pi = ContactDetail.objects.get(pk=id)
        pi.delete()
        data = ContactDetail.objects.all()
        context = {'status_delete': 'success', 'Data': data}
        return render(request, 'admins/contact_detail.html', context)






# -----------------------------------------AMAZON-------------------------------------------------------------------------

# Amazon show
@login_required
@allowed_users(allowed_roles=['admin'])
def amazon_deals(request):
    data = AmazonData.objects.all()
    context = {'amazon': 'active','Data':data,}
    
    return render(request, 'admins/amazon_deals.html', context)

# Amazon Add
@login_required
@allowed_users(allowed_roles=['admin'])
def add_amazon(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = AmazonData(title=title, body=body, image=image, url=url)
        form.save()
        data = AmazonData.objects.all()
        context = {'status_add': 'success', 'Data': data}
        return render(request, 'admins/amazon_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/add_amazon.html')

# Amazon Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_amazon(request,id):
    pi = AmazonData.objects.get(pk=id)
    context = {'Data':pi}
    if request.method == "POST":
        pi = AmazonData.objects.get(pk=id)
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = AmazonData(title=title, body=body, image=image, url=url, id=id)
        form.save()
        data = AmazonData.objects.all()
        context = {'status_edit': 'success', 'id': id, 'Data': data}
        return render(request, 'admins/amazon_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/edit_amazon.html',context)

# Amazon Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_amazon(request, id):
    if request.method == "POST":
        pi = AmazonData.objects.get(pk=id)
        pi.delete()
        data = AmazonData.objects.all()
        context = {'status_delete': 'success', 'Data': data}
        return render(request, 'admins/amazon_deals.html', context)




# ---------------------------------------FLIPKART---------------------------------------------------------------------------------

# Flipkart show
@login_required
@allowed_users(allowed_roles=['admin'])
def flipkart_deals(request):
    data = FlipkartData.objects.all()
    context = {'flipkart': 'active','Data': data}
    
    return render(request, 'admins/flipkart_deals.html', context)

# Flipkart Add
@login_required
@allowed_users(allowed_roles=['admin'])
def add_flipkart(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = FlipkartData(title=title, body=body, image=image, url=url)
        form.save()
        data = FlipkartData.objects.all()
        context = {'status_add': 'success', 'Data': data}
        return render(request, 'admins/flipkart_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/add_flipkart.html')

# Flipkart Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_flipkart(request,id):
    pi = FlipkartData.objects.get(pk=id)
    context = {'Data':pi}
    if request.method == "POST":
        pi = FlipkartData.objects.get(pk=id)
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = FlipkartData(title=title, body=body, image=image, url=url, id=id)
        form.save()
        data = FlipkartData.objects.all()
        context = {'status_edit': 'success', 'id': id, 'Data': data}
        return render(request, 'admins/flipkart_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/edit_flipkart.html',context)


# Flipkart Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_flipkart(request, id):
    if request.method == "POST":
        pi = FlipkartData.objects.get(pk=id)
        pi.delete()
        data = FlipkartData.objects.all()
        context = {'status_delete': 'success','Data': data}
        return render(request, 'admins/flipkart_deals.html', context)




# --------------------------------------SNAPDEAL------------------------------------------------------------

# Snapdeal Show
@login_required
@allowed_users(allowed_roles=['admin'])
def snapdeal_deals(request):
    data = SnapdealData.objects.all()
    context = {'snapdeal': 'active','Data': data}
    
    return render(request, 'admins/snapdeal_deals.html', context)
    
# Snapdeal Add
@login_required
@allowed_users(allowed_roles=['admin'])
def add_snapdeal(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = SnapdealData(title=title, body=body, image=image, url=url)
        form.save()
        data = SnapdealData.objects.all()
        context = {'status_add': 'success', 'Data': data}
        return render(request, 'admins/snapdeal_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/add_snapdeal.html')

# Snapdeal Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_snapdeal(request,id):
    pi = SnapdealData.objects.get(pk=id)
    context = {'Data':pi}
    if request.method == "POST":
        pi = SnapdealData.objects.get(pk=id)
        title = request.POST.get('title')
        body = request.POST.get('body')
        url = request.POST.get('url')
        image = request.FILES.get('image')
        form = SnapdealData(title=title, body=body, image=image, url=url, id=id)
        form.save()
        data =SnapdealData.objects.all()
        context = {'status_edit': 'success', 'id': id, 'Data': data}
        return render(request, 'admins/snapdeal_deals.html', context)
        
        # pi = ContactDetail.objects.get(pk=id)
        # print(pi)
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})
    else:
        return render(request, 'admins/edit_snapdeal.html',context)

# Snapdeal Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_snapdeal(request, id):
    if request.method == "POST":
        pi = SnapdealData.objects.get(pk=id)
        pi.delete()
        data =SnapdealData.objects.all()
        context = {'status_delete': 'success', 'Data': data}
        return render(request, 'admins/snapdeal_deals.html', context)
    
    
    
