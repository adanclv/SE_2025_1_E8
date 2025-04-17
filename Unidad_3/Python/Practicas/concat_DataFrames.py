import os
import pandas as pd

def merge_csv(path, name='merged_completo'):
    files = os.listdir(path)
    df_completo = pd.DataFrame()
    for file in files:
        df = pd.read_csv(path + file)
        df_completo = pd.concat([df_completo, df], ignore_index=True)
    df_completo.to_csv(f'{path + name}.csv', index=False)
    print('Archivos combinados ✅')

if __name__ == '__main__':
    PATH = '../Archivos/ResultadosMH/'
    FILE_NAME = 'merge_mh'
    merge_csv(PATH, FILE_NAME)