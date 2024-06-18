from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.core.files.base import ContentFile
from PIL import Image
import base64
import io
import psycopg2

try:
    connection = psycopg2.connect(
        dbname="suburbioDB",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(max_length=50)

    @staticmethod
    def convert_image_to_base64(image):
        if image:
            image_data = image.read()
            return base64.b64encode(image_data).decode()
        return None

    @staticmethod
    def convert_base64_to_image(base64_string, image_name='image.jpg'):
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
        image_file = io.BytesIO()
        image.save(image_file, format='JPEG')
        image_field = ContentFile(image_file.getvalue(), image_name)
        return image_field

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Aumente o tamanho do campo para acomodar o hash da senha
    last_login = models.DateTimeField(default=timezone.now)  # Adicione este campo

    def is_valid(self):
        pass
