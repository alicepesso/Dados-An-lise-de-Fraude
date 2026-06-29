import boto3
import kagglehub
from kagglehub import KaggleDatasetAdapter
import awswrangler as wr

# Cria a sessão 
session = boto3.Session(
    aws_access_key_id="sua-chave-de-acesso",
    aws_secret_access_key="sua-chave-de-acesso-secreto",
    region_name="us-east-1"  
)

# Lendo o dado do Kaggle 
file_path = "credit_card_fraud.csv"
df_kaggle = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "teamincribo/credit-card-fraud",
  file_path
)

print("Dados lidos! Enviando para o S3...")

caminho_s3 = "s3://credito-fraudes-kaggle/bronze/credit_card_fraudaaa.csv"

df_kaggle = df_kaggle.replace(r'[\r\n]+', ' ', regex=True)

wr.s3.to_csv(
    df=df_kaggle,
    path=caminho_s3,
    index=False, 
    sep=';',     
    boto3_session=session
)

print(df_kaggle.dtypes)
print(" Arquivo salvo na Camada Bronze com sucesso!")