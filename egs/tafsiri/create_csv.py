import os, glob, sys
import numpy as np
import pandas as pd

languages = ['fongbe', 'goungbe', 'wolof', 'haussa', 'swahili']

def get_alffa_data(folder1, language, tafsiri=False):
    data = []
    subfolders = os.listdir(folder1)
    for subfolder in subfolders:
        subfolder = os.path.join(folder1, subfolder, "*.wav")
        for filename in glob.glob(subfolder):
            if tafsiri and language == 'fongbe':
                if 'fongbe' in filename:
                    data.append((filename.split('/')[-1], filename, language))
            elif tafsiri and language == 'goungbe':
                if 'goungbe' in filename or 'goubgbe' in filename:
                    data.append((filename.split('/')[-1], filename, language))
            else:
                data.append((filename.split('/')[-1], filename, language))
    return data
    
def split_data(data):
    chunked_list = list()
    kk = 0
    five_split = np.array_split(data, 5)
    for d in five_split:
        d = list(d)
        kk += 1
        for _ in d:
            _ = list(_)
            _.append(kk)
            chunked_list.append(_)
    return chunked_list

def get_data_filenames():
    data = []
    fgb = []
    swh = []
    wf = []
    folder1 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/FONGBE/data/train/wav/"
    folder2 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/FONGBE/data/test/wav/"
    fgb.extend(get_alffa_data(folder1, 'fongbe'))      
    print(len(fgb))
    fgb.extend(get_alffa_data(folder2, 'fongbe'))
    print(len(fgb))
    folder3 = "/home/frejus/Projects/tafsiri-datasets/dataset/"
    fgb.extend(get_alffa_data(folder3, 'fongbe', True))     
    print(len(fgb))
    data.extend(split_data(fgb))  
    
    
    folder4 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/SWAHILI/data/train/wav/"
    swh.extend(get_alffa_data(folder4, 'swahili'))     
    print(len(swh))
    folder5 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/SWAHILI/data/test/wav5/"
    swh.extend(get_alffa_data(folder5, 'swahili'))     
    print(len(swh))
    data.extend(split_data(swh)) 
    folder6 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/WOLOF/data/train/"
    wf.extend(get_alffa_data(folder6, 'wolof'))     
    print(len(wf))
    folder7 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/WOLOF/data/test/wav/"
    wf.extend(get_alffa_data(folder7, 'wolof'))     
    print(len(wf))
    folder8 = "/home/frejus/Projects/ALFFA_PUBLIC/ASR/WOLOF/data/dev/wav/"
    wf.extend(get_alffa_data(folder8, 'wolof'))
    data.extend(split_data(wf)) 
    print(len(data))
    return data
            
        
filename_list = get_data_filenames()

df = pd.DataFrame(filename_list, columns=['filename', 'path', 'category', 'fold'])
df.to_csv('low_resources.csv')
    
    
     