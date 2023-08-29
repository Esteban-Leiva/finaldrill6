from django import forms


class MainForm(forms.Form):
    marcas = (('FORD', 'FORD'),('FIAT', 'FIAT'),('CHEVROLET', 'CHEVROLET'),('TOYOTA', 'TOYOTA'),)
    categorias= (('PARTICULAR','PARTICULAR'),('TRANSPORTE','TRANSPORTE'),('CARGA','CARGA'))

    marca = forms.ChoiceField(label='Marca', choices = marcas)
    modelo = forms.CharField(label='Modelo', max_length=100)
    carroceria = forms.CharField(label='Serial Carroceria', max_length=50)
    motor = forms.CharField(label='Serial Motor', max_length=50)
    categoria = forms.ChoiceField(label='Categoria', choices = categorias)
    precio = forms.IntegerField(label='Precio')