# Using Rapid Api
def search1(request):
    if request.method == "POST":
        text = request.POST['search_bar']
        product_keywords = text.split(' ')
        print(product_keywords)

    url = "https://amazon23.p.rapidapi.com/product-search"
    querystring = {"query":text ,"country":"IN"}
    headers = {
        'x-rapidapi-host': "amazon23.p.rapidapi.com",
        'x-rapidapi-key': "08565f93abmsh46d2e48f99ae72ap1a660ajsnb1138a79da69"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    found=0
    for i in range(5):
        title = response['search_results'][i]['title'].lower()
            
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
