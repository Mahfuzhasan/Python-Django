from rest_framework import serializers
from .models import (about_us,news,full,partial,bachalor,masters,phd)



class about__us(serializers.ModelSerializer):
	
	class Meta:
		model = about_us
		

class news_serial(serializers.ModelSerializer):
	
	class Meta:
		model = news	

class full_serial(serializers.ModelSerializer):
	  class Meta:
	  	model = full


class partial_serial(serializers.ModelSerializer):
	  class Meta:
	  	model = partial

class bachalor_serial(serializers.ModelSerializer):
	  class Meta:
	  	model = bachalor

class masters_serial(serializers.ModelSerializer):
	  class Meta:
	  	model = masters

class phd_serial(serializers.ModelSerializer):
	  class Meta:
	  	model = phd	  	
