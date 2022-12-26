from django.shortcuts import render
from .models import person
from .models import ortak
from django.db.models import Q

marka_liste = ["Asus","HP","Lenovo","Apple","Dell","Acer","Hometech","Technopc","Fujitsu","Huawei","MSI","Casper","Monster","İXtech","HONOR"]

marka_listev2 = ["Asus","HP","Lenovo","Apple","Dell","Acer","Hometech","Technopc","Fujitsu","Huawei","MSI","Casper","Monster","İXtech","HONOR"]

islemci_liste = ["Intel Core i5 10210U","AMD Ryzen 7 5800H","AMD Ryzen 5 5600U",

                "Intel Core i3 1115G4","Apple M1 Apple M1","Intel Core i5 1135G7",

                "Intel Celeron N4020","Intel Core i5 1235U","AMD Ryzen 5 4600H",

                "Intel Core i3 7020U","Intel Core i5 9300H","AMD Ryzen 7 5800HS",

                "Intel Pentium N3710","Intel Core i7 12650H","Intel Core i7 1255U",
                
                "Intel Core i7 1165G7","Intel Core i5 1035G1","Intel Core i5 11400H",
                
                "Intel Celeron N4000","AMD Ryzen 5 4600H","Intel Core i5 12450H",

                "AMD Ryzen 7 5700U","Intel Core i7 11800H","AMD Ryzen 9 5900HX",

                "Intel Core i7 1280P","Intel Core i7 12700H","Apple M2 Apple M2"]

islemci_listev2 = ["Intel Core i5 10210U","AMD Ryzen 7 5800H","AMD Ryzen 5 5600U",

                "Intel Core i3 1115G4","Apple M1 Apple M1","Intel Core i5 1135G7",

                "Intel Celeron N4020","Intel Core i5 1235U","AMD Ryzen 5 4600H",

                "Intel Core i3 7020U","Intel Core i5 9300H","AMD Ryzen 7 5800HS",

                "Intel Pentium N3710","Intel Core i7 12650H","Intel Core i7 1255U",
                
                "Intel Core i7 1165G7","Intel Core i5 1035G1","Intel Core i5 11400H",
                
                "Intel Celeron N4000","AMD Ryzen 5 4600H","Intel Core i5 12450H",

                "AMD Ryzen 7 5700U","Intel Core i7 11800H","AMD Ryzen 9 5900HX",

                "Intel Core i7 1280P","Intel Core i7 12700H","Apple M2 Apple M2"]

os_liste = ["Windows 11 Home","Ubuntu","Windows 10 Pro","Windows 10 Home","FreeDos","Linux","macOS","Windows 11 Pro"]

os_listev2 = ["Windows 11 Home","Ubuntu","Windows 10 Pro","Windows 10 Home","FreeDos","Linux","macOS","Windows 11 Pro"]

size_liste = ["15,6 inç","14 inç","17,3 inç","14,1 inç","13,3 inç","16,1 inç","13 inç","16 inç"]

size_listev2 = ["15,6 inç","14 inç","17,3 inç","14,1 inç","13,3 inç","16,1 inç","13 inç","16 inç"]

site_liste = ["Hepsiburada","N11","Trendyol"]

site_listev2 = ["Hepsiburada","N11","Trendyol"]

def site_search_view(request):
    query_dict = request.GET
    try:
        query = query_dict.get("query")
        print(query)
        # i = 0
        # a = 1
        # bosluk_listesi = []
        # aranan_listesi = []
        # for a in range(len(query)):
        # if query.find(" ",i,len(query)) != -1 :
        #     bosluk_listesi.append(query.find(" ",i,len(query)))
        #     i = query.find(" ",i,len(query)) + 1
        #     a = a + 1
        # else:
        #     break
        
        # for k in range(len(bosluk_listesi) + 1):
        # if k == 0:
        #     aranan_listesi.append(query[0:bosluk_listesi[k]])
        # elif k != len(bosluk_listesi):
        #     aranan_listesi.append(query[bosluk_listesi[k-1] + 1:bosluk_listesi[k]])
        # else:  
        #     aranan_listesi.append(query[bosluk_listesi[k-1] + 1:])
    except:
        query = None

    persons = None 
    if query is not None:
        persons = person.objects.filter(Baslik__icontains = query)

    context = {
        "Markalar" : marka_liste,
        "Islemciler" : islemci_liste,
        "Osler" : os_liste,
        "Sizeler" : size_liste,
        "Siteler" : site_liste,
        "Laptoplar": persons
    }
    return render(request, "search.html", context=context)

