from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import requests
from .models import ContactDetail


# Create your views here.

# def home(request):
#     a = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
#     print("response",a)
#     context = {
            
#             "su": User.objects.filter(is_superuser=True).values_list('username')
#         }
#     return render(request,'user/home.html', context)


def home(request):

    # url = "https://amazon24.p.rapidapi.com/api/product"
    # querystring = {"keyword":"iphone","country":"US","page":"1"}
    # headers = {
    #     'x-rapidapi-host': "amazon24.p.rapidapi.com",
    #     'x-rapidapi-key': "530381f333msh3eaefc537afac92p137c35jsn28b257d63e01"
    #     }
    # response = requests.get( url, headers=headers, params=querystring).json()

    # print(response)
    
    return render(request,'user/home.html')


# Using Rapid Api
# def about(request):

#     url = "https://amazon23.p.rapidapi.com/product-search"
#     querystring = {"query":"poco m3","country":"IN"}
#     headers = {
#         'x-rapidapi-host': "amazon23.p.rapidapi.com",
#         'x-rapidapi-key': "08565f93abmsh46d2e48f99ae72ap1a660ajsnb1138a79da69"
#         }
#     response = requests.request("GET", url, headers=headers, params=querystring).json()
#     print(response)
    
#     found=0
    
#     product_keywords = [ 'm3', '6gb', '64gb','blue']
#     for i in range(10):
#         title = response['result'][i]['title'].lower()
            
#         found_keyword = []
#         for keyword in range(len(product_keywords)):
#             if title.find(product_keywords[keyword]) != -1:
#                 found_keyword.append(product_keywords[keyword])
#                 if found_keyword == product_keywords:
#                     found = 1
#                     discounted = response['result'][i]['price']['discounted']
#                     current_price = response['result'][i]['price']['current_price']
#                     currency = response['result'][i]['price']['currency']
#                     before_price = response['result'][i]['price']['before_price']
#                     savings_amount = response['result'][i]['price']['savings_amount']
#                     savings_percent = response['result'][i]['price']['savings_percent']
#                     product_url = response['result'][i]['url']
#                     thumbnail = response['result'][i]['thumbnail']
                    
#                     return_product_detail = {
#                         'discounted' : discounted,
#                         'current_price' : current_price,
#                         'before_price' : before_price,
#                         'savings_amount' : savings_amount,
#                         'savings_percent' : savings_percent,
#                         'product_url' : product_url,
#                         'title' : title,
#                         'thumbnail' : thumbnail,  
#                         'currency' : currency 
#                     }
#                     print(found_keyword," found Product is available")
#                     break
                
#         if found == 1:
#             break
#         else:
#             print(found_keyword ," Product NOT-FOUND")
                
    
#     # print(discounted)
#     # print(current_price)
#     # print(currency)
#     # print(before_price)
#     # print(savings_amount)
#     # print(savings_percent)
#     # print(product_url)
#     # print(title)
#     # print(thumbnail)

#     return render(request, 'user/about.html')
    
    
    
    
    
    
    
# Using Rainforest Api 
def about(request):

    # set up the request parameters
    params = {
    'api_key': '62B5DE806E2D46C78A8C79B94F99D379',
    'type': 'search',
    'amazon_domain': 'amazon.in',
    'search_term': 'poco m3'
    }

    # make the http GET request to Rainforest API
    response = requests.get('https://api.rainforestapi.com/request', params).json()
    
    # print the JSON response from Rainforest API
    # print(response)
    
    found=0
    product_keywords = ['m3','poco', '6gb', '128gb']
    for i in range(10):
        title = response['search_results'][i]['title'].lower()
        
        found_keyword = []
        for keyword in range(len(product_keywords)):
            if title.find(product_keywords[keyword]) != -1:
                found_keyword.append(product_keywords[keyword])
                if found_keyword == product_keywords:
                    found = 1
                    # discounted = response['result'][i]['price']['discounted']
                    # current_price = response['result'][i]['price']['current_price']
                    # currency = response['result'][i]['price']['currency']
                    # before_price = response['result'][i]['price']['before_price']
                    # savings_amount = response['result'][i]['price']['savings_amount']
                    # savings_percent = response['result'][i]['price']['savings_percent']
                    product_url = response['search_results'][i]['link']
                    thumbnail = response['search_results'][i]['image']
                    
                    return_product_detail = {
                        # 'discounted' : discounted,
                        # 'current_price' : current_price,
                        # 'before_price' : before_price,
                        # 'savings_amount' : savings_amount,
                        # 'savings_percent' : savings_percent,
                        # 'currency' : currency ,
                        'product_url' : product_url,
                        'title' : title,
                        'thumbnail' : thumbnail,  
                        
                    }
                    print(found_keyword," found Product is available")
                    break
                
        if found == 1:
            break
        else:
            print(found_keyword ," Product NOT-FOUND")
                
    
    # print(discounted)
    # print(current_price)
    # print(currency)
    # print(before_price)
    # print(savings_amount)
    # print(savings_percent)
    # print(product_url)
    # print(title)
    # print(thumbnail)

    return render(request, 'user/about.html')
    

    
def contact(request):
    if request.method == "POST":   
        nm = request.POST["name"]
        em = request.POST["email"]
        ph = request.POST["phone"]
        msg = request.POST["message"]
        ins = ContactDetail(name=nm, email=em, phone=ph, message=msg)
        ins.save()
        
    return render(request,'user/contact.html')