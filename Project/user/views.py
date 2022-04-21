from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
import requests
from .models import AmazonData, ContactDetail, FlipkartData, SnapdealData
import datetime
from admins.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .forms import ContactUsForm
import requests
import bs4


# Create your views here.

# def home(request):
#     a = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
#     print("response",a)
#     context = {
            
#             "su": User.objects.filter(is_superuser=True).values_list('username')
#         }
#     return render(request,'user/home.html', context)


#Home Page
def home(request):

    amazon = AmazonData.objects.all()
    flipkart = FlipkartData.objects.all()
    snapdeal = SnapdealData.objects.all()
    current = datetime.datetime.now()
    context = {'amazon': amazon, 'flipkart': flipkart, 'snapdeal': snapdeal , 'current': current, 'home': 'active'}
    
    # if User.is_superuser==True:
    #     return render(request,'admins/home.html')
    
    # if User.is_anonymous:
    #     return render(request,'user/home.html', context)
        
    

    return render(request,'user/home.html', context)

#About Page
def about(request):
    context = {'about': 'active'}
    return render(request,'user/services.html', context)


def contact(request):
    form = ContactUsForm()
    saved = False
    if request.method == "POST":   
        nm = request.POST["name"]
        em = request.POST["email"]
        ph = request.POST["phone"]
        msg = request.POST["message"]
        ins = ContactDetail(name=nm, email=em, phone=ph, message=msg)
        ins.save()
        saved = True
        
    context = {'contact': 'active', 'saved': saved, 'form': form}
        
    return render(request,'user/contact.html', context)
        


#Contact Page
# def contact(request):
#     saved = False
#     if request.method == "POST":   
#         nm = request.POST["name"]
#         em = request.POST["email"]
#         ph = request.POST["phone"]
#         msg = request.POST["message"]
#         ins = ContactDetail(name=nm, email=em, phone=ph, message=msg)
#         ins.save()
#         saved = True
        
#     context = {'contact': 'active', 'saved': saved}
        
#     return render(request,'user/contact.html', context)
    
#Services Page
def services(request):
    context = {'services': 'active'}
    return render(request,'user/services.html', context)
    


# Using Rainforest Api (Only Amazon Data)
def search_resul(request):

    if request.method == 'POST':
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        print(product_keywords)
        # set up the request parameters
        params = {
        'api_key': 'F61DC2435AE54951AEAC801B09EF29B1',
        'type': 'search',
        'amazon_domain': 'amazon.in',
        'search_term': text
        }

        # make the http GET request to Rainforest API
        response = requests.get('https://api.rainforestapi.com/request', params).json()
        
        # print the JSON response from Rainforest API
        # print(response)
        
        found = 0
        for i in range(5):
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
                        return render(request,'user/search_result.html', return_product_detail)
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

    return render(request, 'user/search_result.html')
    
  
