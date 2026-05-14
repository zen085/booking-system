from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Shorter, clearer help text instead of removing completely
        self.fields['username'].help_text = "Required. Letters, digits and @/./+/-/_ only."
        self.fields['password1'].help_text = "At least 8 characters, not too common."
        self.fields['password2'].help_text = "Enter the same password again."

        # Optional: cleaner labels
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'

    # def user_save(self,commit=True):
    #     user = super().save(commit=commit)
    #     if commit:
    #         UserProfile.objects.create(user=user)
    #     return user

