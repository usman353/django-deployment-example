from django.shortcuts import render
from basicapp.forms import FormProfileInfo,UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
	return render(request,'basicapp/index.html')

@login_required
def special(request):
	return HttpResponse('You are logged in')


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def register(request):

	registered=False

	if request.method== 'POST':
		user_form=UserForm(data=request.POST)
		profile_form=FormProfileInfo(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user


			if 'profile_pic' in request.FILES:

				profile.profile_pic=request.FILES['profile_pic']



			profile.save()
			registered=True
		else:
			print(user_form.errors,profile_form.errors)
		

	    

	        # One of the forms was invalid if this else gets called.
	        

	else:
	    # Was not an HTTP post so we just render the forms as blank.
	    user_form = UserForm()
	    profile_form = FormProfileInfo()

	# This is the render and context dictionary to feed
	# back to the registration.html file page.
	return render(request,'basicapp/registration.html',
	                      {'user_form':user_form,
	                       'profile_form':profile_form,
	                       'registered':registered})




def user_login(request):
	
	if request.method=='POST':
		username=request.POST.get('username') # from html name password
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse('Account not active')


		else:
			print('Someone tried to login but Failed!!')
			print('Username:{} and password {}'.format(username,password))
			return HttpResponse('invalid login parameters provided')

	else:
		return render(request,'basicapp/login.html',{})
				




















# def form_name_view(request):
# 	form=forms.FormName()
	

# 	if request.method=='POST':
# 		form=forms.FormName(request.POST)

# 		if form.is_valid():
# 			print('validation success')
# 			print('NAME :' +form.cleaned_data['name'])
# 			print('EMAIL :' +form.cleaned_data['email'])
# 			print('TEXT :' +form.cleaned_data['text'])

# 	return render(request,'basicapp/form_page.html',{'form':form})