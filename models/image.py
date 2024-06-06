from flask import session
from PIL import Image
import os
from io import BytesIO
import base64

UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def process_image(file=None):
    if file:
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(image_path)
        session['image_path'] = image_path
        session['rotation'] = 0

    image_data = None
    rotation_value = 0
    if 'image_path' in session:
        image = Image.open(session['image_path'])
        rotation_value = session['rotation']
        rotated_image = image.rotate(rotation_value, expand=True)
        buffer = BytesIO()
        rotated_image.save(buffer, format="PNG")
        image_data = base64.b64encode(buffer.getvalue()).decode()

    return image_data, rotation_value

def delete_image():
    if 'image_path' in session:
        try:
            os.remove(session['image_path'])
        except FileNotFoundError:
            pass
        session.pop('image_path', None)
    session.pop('rotation', None)
