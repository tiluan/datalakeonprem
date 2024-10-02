from minio import Minio
from minio.error import S3Error  # Updated import
import os

# Add Logger
import logging
logger = logging.getLogger(__name__)

# Ingestão dos dados para o MinIO
def upload_to_minio(bucket_name, file_name):
    # Obter as variáveis de ambiente
    access_key = os.getenv('MINIO_ROOT_USER')
    secret_key = os.getenv('MINIO_ROOT_PASSWORD')

    # Criar um cliente MinIO com a URL do MinIO, chave de acesso e chave secreta
    minioClient = Minio('http://172.27.137.205:9090/',
                        access_key=access_key,
                        secret_key=secret_key,
                        secure=False)

    # Verificar se o bucket existe
    try:
        found = minioClient.bucket_exists(bucket_name)
        if not found:
            minioClient.make_bucket(bucket_name)
        # Fazer o upload do arquivo
        minioClient.fput_object(bucket_name, file_name, file_name)
        logger.info(f"Arquivo {file_name} enviado para o bucket {bucket_name} com sucesso.")
    except S3Error as err:
        logger.error(f"Erro ao acessar o MinIO: {err}")