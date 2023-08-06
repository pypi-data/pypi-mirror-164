import pdf2image
import layoutparser as lp
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image

def load_images(_path,nb_page = 3):
    '''
    Charge les plans à partir d'un dossier pouvant contenir plusieurs sous dossiers
     _path = chemin d'accès au dossier mère
     nb_page = nombre de pages à garder pour les pdf 
     retourne un dictionnaire contenant les pdf en format PIL
     '''
    names = []
    pdf = {}
    
    for path, subdirs, files in os.walk(_path):
        for name in files:
        
            names.append(os.path.join(path,name))

    for i in names:

        if '.pdf' in i or '.PDF' in i:
            
            img =pdf2image.convert_from_bytes(open(i,'rb').read(),last_page=nb_page)
            if len(img)>1:
                pdf[i] = img
                
            else:
                pdf[i] = img
                
            

    return pdf

def load_model_layout_parser(config = './trained_layout_parser/config_table.yaml', modele ='./trained_layout_parser/model_retrained.pth', label = {0: "cartouche"} ):
    '''
    charge le modèle de layout_parser
    config = chemin d'accès à la configuration du réseau à utiliser, fichier .yaml
    modele = chemin d'accès du modèle à utiliser, fichier à pth
    retourne le modèle
    '''
    
    model = lp.models.Detectron2LayoutModel(
            config_path =config,
            model_path = model,
            label_map = label)
    return model

def detect_cartouche(images, model):
    '''
    Réalise la détection des cartouches sur les plans et pdf
    images = dictionnaire contenant les images en format PIL
    model = model à utiliser pour l'inférence
   
    Return : - images = dictionnaire contenant les images avec cartouche
             - layouts = dictionnaire contenant des layout
    '''
    layouts = {}
    true_img = {}
    for i in images:
        if isinstance(images[i],list):
            score = 0
            true_page = 0
            true_lay = 0
            for j in images[i]:
                cur = (model.detect(j))
                if len(cur)>0:
                    if cur[0].score>score:
                        score = cur[0].score
                        true_page = j
                        true_lay = cur
            if true_page != 0 :
                layouts[i] =true_lay
                images[i] = true_page
                        
        else:
            layouts[i] = model.detect(i)
           
    return images, layouts

def crop_cartouche(images, layout):
    '''
    Extrait les cartouches à partir d'un dictionnaire d'images et le dictionnaire de layout correspondant 
    '''
    crops_all = {}
    unused = {}
    for l in layout:
        
        
        text_blocks = lp.Layout([b for b in layout[l] if b.type=='cartouche'])
        nb_block = len(text_blocks)
        right = 0
        if nb_block >0 :

            if nb_block >1 : 
                for i in range(1,nb_block):
                    if text_blocks[right].score - text_blocks[i].score <0.001:
                        if text_blocks[i].block.y_2 - text_blocks[i].block.y_1 > text_blocks[right].block.y_2 - text_blocks[right].block.y_1:
                            right = i


            if text_blocks[right].score>0.95:
                crop = text_blocks[right].crop_image(np.array(images[l]))

                crops_all[l] = crop
        else:
            unused[l] = images[l]
            
    return crops_all, unused

def detect_and_crop_cartouche(images,model):
    '''
    regroupe la détection et l'extraction des cartouches
    '''
    images, layout_dict = detect_cartouche(images, model)
    cropped, unused = crop_cartouche(images, layout_dict)




