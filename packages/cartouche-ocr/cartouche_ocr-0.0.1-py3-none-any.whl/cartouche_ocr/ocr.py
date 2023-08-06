from PIL import Image
import pandas as pd
import os
from doctr.models import ocr_predictor

def ocr_cartouche(cartouches):
    '''
    prend un dictionnaire de cartouches et réalise l'ocr dessus
    '''
    predictor = ocr_predictor(pretrained=True)
    result = []
    for j in cartouches:
        cur = {}
        tail = os.path.split(j)[1]
        cur["name"] = tail
        output = predictor([cartouches[j]]).render()
        cur["output"] = output.replace('\n'," ")
        result.append(cur)
    return result

def extract_result(result,name='result'):
    '''
    enregistre le résultat sous format excel
    '''
    df = pd.DataFrame(result)
    df.to_excel(name+'.xls')
    
def ocr_all(cartouches):
    '''
    réalise l'ocr et l'exportation
    '''
    result = ocr_cartouche(cartouches)
    extract_result(result)
