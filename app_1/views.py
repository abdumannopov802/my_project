from django.shortcuts import render
from django.views.generic import TemplateView   # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Create your views here.

class HomePageView(TemplateView):
    # def table(request):
        # table_base = ['id', 'Name', 'E-mail', 'Investment', 'Action']
        template_name = 'home.html'
        # return template_name
    

class secondHomePageView(TemplateView):
    template_name = 'about.html'

class newsPageView(TemplateView):
    template_name = 'news.html'

class imagesPageView(TemplateView):
    template_name = 'images.html'

class Admin(TemplateView):
    template_name = 'admin.html'

class PostDetaliView(TemplateView):
     template_name = 'postdetails.html'

class NewTableView(TemplateView):
     template_name = 'index.html'



from django.http import HttpResponse, HttpRequest
def HomeworkTable(request):
    # print(str(request))
    context = {"123":("Alfred Alan", "aalan@gmail.com", "Stock",''),
            "321":("Alison Smart", "asmart@biztalk.com", "Residential Property",''),
            "213":("Elly Emery", "andyp@mycorp.com", "Stock",''),
            "231":("Andrew Phips", "bdnb@albert.net", "Bonds",''),
            "436":("Alfred Alan", "aalan@gmail.com", "Stock",''),
            "784":("Alison Smart", "asmart@biztalk.com", "Residential Property",''),
            "269":("Elly Emery", "andyp@mycorp.com", "Stock",''),
            "163":("Andrew Phips", "bdnb@albert.net", "Bonds",''),"123":("Alfred Alan", "aalan@gmail.com", "Stock",''),
            "243":("Alison Smart", "asmart@biztalk.com", "Residential Property",''),
            "673":("Elly Emery", "andyp@mycorp.com", "Stock",''),
            "563":("Andrew Phips", "bdnb@albert.net", "Bonds",''),}
    
    return render(request=request, template_name='table.html', context={'context':context})

# def mssview(request):
#     return render(request=request, template_name='detail.html', context={})

def test(request):
    test = 'some text'
    return render(request=request, template_name='test.html', context={'test':test})


def test2(request):
    dictionary = {'4 gacha': [1, 2, 3],
                   '7 gacha': [4, 5, 6],
                   '10 gacha': [7, 8, 9]}
    return render(request=request, template_name='test.html', context={'dict':dictionary})

