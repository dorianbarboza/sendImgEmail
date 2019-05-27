import io
import smtplib
import mimetypes
from PIL import ImageChops
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
#from _future_ import print_function
from PIL import Image
import StringIO
import cStringIO

def edicion_imagen():

    image = Image.open("marte.png")
    new_image = ImageChops.invert(image)
    new_image.save("editmarte.png")
    return new_image


def envio(attach_image):
    # Creando objeto, definiendo cuerpo del mensaje
    mensaje = MIMEMultipart()
    mensaje ['gmail_from'] = "dorianbarboza@gmail.com"
    mensaje ['gmail_to'] = "eyden.barboza@gmail.com"
    mensaje ['subject'] = "Imagen"
    mensaje ['body'] = "Imagen de marte"

    memf = cStringIO.StringIO()
    attach_image.save(memf, "PNG")

    attach = MIMEImage(memf.getvalue(), "png")
    attach.add_header('Content-Disposition','attachment; filename = "editmarte.png"')
    mensaje.attach(attach)

    # Autenticacion
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('dorianbarboza@gmail.com','dabv-18101996')

    # Envio de correo
    mailServer.sendmail("eyden.barboza@gmail.com","andyfbarbozav.itche@gmail.com", mensaje.as_string())

    # Cerrar conexion
    mailServer.quit()

if __name__ == '__main__':
    imagen = edicion_imagen()
    send = envio(imagen)
