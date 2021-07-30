from django.forms import ModelForm, Textarea
from .models import yazi
from captcha.fields import ReCaptchaField


class CreateForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = yazi

        fields = '__all__'  # seçilen model daki bütün objeleri çağırır.
        # fields = ['baslik']  model ın içinden sadece seçilen objeleri çağırır.
        # exclude = ['baslik']  model ın içinden bu obje dışında hepsini çağırır.

        widgets = {
            'metin': Textarea(attrs = {'cols': 80, 'rows': 20, 'class': 'metinClassı'})
        }

