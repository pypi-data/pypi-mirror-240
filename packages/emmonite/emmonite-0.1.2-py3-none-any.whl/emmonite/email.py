import smtplib
from email.message import EmailMessage
from string import Template


# Para enviar correos (función creada 05-08-2023)
def send_email(email_sender, email_password, smtp_server, smtp_port,
               subject, lista_correos, body_path=None, body_str=None, variables=None, attachment_data=None, filename=""):
    """
    Envia un correo.

    :param email_sender: cuenta de correo que enviara el email - "soporte@soporte.cl"
    :param email_password: contraseña de la cuenta que enviará el email - qwer123.
    :param smtp_server: servidor smtp - "smtp.gmail.com"
    :param smtp_port: puerto del servidor smtp - 465

    :param subject: Asunto del correo
    :param body_path: ruta del archivo.html
    :param body_str: string de html
    :param variables: diccionario de variables que usara el html
    :param lista_correos: Lista de destinatarios
    :param attachment_data: Opcional. Datos del archivo adjunto (BytesIO)
    :param filename: Nombre del archivo adjunto

    :return: Diccionario con el estado del envío y el mensaje de error si ocurre uno.
    """

    body = ""

    try:
        if body_path:
            with open(body_path, 'r', encoding='utf-8') as file:
                html_string = file.read()
                html_template = Template(html_string)
                body = html_template.safe_substitute(variables) if variables else html_string

        elif body_str:
            html_template = Template(body_str)
            body = html_template.safe_substitute(variables) if variables else body_str

        # Detalles del correo
        msg = EmailMessage()
        msg.set_content(body, subtype='html')
        msg['Subject'] = subject
        msg['From'] = email_sender
        msg['To'] = ', '.join(lista_correos)

        # Adjuntar archivo si existe
        if attachment_data:
            file_data = attachment_data.getvalue()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)

        # Enviar correo

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email_sender, email_password)
            server.send_message(msg)

            # Si todo sale bien, retorna un diccionario indicando el éxito
            return {"success": True, "message": f"Correo enviado exitosamente a: {', '.join(lista_correos)}"}
    except Exception as e:
        # Si hay un error, retorna un diccionario con el error
        return {"success": False, "error": str(e)}