def site_msearch_view(request):
    query_dict = request.GET
    try:
        query = query_dict.get("query")
        print(query)
    except:
        query = None

    persons = None 
    if query is not None:
        ortaks = ortak.objects.filter(Baslik__icontains = query)

    context = {
        "Markalar" : marka_liste,
        "Laptoplar": ortaks
    }
    return render(request, "msearch.html", context=context)    

def home(request):
    persons = person.objects.all()
    data = {
        "Markalar" : marka_liste,
        "Islemciler" : islemci_liste,
        "Osler" : os_liste,
        "Sizeler" : size_liste,
        "Siteler" : site_liste,
        "Laptoplar": persons
    }
    return render(request, "index.html", data)

def mahone(request):
    ortaks = ortak.objects.all()
    data = {
        "Markalar" : marka_liste,
        "Islemciler" : islemci_liste,
        "Osler" : os_liste,
        "Sizeler" : size_liste,
        "Laptoplar": ortaks
    }
    return render(request, "mahone.html", data)    

def laptop_details(request, id):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "id": id
    }
    return render(request, "details.html", data)

def mahone_details(request, id):
    ortaks = ortak.objects.all()
    data = {
        "Laptoplar": ortaks,
        "id": id
    }
    return render(request, "mahone_details.html", data)

def Mmarka_listesi(request, marka_liste):
    ortaks = ortak.objects.all()
    data = {
        "Laptoplar": ortaks,
        "Markalar": marka_liste,
        "marka_liste": marka_listev2
    }
    return render(request, "mmarka.html", data)

def ascsorted(request):
    persons = person.objects.all()
    sorted_persons_price_asc = person.objects.order_by('-Fiyat')

    data= {'sortedpriceasc': sorted_persons_price_asc,
            "Markalar" : marka_liste,
            "Osler" : os_liste,
            "Sizeler" : size_liste,
            "Siteler" : site_liste,
            "Islemciler" : islemci_liste}
    
    return render(request, 'ascsorted.html', data)

def descsorted(request):
    persons = person.objects.all()
    sorted_persons_price_desc = person.objects.order_by('Fiyat')
    
    data= {'sortedpricedesc': sorted_persons_price_desc,
            "Markalar" : marka_liste,
            "Osler" : os_liste,
            "Sizeler" : size_liste,
            "Siteler" : site_liste,
            "Islemciler" : islemci_liste}
    
    return render(request, 'descsorted.html', data)

def puan(request):
    persons = person.objects.all()
    sorted_puan = person.objects.order_by('-Puan')
    
    data= {'sortedpuan': sorted_puan,
            "Markalar" : marka_liste,
            "Osler" : os_liste,
            "Sizeler" : size_liste,
            "Siteler" : site_liste,
            "Islemciler" : islemci_liste}
    
    return render(request, 'puan.html', data)
   
def Marka_listesi(request, marka_liste):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "Osler" : os_liste,
        "Markalar": marka_liste,
        "Sizeler" : size_liste,
        "marka_liste": marka_listev2,
        "Siteler" : site_liste,
        "Islemciler" : islemci_liste
    }
    return render(request, "markalar.html", data)    

def Islemci_listesi(request, islemci_liste):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "Osler" : os_liste,
        "Markalar": marka_liste,
        "Sizeler" : size_liste,
        "Islemciler" : islemci_liste,
        "Siteler" : site_liste,
        "islemci_liste" : islemci_listev2
    }
    return render(request, "islemciler.html", data)

def Os_listesi(request, os_liste):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "Markalar": marka_liste,
        "Islemciler" : islemci_liste,
        "Sizeler" : size_liste,
        "Osler" : os_liste,
        "Siteler" : site_liste,
        "os_liste" : os_listev2,
    }
    return render(request, "osler.html", data)    

def Size_liste(request, size_liste):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "Markalar": marka_liste,
        "Islemciler" : islemci_liste,
        "Osler" : os_liste,
        "Sizeler" : size_liste,
        "Siteler" : site_liste,
        "size_liste" : size_listev2,
    }
    return render(request, "sizeler.html", data)  

def Site_liste(request, site_liste):
    persons = person.objects.all()
    data = {
        "Laptoplar": persons,
        "Markalar": marka_liste,
        "Islemciler" : islemci_liste,
        "Osler" : os_liste,
        "Sizeler" : size_liste,
        "Siteler" : site_liste,
        "site_liste" : site_listev2
    }
    return render(request, "siteler.html", data)        