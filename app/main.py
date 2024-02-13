from dotenv import load_dotenv
import os
import sys

def init_env():
    load_dotenv()
    resolved_pypath = os.path.abspath(os.getenv("PYTHONPATH"))
    sys.path.insert(0, resolved_pypath)
init_env()

from app import app

def main():
    app.run()

if __name__=='__main__':
    main()