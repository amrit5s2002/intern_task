from django.shortcuts import render
from .models import *
# Create your views here.
def search(request):
    print("test")
    # print(type(items))
    if request.method == 'GET':
        query= request.GET.get('q')
        if not query :
            query = ""
        submitbutton= request.GET.get('submit')
        print(submitbutton)
        print(query)
        if query is not None:
            print('not null')
            items = Task.objects.filter(item__icontains=query)
            print(items)
            return render(request,'search_list.html',{'items':items,'submitbutton':submitbutton})
        else:
            message_null = "please type item to search"
            return render(request,'search_list.html',{'message_null':message_null})
    else:
        return render(request,'search_list.html')
    
    
    
def random(request):
    if request.method == 'POST':
        addlistbutton= request.GET.get('random')
        print(addlistbutton)
        return render(request,'search_list.html')