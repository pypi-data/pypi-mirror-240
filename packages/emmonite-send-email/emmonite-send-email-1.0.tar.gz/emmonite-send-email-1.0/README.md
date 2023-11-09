# Enviar correo

### Esta libreria no utiliza paquetes externos, solo los que ya tiene python por defecto.

**Metodo de uso:**

```python


# Este es tu diccionario de variables para reemplazar en el HTML
variables = {
    "nombre": "Javier Bahamondes",
    "edad": 35,
}

# Estos son los detalles del correo electrónico
email_sender = 'soporte@email.cl'
email_password = 'qwer123.'
smtp_server = 'smtp.gmail.com'
smtp_port = 465
subject = 'Bienvenido a Nuestro Servicio'
body_path = 'template_email.html'  # Asegúrate de que este sea el path correcto al archivo HTML
lista_correos = ['destinatario1@example.com', 'destinatario2@example.com']

# Llamada a la función send_email
send_email(email_sender, email_password, smtp_server, smtp_port, subject,
           body_path, variables, lista_correos)
```
