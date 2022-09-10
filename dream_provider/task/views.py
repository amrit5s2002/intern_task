from django.shortcuts import render
from .models import *
import string    
import random
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
            # print('not null')
            items = Task.objects.filter(item__icontains=query)
            # print(items)
            return render(request,'search_list.html',{'items':items,'submitbutton':submitbutton})
        else:
            message_null = "please type item to search"
            return render(request,'search_list.html',{'message_null':message_null})
    else:
        return render(request,'search_list.html')
    

    
def ran(request):
    word = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase ,k = 10))  
    # print(word)
    item_query = Task(item = word )
    item_query.save()
    return render(request,'random.html',{'item':word})