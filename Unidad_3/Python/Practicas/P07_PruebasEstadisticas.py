import pandas as pd
from scipy import stats

def load_instancia():
    file = '../Archivos/ResultadosMH_IQR/merge_iqr.csv'
    df = pd.read_csv(file)
    h = set(df['h'])
    df_completo = pd.DataFrame(columns=list(h))
    grupos = df.groupby('va')
    for va, grupo in grupos:
        fila = pd.Series(list(grupo['iqr']), index=list(grupo['h']))
        df_completo.loc[len(df_completo)] = fila

    return df_completo


if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    df = load_instancia()
    ranking = df.apply(stats.rankdata, axis=1)
    print("Columnas Rankeadas:")
    print(ranking)

    # Friedman Test
    res = stats.friedmanchisquare(*[df[columna] for columna in df])
    print(res)