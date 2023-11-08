from django.shortcuts import render, HttpResponse
from .forms import UserInfoForm


# Create your views here.

# def user_info_form(request):
#     if request.method == 'POST':
#         form = UserInfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = UserInfoForm()
#     return  render(request, 'user_info/user_info_form.html', {'form': form})

# def success(request):
#     return render(request, 'user_info/success.html')

def home(request):
    context = {
        'variable1': 'Hello World learn Django',
        'variable2': 'Hello World learn Devops'

    }
    return render(request,'index.html',context)
    # return HttpResponse('This is Home page')

def about(request):
    return HttpResponse('This is about page')

def services(request):
    return HttpResponse('This is services page')

def contact(request):
    return HttpResponse('This is contact page')
