from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1 = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
source2 = "https://www.amazon.in/Apple-iPhone-Xs-Max-64GB/dp/B07J3CJM4N/ref=sr_1_4?dchild=1&keywords=Apple+iPhone+XS+%28Space+Grey%2C+64+GB%29&qid=1584873760&s=electronics&sr=1-4"
source3 = "https://www.croma.com/apple-iphone-xs-space-grey-64-gb-4-gb-ram-/p/214062"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(
    r'D:\Learning\Practice\Selenium\chromedriver.exe', options=CO)
print("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")

print("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath(
    "/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element_by_xpath(
    "/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print(" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
a_price = wd.find_element_by_xpath(
    "/html/body/div[4]/div[2]/div[4]/div[10]/div[12]/div/table/tbody/tr[2]/td[2]/span[1]")
raw_p = a_price.text
# print (raw_p[2:8])
print(" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element_by_xpath(
    "/html/body/main/div[5]/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/span")
raw_c = c_price.text
# print (raw_c[1:7])
print(" ---> Successfully retrieved the price from Croma\n")
time.sleep(2)

# Final display
print("#------------------------------------------------------------------------#")
print("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
print("  Price available at Amazon is: "+raw_p[2:8])
print("   Price available at Croma is: "+raw_c[1:7])


<a class = "_1fQZEK" href = "/apple-iphone-12-white-128-gb/p/itm95393f4c6cc59?pid=MOBFWBYZBTZFGJF9&amp;lid=LSTMOBFWBYZBTZFGJF9AXUVLJ&amp;marketplace=FLIPKART&amp;q=iphone+12+128+gb&amp;store=tyy%2F4io&amp;srno=s_1_1&amp;otracker=search&amp;otracker1=search&amp;fm=organic&amp;iid=c0df7668-208a-47a4-be6f-91205d4e5cf5.MOBFWBYZBTZFGJF9.SEARCH&amp;ppt=None&amp;ppn=None&amp;ssid=zn0mq1a0y80000001632665579670&amp;qH=8bf7b28661f9b1ca" rel = "noopener noreferrer" target = "_blank" >



<div class = "MIXNux" > <div class = "_2QcLo-" > <div > <div class = "CXW8mj" style = "height:200px;width:200px" > <img alt = "APPLE iPhone 12 (White, 128 GB)" class = "_396cs4 _3exPp9" src = "https://rukminim1.flixcart.com/image/312/312/kg8avm80/mobile/j/f/9/apple-iphone-12-dummyapplefsn-original-imafwg8dhe5aeyhk.jpeg?q=70"/> < /div > </div > </div > 

<div class = "_3wLduG" > <div class = "_3PzNI-" > <span class = "f3A4_V" > <label class = "_2iDkf8" > <input class = "_30VH1S" readonly = "" type = "checkbox"/> < div class = "_24_Dny" > </div > </label > </span > <label class = "_6Up2sF" > <span > Add to Compare < /span > </label > </div > </div > <div class = "_2hVSre _3nq8ih" > <div class = "_36FSn5" > <svg class = "_1l0elc" height = "16" viewbox = "0 0 20 16" width = "16" xmlns = "http://www.w3.org/2000/svg" > <path class = "eX72wL" d ="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484


# 2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"></path></svg></div></div></div>



<div class="_3pLy-c row"><div class="col col-7-12"><div class="_4rR01T">APPLE iPhone 12 (White, 128 GB)</div><div class="gUuXy-"><span class="_1lRcqv" id="productRating_LSTMOBFWBYZBTZFGJF9AXUVLJ_MOBFWBYZBTZFGJF9_"><div class="_3LWZlK">4.6<img class="_1wB99o" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/></div></span><span class="_2_R_DZ"><span><span>12,363 Ratings </span><span class="_13vcmD">&amp;</span><span> 1,080 Reviews</span></span></span></div><div class="fMghEO"><ul class="_1xgFaf"><li class="rgWa7D">128 GB ROM</li><li class="rgWa7D">15.49 cm (6.1 inch) Super Retina XDR Display</li><li class="rgWa7D">12MP + 12MP |
1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="
12MP Front Camera < /li > <li class = "rgWa7D" > A14 Bionic Chip with Next Generation Neural Engine Processor < /li > <li class = "rgWa7D" > Ceramic
Shield < /li > <li class = "rgWa7D" > Industry-leading IP68 Water Resistance < /li > <li class = "rgWa7D" > All Screen OLED Display < /li > <li class = "rgWa7D" > 12MP TrueDepth Front Camera with Night Mode, 4K Dolby Vision HDR Recording < /li > <li class = "rgWa7D" > Brand Warranty for 1 Year < /li > </ul > </div > </div > <div class = "col col-5-12 nlI3QM" > <div class = "_3tbKJL" > <div class = "_25b18c" > <div class = "_30jeq3 _1_WHN1" >₹69, 149 < /div > <div class = "_3I9_wc _27UcVY" >₹<!-- - -> 70, 900 < /div > <div class = "_3Ay6Sb" > <span > 2 % off < /span > </div > </div > </div > <div class = "_13J9qT" > <img height = "21" src = "//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/fa_62673a.png"/> < /div > <div class = "_2ZdXDB" > <div class = "_3xFhiH" > <div class = "_2Tpdn3 _18hQoS" style = "color:#000000;font-size:14px;font-style:normal;font-weight:400" > Upto < /div > <div class = "_2Tpdn3 _18hQoS" style = "color:#000000;font-size:14px;font-style:normal;font-weight:700" >₹15, 000 < /div > <div class = "_2Tpdn3 _18hQoS" style = "color:#000000;font-size:14px;font-style:normal;font-weight:400" > Off on Exchange < /div > </div > </div > </div > </div > </a >
