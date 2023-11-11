import  pandas as pd
import numpy as np
def get_grupos_pokemon():
    df = pd.read_csv('mycsvfile.csv')
    return df['name']

def get_altura_media_grupo(grupo):
    df = pd.read_csv('mycsvfile.csv')
    return np.array(df[df['name'] == grupo]['AVGHeight'])

def get_peso_medio_grupo(grupo):
    df = pd.read_csv('mycsvfile.csv')
    return np.array(df[df['name'] == grupo]['AVGWeight'])
