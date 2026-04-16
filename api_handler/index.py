import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from HNG_Task1.wsgi import application

app = application