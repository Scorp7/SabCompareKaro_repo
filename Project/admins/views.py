from django import urls
from django.conf.urls import url
from user.models import AmazonData, FlipkartData, SnapdealData, ContactDetail
from django.http import request
from django.shortcuts import render, HttpResponseRedirect, redirect
from admins.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#MAIN
@login_required
@allowed_users(allowed_roles=['admin'])
def main(request):
    return render(request, 'admins/home.html')




# USER
# User show
@login_required
@allowed_users(allowed_roles=['admin'])
def user_detail(request):
    data = User.objects.all()
    context = {'user': 'active','Data': data,}
    
    return render(request, 'admins/user_detail.html', context)

# User Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_user(request,id):
    pi = ContactDetail.objects.get(pk=id)
    context = {'Data':pi}
    print("IN edit User")
    if request.method == "POST":
        print("IN IFFFF")
        # if form.is_valid():
        #     form.save()
        # else:
        #     pi = UserData.objects.get(pk=id)
        #     form = UserRegistration(instance=pi)
    # return render (request, 'user/edit.html', {'Form': form})

    return render(request, 'admins/home_url',context)

# User Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_user(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/admins/user_detail/')







# CONTACT
# Contact Show
@login_required
@allowed_users(allowed_roles=['admin'])
def contact_detail(request):
    data = ContactDetail.objects.all()
    context = {'contact': 'active','Data': data,}
    
    return render(request, 'admins/contact_detail.html', context)#

# Contact Add
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
# @login_required
# @allowed_users(allowed_roles=['admin'])
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
        return redirect('/admins/contact_detail/')






# AMAZON
# Amazon show
@login_required
@allowed_users(allowed_roles=['admin'])
def amazon_deals(request):
    data = AmazonData.objects.all()
    context = {'amazon': 'active','Data':data,}
    
    return render(request, 'admins/amazon_deals.html', context)

# Amazon Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_amazon(request,id):

    return render(request, 'admins/amazon_deals_url')

# Amazon Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_amazon(request, id):
    if request.method == "POST":
        pi = AmazonData.objects.get(pk=id)
        pi.delete()
        return redirect('/admins/amazon_deals')





# FLIPKART
# Flipkart show
@login_required
@allowed_users(allowed_roles=['admin'])
def flipkart_deals(request):
    data = FlipkartData.objects.all()
    context = {'flipkart': 'active','Data': data}
    
    return render(request, 'admins/flipkart_deals.html', context)

# Flipkart Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_flipkart(request,id):

    return render(request, 'admins/flipkart_deals_url')

# Flipkart Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_flipkart(request, id):
    if request.method == "POST":
        pi = FlipkartData.objects.get(pk=id)
        pi.delete()
        return redirect('/admins/flipkart_deals')




# SNAPDEAL
# Snapdeal Show
@login_required
@allowed_users(allowed_roles=['admin'])
def snapdeal_deals(request):
    data = SnapdealData.objects.all()
    context = {'snapdeal': 'active','Data': data}
    
    return render(request, 'admins/snapdeal_deals.html', context)
    
# Snapdeal Edit
@login_required
@allowed_users(allowed_roles=['admin'])
def edit_snapdeal(request,id):

    return render(request, 'admins/snapdeal_deals_url')

# Snapdeal Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_snapdeal(request, id):
    if request.method == "POST":
        pi = SnapdealData.objects.get(pk=id)
        pi.delete()
        return redirect('/admins/snapdeal_deals')

    
    
    
