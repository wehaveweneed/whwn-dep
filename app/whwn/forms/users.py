from django import forms
from registration.forms import RegistrationFormUniqueEmail
from whwn.models import UserProfile
from whwn.models import Team

class NewUserRegistrationForm(RegistrationFormUniqueEmail):
    join_team = forms.ModelChoiceField(queryset=Team.objects.all(), required=False)
    new_team = forms.CharField(label=u"Start a team", required=False)
    def clean(self):
        cleaned_data = super(NewUserRegistrationForm, self).clean()
        if not cleaned_data.get("join_team") and not cleaned_data.get("new_team"):
            raise forms.ValidationError("You must either create or join a team")
        if cleaned_data.get("join_team") and cleaned_data.get("new_team"):
            raise forms.ValidationError("If you are joining a team, you cannot also\
                    create a team")
        return cleaned_data
