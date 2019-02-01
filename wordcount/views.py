from django.http import HttpResponse
from django.shortcuts import render

def  homepage(request):
    return render(request, "first.html")

def  count(request):
    data=request.GET['fulltextarea']
    word_list = data.split()
    len_word_list=len(word_list)

    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            #increase value by 1
            worddictionary[word] +=1
        else:
            # add to the worddictionary and set value to 1
            worddictionary[word] =1
    return render(request, 'count.html',{'textarea':data ,'words':len_word_list,'worddict':worddictionary})


def about(request):
    return render(request,"about.html")


def validation(request):
    return render(request, "fvalidation.html")

def mywebsite(request):
    return render(request, "shubh.html")