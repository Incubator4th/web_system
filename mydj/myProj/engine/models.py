from django.db import models

# Create your models here.
SEX_CHOICES = (
    ('0','Male'),
    ('1','Female'),
)

class User(models.Model):
	username = models.CharField(db_column=r'Student_ID',primary_key=True,max_length=30)
	password = models.CharField(db_column=r'password',max_length=30)
	realname = models.CharField(db_column=r'Student_Name',max_length=10, default='Unknown')
	userPhone= models.IntegerField(db_column=r'Student_Phone',default="")
	usersex  = models.CharField(db_column=r'Student_Sex',choices = SEX_CHOICES,max_length = 1,default='Unknown')
	email = models.EmailField(db_column=r'Email',default='blank')
	
	def __str__(self):
		return self.username
class Teacher(models.Model):
	teacherid = models.CharField(db_column=r'Teacher_ID',primary_key=True,max_length=30)
	password = models.CharField(db_column=r'password',max_length=30)
	teachername = models.CharField(db_column=r'Teacher_Name',max_length=30)

	def __str__(self):
		return self.teacherid

class Course(models.Model):
	courseid = models.CharField(db_column=r'Course_Id',primary_key=True,max_length=10,default='Unknown')
	coursename = models.CharField(db_column=r'Course_Name',max_length=30)
	coursetime = models.DateTimeField(db_column=r'Course_Time')
	coursenum = models.IntegerField(db_column=r'Course_Max_Number',default=0)
	courseinfo =models.CharField(db_column=r'Course_Information',max_length=512,default='Unknown')
	teacherid = models.ForeignKey(Teacher)

	def __str__(self):
		return self.courseid

class Report(models.Model):
	username = models.ForeignKey(User)
	courseid = models.ForeignKey(Course)
	score = models.IntegerField(db_column=r'Report_Score',default=60)

	def __str__(self):
		return self.reportid
