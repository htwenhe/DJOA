from django.shortcuts import render

# Create your views here.
def thanks(request,):
    return render(request,'thanks.html',{
        'name':'wenhe',
        'sex':'男'
    })
