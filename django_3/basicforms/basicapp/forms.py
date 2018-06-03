from django import forms
from django.core import validators
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo





class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())


	class Meta():
		model=User
		fields=('username','email','password')


class FormProfileInfo(forms.ModelForm):
	class Meta():
		model=UserProfileInfo
		fields=('portfolio_site','profile_pic')



















# class FormName(forms.Form):
# 	name=forms.CharField()
# 	email=forms.EmailField()
# 	verify_email=forms.EmailField(label='Enter email again')
# 	text=forms.CharField(widget=forms.Textarea)
# 	botcatcher=forms.CharField(required=False,
# 								widget=forms.HiddenInput,
# 								validators=[validators.MaxLengthValidator(0)])


# 	def clean(self):
# 		all_cleaned_data=super().clean()
# 		email=all_cleaned_data['email']
# 		vmail=all_cleaned_data['verify_email']
# 		if email!=vmail:
# 			raise forms.ValidationError('Make sure emails are same')
		















# def check_z(value): this creates a custom validator
# 	if value[0].lower()!='z':
# 		raise forms.ValidationError('Name Needs to start with Z.')




	# def clean_botcatcher(self): # manual check no need as validators present.
	# 	botcatcher=self.cleaned_data['botcatcher']
	# 	if len(botcatcher)>0:
	# 		raise forms.ValidationError('got you bot')
