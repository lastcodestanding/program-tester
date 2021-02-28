import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

#os.environ['GOOGLE_APPLICATIONCREDENTIALS'] = r'ServiceAccountToken.json'
client = vision.ImageAnnotatorClient()

folder_path = r'static/Images'
image_file = 'testprog.jfif'
file_path = os.path.join(folder_path,image_file)

with io.open(file_path, 'rb') as image_file:
    content  = image_file.read()
    
image = vision.types.Image(content = content)
response = client.document_text_detection(image=image)
doctext = response.full_text_annotation.text
print(doctext)