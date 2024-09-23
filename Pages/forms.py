from Account.models import UserAccount
from django import forms


class UserAccountForm(forms.ModelForm):
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  class Meta:
      model = UserAccount
      fields = ['first_name', 'last_name', 'email', 'company', 'password']
  
  def save(self, commit=True):
        # Save the provided password in hashed format

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user