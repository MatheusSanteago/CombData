import pandas as pd
import matplotlib.pyplot as plt


def transform(data):  # Transformação
    data.rename(columns={'referencia': 'Referência',
                         'ano': 'Ano',
                         'mes': 'Mês',
                         'gasolina_comum_preco_revenda_avg': 'Gasolina Comum',
                         'gasolina_aditivada_preco_revenda_avg': 'Gasolina Aditivada',
                         'etanol_hidratado_preco_revenda_avg': 'Etanol Hidratado',
                         'oleo_diesel_preco_revenda_avg': 'Oléo Diesel',
                         'oleo_diesel_s10_preco_revenda_avg': 'Oléo Diesel S10',
                         'gas_cozinha_glp_preco_revenda_avg': 'GLP',
                         'gas_natural_veicular_gnv_preco_revenda_avg': 'GNV',
                         }, inplace=True)
    newData = data[['Referência',
                    'Ano',
                    'Mês',
                    'Gasolina Comum',
                    'Gasolina Aditivada',
                    'Etanol Hidratado',
                    'Oléo Diesel',
                    'Oléo Diesel S10',
                    'GLP',
                    'GNV']]
    return newData


def calculosBasicos(data):  # Média por ano de cada combustível
    df = data[['Ano', 'Gasolina Comum',
               'Gasolina Aditivada',
               'Etanol Hidratado',
               'Oléo Diesel',
               'Oléo Diesel S10',
               'GLP',
               'GNV']].groupby(['Ano'], as_index=False)
    df_mean = df.mean()
    df_median = df.median()


def plotting(media):
    plt.plot('Ano', 'Gasolina Comum',
             data=media, label='Gasolina Comum')
    plt.plot('Ano', 'Gasolina Aditivada',
             data=media, label='Gasolina Aditivada')
    plt.plot('Ano', 'Etanol Hidratado',
             data=media, label='Etanol Hidratado')
    plt.plot('Ano', 'Oléo Diesel', data=media, label='Oléo Diesel')
    plt.plot('Ano', 'Oléo Diesel S10',
             data=media, label='Oléo Diesel S10')
    plt.plot('Ano', 'GNV', data=media, label='GNV')
    plt.grid(True)
    plt.xlabel('Anos')
    plt.ylabel('Valor em R$')
    plt.legend()
    plt.ylim(0, 7)
    plt.show()


if __name__ == '__main__':  # Execucução
    df_full1 = pd.read_csv('./combustiveis-brasil.csv', delimiter=',')
    df = transform(df_full1)
    calculosBasicos(df)
