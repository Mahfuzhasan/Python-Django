from django.db import models





class news(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=500)
	def __str__(self):
	   return	self.title

class about_us(models.Model):
	us=models.CharField(max_length=600)





class full(models.Model):
	facilities=models.CharField(max_length=500)
	conditions=models.CharField(max_length=600)



class partial(models.Model):
	major =  models.CharField(max_length=400)
	facilities  =  models.CharField(max_length=500)
	conditions  =  models.CharField(max_length=600)






class bachalor(models.Model):
      sub =  models.CharField(max_length=400)
      def __str__(self):
      	return self.sub

class masters(models.Model):
      sub =  models.CharField(max_length=400)
      def __str__(self):
      	return self.sub


class phd(models.Model):
      sub =  models.CharField(max_length=400)
      def __str__(self):
      	return self.sub


	  
		
	   
