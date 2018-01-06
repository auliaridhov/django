from django.shortcuts import render
def index(request):
	return render(request,'PROJECT/home.html')

def contact(request):
	return render(request,'PROJECT/basic.html',{'content':['if you like to contact me, please email','liburankuhilang']})

def halamanke2(request):
    return render(request,'PROJECT/halamanke2.html')

def about(request):
    return render(request,'PROJECT/about.html')

def offlane(request):
    return render(request,'PROJECT/offlane.html')

def midlane(request):
    return render(request,'PROJECT/midlane.html')

def safelane(request):
    return render(request,'PROJECT/safelane.html')
