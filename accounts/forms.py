from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = (
			"username",
			"email",
			"age",)

	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = None

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = (
			"username",
			"email",
			"age",
			)