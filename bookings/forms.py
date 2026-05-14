from django  import forms
from .models import Order
from . import helper


class BookingOrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','email','phone','date','time','notes']
        # widget = {
        #     'date':forms.DateInput(attrs={'type':'date'})
        # }
    
    # def __init__(self, *args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['date'].widget = forms.HiddenInput()
    #     self.fields['time'].widget = forms.HiddenInput()

    def clean_name(self):
        return helper.name_logic(self.cleaned_data.get('name'))
    
    def clean_email(self):
        return helper.email_logic(self.cleaned_data.get('email'))
    
    def clean_phone(self):
        return helper.phone_logic(self.cleaned_data.get('phone'))
    
    def clean_date(self):
        return helper.date_logic(self.cleaned_data.get('date'))
    
    def clean_service(self):
        clean_data = super().clean()
        time = clean_data.get('time')
        notes = clean_data.get('notes')

        helper.check_fields(time,notes)
        return clean_data
    
    
    




    # def date_logic(self):
    #     booking_date = self.cleaned_data.get('date')

    #     if not booking_date:
    #         raise forms.ValidationError("Date is required.")

    #     if booking_date < date.today():
    #         raise forms.ValidationError("You can not book a past date.")
    #     return booking_date
   
    # def  name_logic(self):
    #     name = self.cleaned_data.get('name')

    #     if not name:
    #         raise forms.ValidationError("Name is required.")

    #     if len(name) < 3:
    #         raise forms.ValidationError("Name is too short.")
    #     return name

    # def email_logic(self):
    #     email = self.cleaned_data.get('email')

    #     if not email:
    #         raise forms.ValidationError("Email address is required.")

    #     if not re.match(EMAIL_REGEX,email):
    #         raise forms.ValidationError("Enter valid email address.")
    #     return email
    
    # def phone_logic(self):
    #     phone  = self.cleaned_data.get('phone')

    #     if not phone:
    #         raise forms.ValidationError("Phone number is required.")

    #     if not re.match(PHONE_REGEX,phone):
    #         raise forms.ValidationError("Enter valid phone number.")
    #     return phone
    

    # def check(self):
    #     cleaned_data = super().clean()

    #     service = cleaned_data('service')
    #     time = cleaned_data('time')
    #     notes = cleaned_data('notes')

    #     if not service or not time or not notes:
    #         raise forms.ValidationError("Fill all required fields.")
    #     return cleaned_data
    
    # def slot_check(self):
    #     cleaned_data =  super().clean()

    #     booking_date = cleaned_data.get('date')
    #     booking_time = cleaned_data.get('time')

    #     if booking_date and booking_time:
    #         if Order.objects.filter(date=booking_date,time=booking_time).exists():
    #             raise forms.ValidationError("This time slot is arleady booked.")
        


