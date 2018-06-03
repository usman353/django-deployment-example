from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import UserForm
# Create your views here.

def index(request):
	context_dict={'text':'hello world','number':100}
	return render(request,'apptwo/index.html',context=context_dict)
    

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'apptwo/users.html',context=user_dict)

def form_view(request):
	us_form=UserForm()

	if request.method=='POST':
		us_form=UserForm(request.POST)
		if us_form.is_valid():			
			print('validation success')
			print('Fst_NAME :' +us_form.cleaned_data['first_name'])
			print('Lst_NAME :' +us_form.cleaned_data['last_name'])
			print('EMAIL :' +us_form.cleaned_data['email'])
			us_form.save(commit=True)
			return users(request)
		else:
			print('Error in form ')

	return render(request,'appTwo/form_page.html',{'form':us_form})

def relative(request):
	return render(request,'appTwo/relative_url_temp.html')