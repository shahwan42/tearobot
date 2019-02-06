import requests
import json
import os

def ocr_space_file(filename, overlay=False, language='eng'):
    
    api_key = os.environ.get('OCR_API')
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    results= r.json()
    return results['ParsedResults'][0]['ParsedText']




def ocr_space_url(url, overlay=False, language='eng'):

    api_key = os.environ.get('OCR_API')
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    results= r.json()
    return results['ParsedResults'][0]['ParsedText']


