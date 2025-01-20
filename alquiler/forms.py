from django import forms
from .models import *  
from django.contrib.auth.forms import UserCreationForm

# Formulario para Usuario
class UsuarioForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Nombre de Usuario"
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contraseña"
    )

    class Meta:
        model = Usuario
        fields = ['email', 'telefono', 'fecha_registro']  # Ya no es necesario incluir 'nombre'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    # Validacion para el  email, verifica que no exista en la base de datos 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado")  
        return email

    # Validacion personalizada para el campo "nombre", verifica que no exista en la base de datos 
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=nombre).exists():  
            raise forms.ValidationError("Este nombre ya está registrado")
        return nombre


# Formulario para Perfil
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['genero', 'edad', 'ubicacion', 'biografia']
        widgets = {
            'genero': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')], attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    # Validacion para edad,  pongo una edad minima y otra maxima, para crear el perfil 
    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad is not None:
            if edad < 18:  
                raise forms.ValidationError("La edad debe ser mayor  a 18 años")
            if edad > 100: 
                raise forms.ValidationError("La edad no puede ser mayor a 100 años")
        return edad

    # Validacion para asegurar una longitud mínima en la biografía
    def clean_biografia(self):
        biografia = self.cleaned_data.get('biografia')
        if len(biografia) < 50:  
            raise forms.ValidationError("La biografía debe tener al menos 50 caracteres")
        return biografia


# Formulario para Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'premiun', 'principal']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'premiun': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'principal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Validacion para asegurar que el nombre no este en la base de datos 
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Categoria.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Este nombre ya está registrado")
        return nombre

    # Validación para la descripcion, minimo 30 caracteress
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 30:
            raise forms.ValidationError("La descripción debe tener al menos 30 caracteres")
        return descripcion


# Formulario para ServicioExtra
class ServicioExtraForm(forms.ModelForm):
    class Meta:
        model = ServicioExtra
        fields = ['nombre', 'descripcion', 'precio', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Validacioan para asegurar que el precio sea mayor a 10
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 10:
            raise forms.ValidationError("El precio debe ser mayor a 10")
        return precio


# Formulario para Propiedad
class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['titulo', 'direccion', 'precio_por_noche', 'max_usuarios', 'usuario', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_por_noche': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_usuarios': forms.NumberInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    # Validacion para asegurar que el precio no sea negativo 
    def clean_precio_por_noche(self):
        precio = self.cleaned_data.get('precio_por_noche')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio por noche debe ser mayor a 0")
        return precio

    # Validacion para asegurar el minimo y max de usuarios 
    def clean_max_usuarios(self):
        max_usuarios = self.cleaned_data.get('max_usuarios')
        if max_usuarios is not None:
            if max_usuarios < 1:
                raise forms.ValidationError("El número máximo de usuarios debe ser al menos 1")
            if max_usuarios > 20:
                raise forms.ValidationError("El número máximo de usuarios no puede exceder 20")
        return max_usuarios


# Formulario para Prioridad
class PrioridadForm(forms.ModelForm):
    class Meta:
        model = Prioridad
        fields = ['nombre', 'descripcion', 'premiun', 'numero']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'premiun': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Validacion para comprobar que el nombre sea unico
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Prioridad.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("El nombre ya está registrado.")
        return nombre

    # Validacion para que el numero sea entre el 1 y el 10
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if numero is not None:
            if numero < 1 or numero > 10:
                raise forms.ValidationError("El número debe estar entre 1 y 10")
        return numero



#Formulario de registro 
class RegistroForm (UserCreationForm):
    ROLES = (
                (UsuarioLogin.ANFRITION, 'anfrition'),
                (UsuarioLogin.USUARIO, 'usuario'),
    )
    
    rol =   forms.ChoiceField(choices=ROLES)
    
    class Meta:
        model = UsuarioLogin
        fields = ['username' , 'email', 'password1', 'password2', 'rol']

