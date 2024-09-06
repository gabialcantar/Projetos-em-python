import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Definindo os parâmetros
num_entries = 100
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Função para gerar datas aleatórias
def random_dates(start, end, n):
    start_u = start.timestamp()
    end_u = end.timestamp()
    return [datetime.fromtimestamp(ts) for ts in np.random.uniform(start_u, end_u, n)]

# Dados fictícios
data = {
    "Data da fraude": random_dates(start_date, end_date, num_entries),
    "Valor da transação": np.random.uniform(100, 10000, num_entries).round(2),
    "Tipo de fraude": np.random.choice(["Clonagem", "Roubo de Identidade", "Phishing"], num_entries),
    "Localidade": np.random.choice(["São Paulo/SP", "Rio de Janeiro/RJ", "Belo Horizonte/MG", "Brasília/DF", "Salvador/BA"], num_entries),
    "Instituição financeira": np.random.choice(["Banco A", "Banco B", "Banco C", "Banco D"], num_entries),
    "Meio da transação": np.random.choice(["Online", "Presencial"], num_entries),
    "Status da investigação": np.random.choice(["Em andamento", "Resolvida"], num_entries)
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando no arquivo Excel
file_path = "/mnt/data/fraudes_cartao_credito_brasil.xlsx"
df.to_excel(file_path, index=False)
file_path