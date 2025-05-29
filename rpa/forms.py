from .models import Answers, BusinessUnit, Process, BusinessUnitManagers, User
from django.forms import ModelForm
from django import forms


class AnswerForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TimeSheetsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Answers

        fields = '__all__'
        widgets = {
            'process': forms.HiddenInput(),
            'created_date': forms.HiddenInput(),
            'last_updated': forms.HiddenInput(),
            'Qone': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qtwo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qthree': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qfour': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qfive': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qsix': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qseven': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qeight': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qnine': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qten': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qeleven': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qtwelve': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qthirteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qfourteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qfifteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qsixteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qseventeen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qeighteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qnineteen': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qtwenty': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'Qtwentyone': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),

        }



class BusinessUnitForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TimeSheetsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BusinessUnit

        fields = '__all__'
        widgets = {
            'created_date': forms.HiddenInput(),
            'last_updated': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'head': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ProcessForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TimeSheetsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Process

        fields = {'business_unit', 'created_date','last_updated','name','head'}
        widgets = {
            'business_unit': forms.HiddenInput(),
            'created_date': forms.HiddenInput(),
            'last_updated': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'head': forms.TextInput(attrs={'class': 'form-control'}),

        }

class ProcessConfigForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TimeSheetsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Process

        fields = '__all__'
        widgets = {
            'business_unit': forms.HiddenInput(),
            'created_date': forms.HiddenInput(),
            'last_updated': forms.HiddenInput(),
            'name': forms.HiddenInput(),
            'head': forms.HiddenInput(),
            'recurrence': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'trigger': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'day': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'criticality': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'impact_if_failed': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'impact_if_late': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'impact_of_time_overun': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'late_tolerance': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'time_dependencies': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'wait_until_time': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'complete_by_time': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'complexity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'understanding': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'optimised': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'stable': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'documentation': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'customer_facing': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'regulated': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'self_contained': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'errors': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),
            'manual_intervention': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please fill this in'}),


        }

class BusinessUnitManagersForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Add widget
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),  # Add widget
        required=True
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})  # Add widget
    )

    class Meta:
        model = BusinessUnitManagers
        fields = '__all__'
        widgets = {'business_unit': forms.HiddenInput(),
                   'assigned': forms.HiddenInput(),
                   'user': forms.HiddenInput(),
                   'name': forms.TextInput(attrs={'class': 'form-control'}),}

    def __init__(self, *args, **kwargs):
        self.site_instance = kwargs.pop('site_instance', None)
        super().__init__(*args, **kwargs)

        if self.site_instance:
            self.fields['business_unit'].initial = self.site_instance

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        site_manager = super().save(commit=False)
        site_manager.user = user
        if commit:
            site_manager.save()
            self.save_m2m()
        return site_manager