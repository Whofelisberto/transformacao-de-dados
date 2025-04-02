import tabula
import zipfile
import pandas as pd
import os

## o código só vai funcionar se o pfd do arquivo estiver na msm pasta do projeto!!
pdf_path = "anexo_I.pdf"

## Função para trocar as abreviações pelas descrições 
def trocar(df):
    df.replace({"OD": "Odontologia", "AMB": "Ambulatório"}, inplace=True)
    return df

## usei a biblioteca tabula para extrair todas as tabelas do pdf
tabelas = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

## concatenei as tabelas extraídas em um único dataframe
todas_tabelas = pd.concat(tabelas, ignore_index=True)

## substitui as abreviações "OD" e "AMB"
todas_tabelas = trocar(todas_tabelas)

## salvar os dados em um único arquivo CSV
csv_path = 'tabelas.csv'
todas_tabelas.to_csv(csv_path, index=False, encoding='utf-8')

## compacta o arquivo csv para zip
zip_path = "Teste_seu_nome.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

print(f"arquivo compactado em {zip_path}.")
