from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from django.contrib.auth.models import User
from accounts.models import NormalUser,CorporateUser
user_url = HyperlinkedIdentityField(
	view_name='users-api:user_detail',
    lookup_field='id',
	) 
from django.core import serializers
class NormalUsersListSerializer(ModelSerializer):
	user_name = SerializerMethodField()
	url = user_url
	class Meta:
	    model = NormalUser
	    fields = [
	    	'user_name',
	    	'user',
	    	'url',
	        'aadhar_card',

	    ]
	def get_user_name(self,obj):
		user = obj.user.username
		return user
class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
		'id',
		'username',
		'first_name',
		'last_name',
		'email',
		'password',
		]
		write_only_fields = ('password',)
class NormalUsersDetailSerializer(ModelSerializer):
	#user_name = SerializerMethodField()
	user_detail = SerializerMethodField()
	class Meta:
	    model = NormalUser
	    fields = [
	    	'user',
	    	'user_detail',
	        'aadhar_card',
	    ]
	def get_user_detail(self,obj):
		# u =  obj.user
		# context = {'user_name':u.username,
		# 	'first_name':u.first_name,
		# 	'last_name':u.last_name,
		# 	'email':u.email}
		# user_detail = serializers.serialize("json",u)
		# return user_detail
		return UserDetailSerializer(obj.user_detail(),many=True).data
class NormalUserCreateUpdateSerializer(ModelSerializer):
	user_detail = SerializerMethodField()
	class Meta:
	    model = NormalUser
	    fields = [
	        'user',
	        'aadhar_card',
	        'user_detail',
	    ]
	def get_user_detail(self,obj):
		return UserDetailSerializer(obj.user_detail(),many=True).data