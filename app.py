from flask import Flask
from controllers.main import main_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
