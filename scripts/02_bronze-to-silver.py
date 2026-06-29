import sys
import pandas as pd
import awswrangler as wr
import boto3
from awsglue.utils import getResolvedOptions

# Capturar argumentos passados pelo console
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

boto3.setup_default_session(region_name='us-east-1') 

def transform_bronze_to_silver():
    bronze_path = "s3://credito-fraudes-kaggle/bronze/credit_card_fraud.csv"
    silver_path = "s3://credito-fraudes-kaggle/prata/credit_card_fraud_prata.csv"

    df = wr.s3.read_csv(path=bronze_path, sep=';')
    
    # Criando o ID do cartão com os últimos 4 dígitos do HASH
    df['card_number_suffix'] = df['Card Number (Hashed or Encrypted)'].astype(str).str[-4:]
    
    # Convertendo tipos
    df['Transaction Date and Time'] = pd.to_datetime(df['Transaction Date and Time'])
    
    # Criando as novas colunas temporais
    df['transaction_date'] = df['Transaction Date and Time'].dt.date
    df['transaction_hour'] = df['Transaction Date and Time'].dt.hour
    df['day_of_week'] = df['Transaction Date and Time'].dt.dayofweek

    # Excluindo colunas
    df = df.drop(columns=[
        'Card Number (Hashed or Encrypted)',
        'Card Expiration Date', 
        'CVV Code (Hashed or Encrypted)', 
        'IP Address', 
        'User Account Information',
        'Transaction Notes'
    ])

    # Csv na Silver
    wr.s3.to_csv(
        df=df,
        path=silver_path,
        index=False,
        sep=';',
        encoding='utf-8'
    )

if __name__ == "__main__":
    transform_bronze_to_silver()