# Gera dados fakes de celulares com status Conectado
from generates_fake_data import generates_fake_data
from datetime import datetime
import io
import sys
import os

# Adiciona minio_data_ingestion ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from minio_data_ingestion import upload_to_minio

def main():
    try:
        dispositivo_de_acesso = 'Celular'
        status = 'Conectado'
        qtd_conexao = 10

        df = generates_fake_data(qtd_conexao, dispositivo_de_acesso, status)

        # Converte o DataFrame em parquet e armazena na memória usando BytesIO
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, engine='pyarrow')
        parquet_buffer.seek(0)  # Retorna ao início do buffer

        # Envia para o MinIO
        bucket_name = "landing-zone"
        destination_file = f"{dispositivo_de_acesso}/{status}/{dispositivo_de_acesso}_{status}_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        upload_to_minio(bucket_name, parquet_buffer, destination_file)
        return 

    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")
