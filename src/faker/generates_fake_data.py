from faker import Faker
import random
from faker.providers import internet
from datetime import datetime
import pandas as pd

# Add Logger
import logging
logger = logging.getLogger(__name__)

# Função para gerar dados fake e enviar para o MinIO sem salvar localmente
def generates_fake_data(qtd_conexao, dispositivo_de_acesso, status):
    fake = Faker()
    fake.add_provider(internet)
    velocidade_conexao = [1, 5, 10, 15, 25, 35, 50, 100, 200, 400, 500, 1000]
    faker_data = []

    for _ in range(qtd_conexao):
        novo_registro = {
            'Nome': fake.name(),
            'Endereco': fake.address(),
            'Ip': fake.ipv4_private(),
            'Hora_Conexao': datetime.now(),
            'Dispositivo_de_Acesso': dispositivo_de_acesso,
            'Velocidade_de_Conexao': random.choice(velocidade_conexao),
            'Status_Conexao': status
        }
        faker_data.append(novo_registro)
    
    logger.info(f"Gerados {qtd_conexao} registros de dados fake!")    
    df = pd.DataFrame(faker_data)
    return df