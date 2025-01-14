Las validaciones estan explicadas segun se hacen, el form, aqui voy a explicar los widgets que tengo 

1) TextInput: Utilizado en varios formularios para campos como nombre, titulo, y direccion

    'nombre': forms.TextInput(attrs={'class': 'form-control'}),


2) EmailInput: Usado en el formulario UsuarioForm para el campo email

    'email': forms.EmailInput(attrs={'class': 'form-control'}),

3) DateTimeInput: Usado en el formulario UsuarioForm para el campo fecha_registro

    'fecha_registro': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),

4) Textarea: Utilizado en varios formularios para campos de texto más largos, como ubicacion, biografia, y descripcion

    'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

5) NumberInput: Usado en varios formularios para campos numéricos como edad, precio, precio_por_noche, max_usuarios, y numero.

    'edad': forms.NumberInput(attrs={'class': 'form-control'}),

6) Select: Usado en el formulario PerfilForm para el campo genero y en PropiedadForm para campos relacionados como usuario


    'genero': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')], attrs={'class': 'form-control'}),

7) CheckboxInput: Usado para campos booleanos como premiun, principal, y disponibl

    'premiun': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

8) CheckboxSelectMultiple: Utilizado en el formulario PropiedadForm para el campo servicios_extra

    'servicios_extra': forms.CheckboxSelectMultiple(),
