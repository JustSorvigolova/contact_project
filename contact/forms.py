from .models import Contac
from django.forms import ModelForm, TextInput, Textarea, EmailInput, NumberInput, URLInput, DateTimeInput


class ContacForm(ModelForm):
    class Meta:
        model = Contac
        fields = ['name', 'last_name', 'big_name', 'text_01', 'birthday', 'num_ber', 'email', 'cosial']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "big_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "birthday": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            "text_01": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "num_ber": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            "cosial": URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Соц.сети'
            })
        }