# Using Rapid Api (Only amazon data)
def search_resul(request):

    url = "https://amazon23.p.rapidapi.com/product-search"
    querystring = {"query":"poco m3","country":"IN"}
    headers = {
        'x-rapidapi-host': "amazon23.p.rapidapi.com",
        'x-rapidapi-key': "08565f93abmsh46d2e48f99ae72ap1a660ajsnb1138a79da69"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    print(response)
    
    found=0
    
    product_keywords = [ 'm3', '6gb', '64gb','blue']
    for i in range(10):
        title = response['result'][i]['title'].lower()
            
        found_keyword = []
        for keyword in range(len(product_keywords)):
            if title.find(product_keywords[keyword]) != -1:
                found_keyword.append(product_keywords[keyword])
                if found_keyword == product_keywords:
                    found = 1
                    discounted = response['result'][i]['price']['discounted']
                    current_price = response['result'][i]['price']['current_price']
                    currency = response['result'][i]['price']['currency']
                    before_price = response['result'][i]['price']['before_price']
                    savings_amount = response['result'][i]['price']['savings_amount']
                    savings_percent = response['result'][i]['price']['savings_percent']
                    product_url = response['result'][i]['url']
                    thumbnail = response['result'][i]['thumbnail']
                    
                    return_product_detail = {
                        'discounted' : discounted,
                        'current_price' : current_price,
                        'before_price' : before_price,
                        'savings_amount' : savings_amount,
                        'savings_percent' : savings_percent,
                        'product_url' : product_url,
                        'title' : title,
                        'thumbnail' : thumbnail,  
                        'currency' : currency 
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
    
 # Using Rapid Api



# In use
# (Amazon Rapid Api &&& Flipkart webscraping)
def search_resul(request):
    if request.method == "POST":
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        print(product_keywords)
        
        #Used for flipkart in it's url
        words = ''
        for i in product_keywords:
            words = words+"%20"+i
        words = words[3:]

    #-----------------------------------------Amazon---------------------------------------

        #AMAZON (Rapid_Api)
        url = "https://amazon23.p.rapidapi.com/product-search"
        querystring = {"query":text ,"country":"IN"}
        headers = {
            'x-rapidapi-host': "amazon23.p.rapidapi.com",
            'x-rapidapi-key': "08565f93abmsh46d2e48f99ae72ap1a660ajsnb1138a79da69"
            }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        print(response)
        
        found_amazon = 0
        if "message" in response:
            found_amazon = 0
        
        elif "errors" in response:
            found_amazon = 0
            
        elif response['totalProducts']!=0:
            for i in range(6):
                title = response['result'][i]['title'].lower()
                    
                found_keyword = []
                for keyword in range(len(product_keywords)):
                    if title.find(product_keywords[keyword]) != -1:
                        found_keyword.append(product_keywords[keyword])
                        if found_keyword == product_keywords:
                            found_amazon = 1
                            # discounted = response['result'][i]['price']['discounted']
                            # currency = response['result'][i]['price']['currency']
                            # before_price = response['result'][i]['price']['before_price']
                            # savings_amount = response['result'][i]['price']['savings_amount']
                            # savings_percent = response['result'][i]['price']['savings_percent']
                            current_price = response['result'][i]['price']['current_price']
                            if current_price==0:
                                current_price ="0"
                            product_url = response['result'][i]['url']
                            thumbnail = response['result'][i]['thumbnail']
                            
                            amazon = {
                                # 'discounted' : discounted,
                                # 'before_price' : before_price,
                                # 'savings_amount' : savings_amount,
                                # 'savings_percent' : savings_percent,
                                # 'currency' : currency, 
                                'site_name': 'Amazon',
                                'current_price' : current_price,
                                'product_url' : product_url,
                                'title' : title,
                                'thumbnail' : thumbnail,  
                            }
                            
                            # context = {'1': amazon}
                            # # print(found_keyword," found Product is available")
                            # return render(request,'user/search_result.html', context)
                    break
                        
                if found_amazon == 1:
                    break 
                else:
                    print(found_keyword ," Product NOT-FOUND")
            
        elif (response['totalProducts']==0):
            found_amazon = 0
            
        else:
            found_amazon = 0
                    
        
    # --------------------------------------Flipkart------------------------------------------
        url = "https://www.flipkart.com/search?q="+words+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        value = []
        response = requests.get(url)
        scrapval = bs4.BeautifulSoup(response.text,"html.parser")
        found_flipkart = 0
        if True:
        
        #------------------------For column elements-------------------------------------------------------------        
            for data in scrapval.find_all('div', attrs={"class": "_4rR01T"}):
                tmp = str(data)
                title = tmp[21:-6].lower()
                found_keyword = []
                for keyword in range(len(product_keywords)):
                    if title.find(product_keywords[keyword]) != -1:
                        found_keyword.append(product_keywords[keyword])
                        if found_keyword == product_keywords:
                            found_flipkart = 1
                            
                            current_price = scrapval.find('div', attrs={"class": "_30jeq3 _1_WHN1"})               
                            current_price = str(current_price)[30:-6]
                            current_price = current_price.replace(',', '')
                            if current_price==0:
                                current_price ="0"
                            # current_price = 0
                                
                            thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                            thumbnail = str(thumbnail.get('src'))
                            
                            product_url = scrapval.find('a', attrs={"class": "_1fQZEK"})
                            product_url = str(product_url.get('href'))
                            product_url = "https://www.flipkart.com"+product_url
                            
                            
                            flipkart = {
                                'site_name': 'Flipkart',
                                'current_price' : current_price,
                                'product_url' : product_url,
                                'title' : title,
                                'thumbnail' : thumbnail,  
                            }
                            
                            context = {'1':flipkart}
                            break
                            
                if found_flipkart == 1:
                    break
        
        #------------------------For grid view element-----------------------------------------------------
        if found_flipkart == 0:
            for data in scrapval.find_all('a', attrs={"class": "s1Q9rs"}):
                title = str(data.get('title')).lower()
                # print(title)
                found_keyword = []
                for keyword in range(len(product_keywords)):
                    if title.find(product_keywords[keyword]) != -1:
                        found_keyword.append(product_keywords[keyword])
                        if found_keyword == product_keywords:
                            found_flipkart = 1
                            
                            current_price = scrapval.find('div', attrs={"class": "_30jeq3"})               
                            current_price = str(current_price)[22:-6]
                            current_price = current_price.replace(',', '')
                            if current_price==0:
                                current_price ="0"
                            # print(current_price)
                                
                            thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                            thumbnail = str(thumbnail.get('src'))
                            # print(thumbnail)
                            
                            product_url = scrapval.find('a', attrs={"class": "s1Q9rs"})
                            product_url = str(product_url.get('href'))
                            product_url = "https://www.flipkart.com"+product_url
                            # print(product_url)
                            
                            
                            flipkart = {
                                'site_name': 'Flipkart',
                                'current_price' : current_price,
                                'product_url' : product_url,
                                'title' : title,
                                'thumbnail' : thumbnail,  
                            }
                            
                            context = {'1':flipkart}
                            break
                            
                if found_flipkart == 1:
                    break
        
            
        else:
            found_flipkart=0
            
            
    #------------------------------------Comparing----------------------------------------------    
        if found_amazon==1 and found_flipkart==1:
            if int(amazon['current_price']) <= int(flipkart['current_price']):
                context = {'1':amazon,'2':flipkart}
            elif int(amazon['current_price']) > int(flipkart['current_price']):
                context = {'1':flipkart, '2':amazon}
        elif found_amazon==1 or found_flipkart==1:
            if found_amazon==1:
                context = {'1':amazon}
            elif found_flipkart==1:
                context = {'1':flipkart}
        else:
            context = {'not_found':1}  

        return render(request, 'user/search_result.html', context)


  
# USING WEB SCRAPING (AMAZON AND FLIPKART)
def search_result(request):
    if request.method == "POST":
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        
        words = ''
        for i in product_keywords:
            words = words+"+"+i
        words = words[1:]
        
    #-----------------------------------------------Amazon---------------------------------------------------------------------
        
        value = []
        url = "https://www.amazon.in/s?k="+words+"&ref=nb_sb_noss_2"
        response = requests.get(url)
        scrapval = bs4.BeautifulSoup(response.text,"html.parser")
        found_amazon = 0
        
        #----------------------For column products------------------------    
        if found_amazon == 0:
            for i in range(5):
                response = requests.get(url)
                scrapval = bs4.BeautifulSoup(response.text,"html.parser")
                for data in scrapval.find_all('span', attrs={"class": "a-size-medium a-color-base a-text-normal"}):
                    # print(data)
                    tmp = str(data)
                    title = tmp[55:-7].lower()
                    # print(title)
                    found_keyword = []
                    for keyword in range(len(product_keywords)):
                        if title.find(product_keywords[keyword]) != -1:
                            found_keyword.append(product_keywords[keyword])
                            if found_keyword == product_keywords:
                                found_amazon = 1
                                
                                current_price = scrapval.find('span', attrs={"class": "a-price-whole"}) 
                                current_price = str(current_price)[28:-7]
                                current_price = current_price.replace(',', '')
                                if current_price==0:
                                    current_price ="0"
                                # current_price = 0
                                    
                                thumbnail = scrapval.find('img', attrs={"class": "s-image"})
                                thumbnail = str(thumbnail.get('src'))
                                
                                product_url = scrapval.find('a', attrs={"class": "a-link-normal a-text-normal"})
                                product_url = str(product_url.get('href'))
                                product_url = "https://www.amazon.in"+product_url
                                
                                
                                amazon = {
                                    'site_name': 'Amazon',
                                    'current_price' : current_price,
                                    'product_url' : product_url,
                                    'title' : title,
                                    'thumbnail' : thumbnail,  
                                }
                                
                                context = {'1':amazon}
                                break
                                
                    if found_amazon == 1:
                        break

                if found_amazon == 1:
                        break

        #---------------------For grid products----------------------------
        if found_amazon == 0:
            for i in range(5):
                response = requests.get(url)
                scrapval = bs4.BeautifulSoup(response.text,"html.parser")
                for data in scrapval.find_all('span', attrs={"class": "a-size-base-plus a-color-base a-text-normal"}):
                    # print(data)
                    tmp = str(data)
                    title = tmp[58:-7].lower()
                    # print(title)
                    found_keyword = []
                    for keyword in range(len(product_keywords)):
                        if title.find(product_keywords[keyword]) != -1:
                            found_keyword.append(product_keywords[keyword])
                            if found_keyword == product_keywords:
                                found_amazon = 1
                                
                                current_price = scrapval.find('span', attrs={"class": "a-price-whole"}) 
                                current_price = str(current_price)[28:-7]
                                current_price = current_price.replace(',', '')
                                # print(current_price)
                                if current_price==0:
                                    current_price ="0"
                                    
                                thumbnail = scrapval.find('img', attrs={"class": "s-image"})
                                thumbnail = str(thumbnail.get('src'))
                                # print(thumbnail)
                            
                                
                                product_url = scrapval.find('a', attrs={"class": "a-link-normal a-text-normal"})
                                product_url = str(product_url.get('href'))
                                product_url = "https://www.amazon.in"+product_url
                                # print(product_url)
                                
                                amazon = {
                                    'site_name': 'Amazon',
                                    'current_price' : current_price,
                                    'product_url' : product_url,
                                    'title' : title,
                                    'thumbnail' : thumbnail,  
                                }
                                
                                context = {'1':amazon}
                                break
                                
                    if found_amazon == 1:
                        break

                if found_amazon == 1:
                        break
        
                
    # --------------------------------------Flipkart------------------------------------------
        url = "https://www.flipkart.com/search?q="+words+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        value = []
        for i in range(3):
            response = requests.get(url)
            scrapval = bs4.BeautifulSoup(response.text,"html.parser")
            found_flipkart = 0
            if True:
                
                #------------------------For column elements-------------------------------------------------------------        
                for data in scrapval.find_all('div', attrs={"class": "_4rR01T"}):
                    tmp = str(data)
                    title = tmp[21:-6].lower()
                    # print(title)
                    found_keyword = []
                    for keyword in range(len(product_keywords)):
                        if title.find(product_keywords[keyword]) != -1:
                            found_keyword.append(product_keywords[keyword])
                            if found_keyword == product_keywords:
                                found_flipkart = 1
                                
                                current_price = scrapval.find('div', attrs={"class": "_30jeq3 _1_WHN1"})               
                                current_price = str(current_price)[30:-6]
                                current_price = current_price.replace(',', '')
                                if current_price==0:
                                    current_price ="0"
                                # current_price = 0
                                    
                                thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                                thumbnail = str(thumbnail.get('src'))
                                
                                product_url = scrapval.find('a', attrs={"class": "_1fQZEK"})
                                product_url = str(product_url.get('href'))
                                product_url = "https://www.flipkart.com"+product_url
                                
                                
                                flipkart = {
                                    'site_name': 'Flipkart',
                                    'current_price' : current_price,
                                    'product_url' : product_url,
                                    'title' : title,
                                    'thumbnail' : thumbnail,  
                                }
                                
                                context = {'1':flipkart}
                                break
                                
                    if found_flipkart == 1:
                        break
            
            
                if found_flipkart == 0:
                #------------------------For grid view element-----------------------------------------------------
                    for data in scrapval.find_all('a', attrs={"class": "s1Q9rs"}):
                        title = str(data.get('title')).lower()
                        # print(title)
                        found_keyword = []
                        for keyword in range(len(product_keywords)):
                            if title.find(product_keywords[keyword]) != -1:
                                found_keyword.append(product_keywords[keyword])
                                if found_keyword == product_keywords:
                                    found_flipkart = 1
                                    
                                    current_price = scrapval.find('div', attrs={"class": "_30jeq3"})               
                                    current_price = str(current_price)[22:-6]
                                    current_price = current_price.replace(',', '')
                                    if current_price==0:
                                        current_price ="0"
                                    # print(current_price)
                                        
                                    thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                                    thumbnail = str(thumbnail.get('src'))
                                    # print(thumbnail)
                                    
                                    product_url = scrapval.find('a', attrs={"class": "s1Q9rs"})
                                    product_url = str(product_url.get('href'))
                                    product_url = "https://www.flipkart.com"+product_url
                                    # print(product_url)
                                    
                                    
                                    flipkart = {
                                        'site_name': 'Flipkart',
                                        'current_price' : current_price,
                                        'product_url' : product_url,
                                        'title' : title,
                                        'thumbnail' : thumbnail,  
                                    }
                                    
                                    context = {'1':flipkart}
                                    break
                                    
                        if found_flipkart == 1:
                            break
                
                
                            
            else:
                found_flipkart=0
            
            if found_flipkart==0:
                break
                
            
    #--------------------------------Comparing-------------------------------------------------------------
        if found_amazon==1 and found_flipkart==1:
            if int(amazon['current_price']) <= int(flipkart['current_price']):
                context = {'1':amazon,'2':flipkart}
            elif int(amazon['current_price']) > int(flipkart['current_price']):
                context = {'1':flipkart, '2':amazon}
        elif found_amazon==1 or found_flipkart==1:
            if found_amazon==1:
                context = {'1':amazon}
            elif found_flipkart==1:
                context = {'1':flipkart}
        else:
            context = {'not_found':1}  

    return render(request, 'user/search_result.html', context)

   
# Scraping from flipkart    
def search_resul(request):
    context = {"not_found":"1"}
    if request.method == 'POST':
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        words = ''
        for i in product_keywords:
            words = words+"%20"+i
        words = words[3:]
            
        
        value = []
        url = "https://www.flipkart.com/search?q="+words+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        response = requests.get(url)
        scrapval = bs4.BeautifulSoup(response.text,"html.parser")
        found_flipkart = 0
        
    #------------------------For column elements-------------------------------------------------------------        
        for data in scrapval.find_all('div', attrs={"class": "_4rR01T"}):
            tmp = str(data)
            title = tmp[21:-6].lower()
            found_keyword = []
            for keyword in range(len(product_keywords)):
                if title.find(product_keywords[keyword]) != -1:
                    found_keyword.append(product_keywords[keyword])
                    if found_keyword == product_keywords:
                        found_flipkart = 1
                        
                        current_price = scrapval.find('div', attrs={"class": "_30jeq3 _1_WHN1"})               
                        current_price = str(current_price)[30:-6]
                        current_price = current_price.replace(',', '')
                        if current_price==0:
                            current_price ="0"
                        # current_price = 0
                            
                        thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                        thumbnail = str(thumbnail.get('src'))
                        
                        product_url = scrapval.find('a', attrs={"class": "_1fQZEK"})
                        product_url = str(product_url.get('href'))
                        product_url = "https://www.flipkart.com"+product_url
                        
                        
                        flipkart = {
                            'site_name': 'Flipkart',
                            'current_price' : current_price,
                            'product_url' : product_url,
                            'title' : title,
                            'thumbnail' : thumbnail,  
                        }
                        
                        context = {'1':flipkart}
                        break
                        
            if found_flipkart == 1:
                break
    
    #------------------------For grid view element-----------------------------------------------------
        if found_flipkart == 0:
           for data in scrapval.find_all('a', attrs={"class": "s1Q9rs"}):
            title = str(data.get('title')).lower()
            # print(title)
            found_keyword = []
            for keyword in range(len(product_keywords)):
                if title.find(product_keywords[keyword]) != -1:
                    found_keyword.append(product_keywords[keyword])
                    if found_keyword == product_keywords:
                        found_flipkart = 1
                        
                        current_price = scrapval.find('div', attrs={"class": "_30jeq3"})               
                        current_price = str(current_price)[22:-6]
                        current_price = current_price.replace(',', '')
                        if current_price==0:
                            current_price ="0"
                        # print(current_price)
                            
                        thumbnail = scrapval.find('img', attrs={"class": "_396cs4 _3exPp9"})               
                        thumbnail = str(thumbnail.get('src'))
                        # print(thumbnail)
                        
                        product_url = scrapval.find('a', attrs={"class": "s1Q9rs"})
                        product_url = str(product_url.get('href'))
                        product_url = "https://www.flipkart.com"+product_url
                        # print(product_url)
                        
                        
                        flipkart = {
                            'site_name': 'Flipkart',
                            'current_price' : current_price,
                            'product_url' : product_url,
                            'title' : title,
                            'thumbnail' : thumbnail,  
                        }
                        
                        context = {'1':flipkart}
                        break
                        
            if found_flipkart == 1:
                break
            
    return render(request,'user/search_result.html',context)


# Scraping from amazon   
def search_resul(request):
    context = {'not_found': '1'}
    if request.method == 'POST':
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        words = ''
        for i in product_keywords:
            words = words+"+"+i
        words = words[1:]
            
        
        value = []
        # url = "https://www.amazon.in/s?k="+words
        url = "https://www.amazon.in/s?k="+words+"&ref=nb_sb_noss_1"
        # print(url)
        response = requests.get(url)
        scrapval = bs4.BeautifulSoup(response.text,"html.parser")
        found_amazon = 0
        
    #----------------------For column products------------------------    
        if found_amazon == 0:
            for i in range(5):
                response = requests.get(url)
                scrapval = bs4.BeautifulSoup(response.text,"html.parser")
                for data in scrapval.find_all('span', attrs={"class": "a-size-medium a-color-base a-text-normal"}):
                    # print(data)
                    tmp = str(data)
                    title = tmp[55:-7].lower()
                    print(title)
                    found_keyword = []
                    for keyword in range(len(product_keywords)):
                        if title.find(product_keywords[keyword]) != -1:
                            found_keyword.append(product_keywords[keyword])
                            if found_keyword == product_keywords:
                                found_amazon = 1
                                
                                current_price = scrapval.find('span', attrs={"class": "a-price-whole"}) 
                                current_price = str(current_price)[28:-7]
                                current_price = current_price.replace(',', '')
                                if current_price==0:
                                    current_price ="0"
                                # current_price = 0
                                    
                                thumbnail = scrapval.find('img', attrs={"class": "s-image"})
                                thumbnail = str(thumbnail.get('src'))
                                
                                product_url = scrapval.find('a', attrs={"class": "a-link-normal a-text-normal"})
                                product_url = str(product_url.get('href'))
                                product_url = "https://www.amazon.in"+product_url
                                
                                
                                amazon = {
                                    'site_name': 'Amazon',
                                    'current_price' : current_price,
                                    'product_url' : product_url,
                                    'title' : title,
                                    'thumbnail' : thumbnail,  
                                }
                                
                                context = {'1':amazon}
                                break
                                
                    if found_amazon == 1:
                        break

                if found_amazon == 1:
                        break

    #---------------------For grid products----------------------------
        if found_amazon == 0:
            for i in range(5):
                response = requests.get(url)
                scrapval = bs4.BeautifulSoup(response.text,"html.parser")
                for data in scrapval.find_all('span', attrs={"class": "a-size-base-plus a-color-base a-text-normal"}):
                    # print(data)
                    tmp = str(data)
                    title = tmp[58:-7].lower()
                    # print(title)
                    found_keyword = []
                    for keyword in range(len(product_keywords)):
                        if title.find(product_keywords[keyword]) != -1:
                            found_keyword.append(product_keywords[keyword])
                            if found_keyword == product_keywords:
                                found_amazon = 1
                                
                                current_price = scrapval.find('span', attrs={"class": "a-price-whole"}) 
                                current_price = str(current_price)[28:-7]
                                current_price = current_price.replace(',', '')
                                # print(current_price)
                                if current_price==0:
                                    current_price ="0"
                                    
                                thumbnail = scrapval.find('img', attrs={"class": "s-image"})
                                thumbnail = str(thumbnail.get('src'))
                                # print(thumbnail)
                            
                                
                                product_url = scrapval.find('a', attrs={"class": "a-link-normal a-text-normal"})
                                product_url = str(product_url.get('href'))
                                product_url = "https://www.amazon.in"+product_url
                                # print(product_url)
                                
                                amazon = {
                                    'site_name': 'Amazon',
                                    'current_price' : current_price,
                                    'product_url' : product_url,
                                    'title' : title,
                                    'thumbnail' : thumbnail,  
                                }
                                
                                context = {'1':amazon}
                                break
                                
                    if found_amazon == 1:
                        break

                if found_amazon == 1:
                        break


    return render(request,'user/search_result.html', context)
