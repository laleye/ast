import os, json
import numpy as np

#convert to 16khz
meta = np.loadtxt('./low_resources.csv', delimiter=',', dtype='str', skiprows=1)
os.makedirs('./data/audio_16k/')
for i in range(0, len(meta)):
    audio = meta[i][2]
    _audio = meta[i][1]
    print('sox ' + audio + ' -r 16000 ' + './data/audio_16k/' + _audio)
    os.system('sox ' + audio + ' -r 16000 ' + './data/audio_16k/' + _audio)
    
label_set = {'fongbe': 0, 'goungbe': 1, 'wolof':2, 'swahili': 3}

os.makedirs('./data/datafiles')

for fold in [1,2,3,4,5]:
    base_path = './data/audio_16k/'
    train_wav_list = []
    eval_wav_list = []
    for i in range(0, len(meta)):
        cur_label = str(label_set[meta[i][3]])
        cur_path = meta[i][1]
        cur_fold = int(meta[i][4])
        
        cur_dict = {"wav": base_path + cur_path, "labels": '/m/07rwj'+cur_label.zfill(2)}
        if cur_fold == fold:
            eval_wav_list.append(cur_dict)
        else:
            train_wav_list.append(cur_dict)
            
    print('fold {:d}: {:d} training samples, {:d} test samples'.format(fold, len(train_wav_list), len(eval_wav_list)))

    with open('./data/datafiles/lw_train_data_'+ str(fold) +'.json', 'w') as f:
        json.dump({'data': train_wav_list}, f, indent=1)

    with open('./data/datafiles/lw_eval_data_'+ str(fold) +'.json', 'w') as f:
        json.dump({'data': eval_wav_list}, f, indent=1)

print('Finished Our Data Preparation')