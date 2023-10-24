import waitress
from pp1 import app

if __name__ == "__main__":
    waitress.serve(app, host='127.0.0.1', port=5000)
