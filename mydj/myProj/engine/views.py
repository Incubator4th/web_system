from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib import messages
from engine.models import User,Course,Teacher,Report
# Create your views here.

def index(request):
	username = request.COOKIES.get('username','')
	if username:
		user = User.objects.get(username__exact=username)
		realname = user.realname
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			ip = request.META['HTTP_X_FORWARDED_FOR']
		else:
			ip = request.META['REMOTE_ADDR']
		return render(request,'index.html',{'user':user,'ip':ip})
	else:
		return HttpResponseRedirect('/index/login/')



def logout(request):
	response = HttpResponseRedirect('/index/login/')
	response.delete_cookie('username')
	return response



#Regist
def regist(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			User.objects.create(username=username,password=password)
			return HttpResponse('Regist Success')
	else:
			uf=UserForm()
	return render(request,'regist.html',{'uf':uf})



#login
def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		print (request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.filter(username__exact = username,password__exact = password)
			if user:
				response = HttpResponseRedirect('/index/')
				response.set_cookie('username',username,3600)
				return response
			else:
				messages.error(request, 'Username or Password Wrong')
				return	HttpResponseRedirect('/index/login/')

	else:
		uf = UserForm()
	return render(request,'login.html',{'uf':uf})



def welcome(request):
	if 'HTTP_X_FORWARDED_FOR' in request.META:
		ip = request.META['HTTP_X_FORWARDED_FOR']
	else:
		ip = request.META['REMOTE_ADDR']
	return render(request,'welcome.html',{'ip':ip})

def user_password(request):
	username = request.COOKIES.get('username', '')
	if request.method == 'POST':
		pwd = pwd_change(request.POST)
		if pwd.is_valid():
			oldpassword = pwd.cleaned_data['oldpassword']
			newpassword = pwd.cleaned_data['newpassword']
			newpassword2 = pwd.cleaned_data['newpassword2']
			user = User.objects.filter(username__exact = username,password__exact = oldpassword)
			if user:
				if newpassword==newpassword2:
					user.objects.filter.update(password=newpassword)
					response = HttpResponseRedirect('/index/login/')
					response.delete_cookie('username')
					return response
				else:
					messages.error(request, 'The Second input is different')
					return render(request,'user_password.html')
			else:
				messages.error(request, 'Password Error')
				return	HttpResponseRedirect('/index/login/')

	else:
		pwd = pwd_change()
	return render(request,'user_password.html',{'pwd':pwd})

def information(request):
	username = request.COOKIES.get('username', '')
	if username:
		user = User.objects.get(username__exact=username)
		return render(request, 'information.html', {'user': user})
	else:
		return render(request,'information.html')

def course_list(request):
	username = request.COOKIES.get('username', '')
	user = User.objects.get(username__exact=username)
	if user:
		courses = Course.objects.filter()
		teacher = Teacher.objects.filter()
		courses_list={}
		course_num_list={}
		reports = Report.objects.filter(username__exact=user.username)
		for course in courses:
			for report in reports:
				if course.pk != report.courseid.pk:
					courses_list[course.courseid] = course
			report_num = len(Report.objects.filter(courseid__exact=course))
			course_num_list[course.courseid] = report_num
		course_number = len(courses_list)
		if request.method == 'POST':
			for course in courses:
				if course.coursename in request.POST:
					print(course.coursename)
					reports = Report.objects.filter(username__exact=user.username)
					for report in reports:
						if course.pk == report.courseid.pk:
							print ('Had already choosen')
							messages.error(request, 'Had already choosen')
						else:
							Report.objects.create(username=user,courseid=course)
				return render(request, 'course_list.html', {'courses_list': courses_list, 'teacher': teacher,'course_number':course_number,'course_num_list':course_num_list})
		else:
			return render(request, 'course_list.html',{'courses_list':courses_list,'teacher':teacher,'course_number':course_number,'course_num_list':course_num_list})
	else:
		return render(request, 'course_list.html')

def my_course(request):
	username = request.COOKIES.get('username','')
	user = User.objects.get(username__exact=username)
	if user:
		teacher = Teacher.objects.filter()
		courses_list = {}
		course_num_list = {}
		reports = Report.objects.filter(username__exact=user.username)
		for report in reports:
			course = Course.objects.get(courseid__exact=report.courseid)
			courses_list[course.courseid] = course
			report_num = len(Report.objects.filter(courseid__exact=course))
			course_num_list[course.courseid] = report_num
		course_number=len(reports)
		return render(request,'my_course.html',{'courses_list': courses_list, 'teacher': teacher,'reports':reports,'course_number':course_number,'course_num_list':course_num_list})
	else:
		return render(request,'my_course.html')

def upload(request):
	username = request.COOKIES.get('username','')
	user = User.objects.get(username__exact=username)
	if user:
		if request.method =='POST':
			uploadFile = request.FILES.get("uploadFile",None)
			if not uploadFile:
				messages.error(request,'No files for upload')
				return render(request,'upload.html')
		else:
			return render(request,'upload.html')

def test(request):
	courses = Course.objects.filter()
	dicts={}
	for course in courses:
		print (course.coursename)
		dicts[course.courseid]=course
	return render(request,'test.html',{"dicts":dicts,})


class UserForm(forms.Form):
	username = forms.CharField(label='Username',max_length=30)
	password = forms.CharField(label='password',widget=forms.PasswordInput)

class pwd_change(forms.Form):
	oldpassword = forms.CharField(label='oldpassword', widget=forms.PasswordInput)
	newpassword = forms.CharField(label='newpassword', widget=forms.PasswordInput)
	newpassword2 = forms.CharField(label='newpassword2', widget=forms.PasswordInput)




