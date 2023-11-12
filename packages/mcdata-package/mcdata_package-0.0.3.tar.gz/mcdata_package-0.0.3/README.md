# MCDATA_PACKAGE

MCDATA_PACKAGE é um pacote Python para facilitar o envio de arquivos para o S3, transformar arquivos CSV e RDS para Parquet, realizar limpeza simples dos dados e guardar dicionários de siglas governamentais.

## Instalação

Você pode instalar o pacote MCDATA_PACKAGE usando pip:

pip install mcdata_package


## Uso

Aqui estão alguns exemplos de como você pode usar o pacote MCDATA_PACKAGE:

### Transformar arquivos CSV e RDS para Parquet

from mcdata.transformar import csv_to_parquet, rds_to_parquet
csv_to_parquet('/path/to/csv_file.csv', '/path/to/parquet_file.parquet') 
rds_to_parquet('/path/to/rds_file.rds', '/path/to/parquet_file.parquet')

### Manipular tabelas

import pandas as pd from mcdata.tabela import ManipularTabela
df = pd.read_csv('/path/to/csv_file.csv') 
manipulator = ManipularTabela(df) processed_df = manipulator.process_table(remove_duplicates=True, null_value_replacement='Unknown', column_mapping={'OldColumnName': 'NewColumnName'}, column_value_mapping={'UF': {31: 'São Paulo'}})

### Obter dicionários de siglas governamentais

from mcdata.dicionarios import uf


## Licença

Este projeto é licenciado sob a Licença MIT - por favor, veja [LICENSE](LICENSE) para mais detalhes.

