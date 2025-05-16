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
    df.to_csv(f'../Archivos/comparacionIQR.csv', index=False)
    print(df)

    # Ranking
    ranking = df.apply(stats.rankdata, axis=1)
    print("Columnas Rankeadas:")
    print(ranking)
    ranking_promedio = ranking.mean()
    print("Ranking Promedio:")
    print(ranking_promedio)

    # Friedman Test
    res = stats.friedmanchisquare(*[df[columna] for columna in df])
    print(res)

    from scikit_posthocs import posthoc_nemenyi_friedman # Post hoc 1
    res = posthoc_nemenyi_friedman(df)
    print(res)

    from scikit_posthocs import posthoc_conover_friedman # Post hoc 2
    res = posthoc_conover_friedman(df)
    print(res)