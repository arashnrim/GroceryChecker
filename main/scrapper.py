from urllib.request import Request, urlopen
from requests_html import HTMLSession
from bs4 import BeautifulSoup


prices = []
names = []
units = [] 


def storeSearch(searchString,fairpricePrice,fairpriceUnit):
    fairpricePrice = fairpricePrice[1:]
    #Cold Storage Search
    try:
        lst = [] 
        temp = 0
        sep = "+"
        coldSearch = searchString.split()
        coldSearch = sep.join(coldSearch)
        url = Request('https://coldstorage.com.sg/search?q=' + coldSearch, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        brandName = str()
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        unitFinder = soup.findAll("span", {"class": "size"})
        priceFinder = soup.findAll("div", {"class": "content_price"})
        number = int() 
        price = str() 
        sw = 0
        coldProductName = str()
        temp = str() 
        decimal = str()
        priceFinder = str(priceFinder[0])

        for i in range(0,len(priceFinder)):
            try:
                number = int(priceFinder[i])
                if sw == 1:
                    price += str(number)
                
            except: 
                if priceFinder[i] == "$":
                    sw = 1
                elif priceFinder[i] == "." and sw == 1: 
                    price += priceFinder[i]
                elif priceFinder[i] == "<" and sw == 1:
                    break 
                else: 
                    continue

        brandFinder = soup.findAll("div", {"class": "product_category_name"})
        brandFinder = str(brandFinder[0])
        brand = str()
        for i in range(0,len(brandFinder)):
            try:
                if brandFinder[i] + brandFinder[i+1] + brandFinder[i+2] == "<b>":
                    for i in range(i+3,len(brandFinder)):
                        if brandFinder[i] == "<":
                            break 
                        else: 
                            brand+= brandFinder[i]
            except: 
                break

        nameFinder = soup.findAll("div", {"class": "product_category_name"})
        nameFinder = str(nameFinder[0])
        nameFinder = nameFinder.split()
        exceptions = ['"',",","<",">"]
        name = str()
        nameSw = 0
        for x in nameFinder: 
            nameSw = 0
            for y in x: 
                if y in exceptions:
                    nameSw = 1
            if nameSw == 0: 
                name += x 
                name += " "

        unitFinder = str(unitFinder[0])
        unitFinder = unitFinder.split() 
        unitFinder = unitFinder[-1]
        unit = str()
        for i in range(0,len(unitFinder)):
            if unitFinder[i] == "<":
                break
            else: 
                unit += unitFinder[i]

        coldProductName = brand + " " + name
        coldPrice = price 
        coldProductUnit = unit
    except: 
        coldProductName =  "9999"
        coldPrice = "9999" 
        coldProductUnit = "9999"
    print("Cold searched")
    #Dei Store Search
    try:
        sep = "+"
        deiSearch = searchString.split()
        deiSearch = sep.join(deiSearch)
        product = str()
        session = HTMLSession()
        r = session.get('https://www.dei.com.sg/search?_token=aRkpJ3nCKN5iArm0CpLMEz0gBtxPYF5DyPrk36T6&search='+deiSearch)
        links = r.html.links
        e = [x for x in links]
        for y in e:
            try:
                if y[40]+y[41]+y[42]+y[43]+y[44]+y[45]+y[46]+y[47] == "/product":
                    product = y
                    break
            except:
                continue
        url = Request(product, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        #priceFix = text[2700:]
        #price = priceFix[priceFix.find("$")+1:priceFix.find("/n")]
        priceFinder = soup.findAll("span", {"class": "text-price"})
        priceFinder = str(priceFinder[0])
        priceFinder = priceFinder[10:]
        sw = 0
        price = str()
        for i in range(0,len(priceFinder)):
            if sw == 1: 
                if priceFinder[i] == "<":
                    break
                else: 
                    price+=priceFinder[i]
            elif priceFinder[i] == ">":
                sw = 1
        name = text[9:text.find("|")-1]
        nom = name.split(" - ")
        weight = nom[-1]

        deiPrice = price 
        deiProductName = name
        deiProductWeight = weight
    except:
        deiPrice = "9999"
        deiProductName = "9999"
        deiProductWeight = "9999"
    print("Dei searched")
    #Giant Store Search 
    try:
        sep = "+"
        giantSearch = searchString.split()
        giantSearch = sep.join(giantSearch)
        url = Request("https://giant.sg/search?q="+giantSearch, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        brandName = str()
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()


        number = int() 
        price = str() 
        sw = 0
        coldProductName = str()
        temp = str() 
        decimal = str()
        unitFinder = soup.findAll("span", {"class": "size"})
        priceFinder = soup.findAll("div", {"class": "price_now price-buy price_normal"})
        priceFinder = str(priceFinder[0])

        for i in range(0,len(priceFinder)):
            try:
                number = int(priceFinder[i])
                if sw == 1:
                    price += str(number)
                
            except: 
                if priceFinder[i] == "$":
                    sw = 1
                elif priceFinder[i] == "." and sw == 1: 
                    price += priceFinder[i]
                elif priceFinder[i] == "<" and sw == 1:
                    break 
                else: 
                    continue

        brandFinder = soup.findAll("a", {"class": "to-brand-page"})
        brandFinder = str(brandFinder[0])
        brandFinder = brandFinder[10:]
        brand = str()
        sw = 0
        for i in range(0,len(brandFinder)):
                if sw == 1: 
                    if brandFinder[i] == "<":
                        break
                    else: 
                        brand += brandFinder[i]
                elif brandFinder[i] == ">":
                    sw = 1 
                    


        nameFinder = soup.findAll("a", {"class": "product-link"})
        nameFinder = str(nameFinder[0])
        nameFinder = nameFinder[10:]
        name = str()
        sw = 0
        for i in range(0,len(nameFinder)):
                if sw == 1: 
                    if nameFinder[i] == "<":
                        break
                    else: 
                        name += nameFinder[i]
                elif nameFinder[i] == ">":
                    sw = 1 

        unitFinder = str(unitFinder[0])
        unitFinder = unitFinder.split() 
        unitFinder = unitFinder[-1]
        unit = str()
        for i in range(0,len(unitFinder)):
            if unitFinder[i] == "<":
                break
            else: 
                unit += unitFinder[i]

        giantProductUnit = unit 
        giantProductName = name 
        giantProductPrice = price
    except:
        giantProductUnit = "9999"
        giantProductName = "9999"
        giantProductPrice = "9999"
    print("Giant searched")
    prices.append(coldPrice);prices.append(deiPrice);prices.append(giantProductPrice)
    names.append(coldProductName);names.append(deiProductName);names.append(giantProductName)
    units.append(coldProductUnit);units.append(deiProductWeight);units.append(giantProductUnit)
    
    
    lowest = float(fairpricePrice)
    lowestIndex = 0
    for i in range(0,len(prices)):
        if float(prices[i]) < lowest: 
            lowest = float(prices[i])
            lowestIndex = i 
            
    if units[lowestIndex] == fairpriceUnit:
        if lowestIndex == 0: 
            print("Lowest price is from FairPrice.")
        elif lowestIndex == 1: 
            print("Lowest price is from Cold Storage.")
        elif lowestIndex == 2:
            print("Lowest price is from Dei.")
        elif lowestIndex == 3: 
            print("Lowest price is from Giant.")
    else: 
        del prices[lowestIndex]
        del names[lowestIndex]
        del units[lowestIndex]
        lowest = fairpricePrice
        lowestIndex = 0
        for i in range(0,len(prices)):
            if float(prices[i]) < lowest: 
                lowest = float(prices[i])
                lowestIndex = i 
        
        if units[lowestIndex] == fairpriceUnit:
            if lowestIndex == 0: 
                print("Lowest price is from FairPrice.")
            elif lowestIndex == 1: 
                print("Lowest price is from Cold Storage.")
            elif lowestIndex == 2:
                print("Lowest price is from Dei.")
            elif lowestIndex == 3: 
                print("Lowest price is from Giant.")
        else: 
            del prices[lowestIndex]
            del names[lowestIndex]
            del units[lowestIndex]
        

    return prices,names,units
    

extraLinks = []
session = HTMLSession()
productUnit = ""
while True:
    inp = input("Please input the item that you would like to find. Please be as specific as possible:")
    sep = "%20"
    inp = inp.split()
    inp = sep.join(inp)
    try:
        #Getting links from Fairprice search page 
        r = session.get('https://www.fairprice.com.sg/search?query=' + inp)
        links = r.html.links
        e = [x for x in links]
        for y in e:
            try:
                if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                    product = y
                    break
            except:
                continue
        url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        priceFix = text[700:]
        price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
        for i in range(5,10):
            try: 
                temp = int(price[i])
            except: 
                price = price[0:i]
        productName = text[0:text.find("|")-1]
        unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
        unitFix = str(unitFinder)[133:]
        for i in unitFix:
            if i != "<":
                productUnit += i 
            else: 
                break 
        
        print("\nItem found: {productname} {productunit} {cost}".format(productname = productName, productunit = productUnit, cost = price))
        print("\nIs this the item that you were looking for?")
        inp = input("\nType yes or no:")
        #When item found is correct: 
        if inp == "yes":
            search = productName +" " + productUnit
            try:
                print(storeSearch(search,price,productUnit))
            except:
                print("Sorry, we could not find this item on other stores.")
        #When item found is incorrect, going through other search results in Fairprice search: 
        elif inp == "no":
            print("\nAlright! We'll display the other top 5 search results:")
            for times in range (1,6):
                e.remove(product)
                for y in e:
                    try:
                        if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                            product = y
                            url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
                            page = urlopen(url)
                            productUnit = ""
                            html_bytes = page.read()
                            html = html_bytes.decode("utf-8")
                            soup = BeautifulSoup(html, "html.parser")
                            text = soup.get_text()
                            priceFix = text[700:]
                            price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
                            for i in range(5,10):
                                try: 
                                    temp = int(price[i])
                                except: 
                                    price = price[0:i]
                            productName = text[0:text.find("|")-1]
                            unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
                            unitFix = str(unitFinder)[133:]
                            for i in unitFix:
                                if i != "<":
                                    productUnit += i 
                                else: 
                                    break 

                            extraLinks.append(product)        
                            print("{time}. {productname} {productunit} {cost}".format(time = times, productname = productName, productunit = productUnit, cost = price))
                            break
                    except:
                        continue

            inp = input("\nWhich of these are what you are looking for? Enter 0 if it is none of them, else enter the number of the item:")
            if inp == "0":
                continue
            #Correct item found 
            else:
                url = Request('https://www.fairprice.com.sg' + extraLinks[int(inp)-1], headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(url)
                productUnit = ""
                html_bytes = page.read()
                html = html_bytes.decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text()
                priceFix = text[700:]
                price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
                for i in range(5,10):
                    try: 
                        temp = int(price[i])
                    except: 
                        price = price[0:i]
                productName = text[0:text.find("|")-1]
                unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
                unitFix = str(unitFinder)[133:]
                for i in unitFix:
                    if i != "<":
                        productUnit += i 
                    else: 
                        break
                search = productName +" " + productUnit
                try:
                    print(storeSearch(search,price,productUnit))
                except: 
                    print("Sorry, we could not find that item in other stores.")
                
                          
    except:
        print("\nSorry, we are not able to find that item. Please enter a different item or name.")
        continue

