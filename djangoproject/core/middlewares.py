from exceptions import BaseException
from django.shortcuts import redirect
from django.contrib import messages

class CompleteRegistrationFirst:
	def process_request(self, request):
		if(request.user.is_authenticated()):
			if(request.path in ['/core/user/edit', '/core/user/edit/submit']):
				return None
			user = request.user
			if(user.is_registration_complete()):
				return None
			else:
				messages.info(request, 'Please complete your profile before proceeding.')
				return redirect('/core/user/edit?next='+request.get_full_path())
		else:
			return None


