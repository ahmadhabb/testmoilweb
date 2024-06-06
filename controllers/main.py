from flask import Blueprint, render_template, request, redirect, url_for, session
from models.image import process_image, delete_image

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('error', None)  # Clear any existing error
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                process_image(file)
                return redirect(url_for('main.index'))

        if 'rotate-left' in request.form or 'rotate-right' in request.form or 'reset' in request.form:
            if 'image_path' not in session:
                session['error'] = 'gambar belum di upload'
                return redirect(url_for('main.index'))

            if 'rotate-right' in request.form:
                session['rotation'] = (session['rotation'] - 5) % 360
                return redirect(url_for('main.index'))

            if 'rotate-left' in request.form:
                session['rotation'] = (session['rotation'] + 5) % 360
                return redirect(url_for('main.index'))

            if 'reset' in request.form:
                session['rotation'] = 0
                return redirect(url_for('main.index'))

        if 'delete-image' in request.form:
            delete_image()
            return redirect(url_for('main.index'))

    image_data, rotation_value = process_image()
    error = session.pop('error', None)
    return render_template('index.html', image_data=image_data, rotation_value=rotation_value, error=error)
