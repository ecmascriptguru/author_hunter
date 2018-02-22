import os
from src import app

config_name = os.getenv('FLASK_CONFIG')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
