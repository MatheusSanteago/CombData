import pandas as pd


df_full = pd.read_csv('./combustiveis-brasil.csv', delimiter=',')

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
         'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

df_full.rename(columns={'referencia': 'Referência',
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

df_full.fillna(0, inplace=True)

df = df_full[['Referência',
              'Ano',
              'Mês',
              'Gasolina Comum',
              'Gasolina Aditivada',
              'Etanol Hidratado',
              'Oléo Diesel',
              'Oléo Diesel S10',
              'GLP',
              'GNV']]

print(df.head(10))
