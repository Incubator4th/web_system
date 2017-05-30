from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib import messages
from engine.models import User,Course,Teacher,Report


def t_index(request):
	teacherid = request.COOKIES.get('teacherid','')
	print (teacherid)
	if teacherid:
		teacher = Teacher.objects.get(teacherid__exact=teacherid)
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			ip = request.META['HTTP_X_FORWARDED_FOR']
		else:
			ip = request.META['REMOTE_ADDR']
		return render(request,'index.html',{'teacher':teacher,'ip':ip})
	else:
		return HttpResponseRedirect('/index/login/')

def t_logout(request):
	response = HttpResponseRedirect('/index/login/')
	response.delete_cookie('teacherid')
	return response

def t_login(request):
	if request.method == 'POST':
		tf = TeacherForm(request.POST)
		if tf.is_valid():
			teacherid = tf.cleaned_data['teacherid']
			password = tf.cleaned_data['password']
			teacher = Teacher.objects.filter(teacherid__exact = teacherid,password__exact = password)
			if teacher:
				response = HttpResponseRedirect('/t_index/')
				response.set_cookie('teacherid',teacherid,3600)
				return response
			else:
				return	HttpResponseRedirect('/t_login/')
	else:
		tf = TeacherForm()
	return render(request,'t_login.html',{'tf':tf})


class TeacherForm(forms.Form):
	teacherid = forms.CharField(label='teacherid',max_length=30)
	password = forms.CharField(label='password',widget=forms.PasswordInput)