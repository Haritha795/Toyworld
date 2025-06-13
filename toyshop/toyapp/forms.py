from django import forms
from.models import Reg_tbl

class Regform(forms.ModelForm):
    class Meta:
        model=Reg_tbl
        fields=['fnm','mob','eml','psw'] 
        widgets={
            'fnm':forms.TextInput(attrs={'class':'form-control','placeholder':'FullName','style':'width:500px;height:40px;border-radius:10px;border-color:skyblue;margin-top:20px;'}),
            'mob':forms.NumberInput(attrs={'class':'form-control','placeholder':'MobileNumber','style':'width:500px;height:40px;border-radius:10px;border-color:skyblue;margin-top:20px;'}),
            'eml':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','style':'width:500px;height:40px;border-radius:10px;border-color:skyblue;margin-top:20px;'}),
            'psw':forms.PasswordInput(attrs={'class':'form-control','placeholder':'MobileNumber','style':'width:500px;height:40px;border-radius:10px;border-color:skyblue;margin-top:20px;'}),   
        }          