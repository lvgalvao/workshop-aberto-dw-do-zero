# Workshop Aberto: DW para Avaliação de Valor de Mercado de Empresas Brasileiras

### 1. Clonar o Repositório
Primeiro, clone o repositório do projeto para o seu ambiente local.

```bash
git clone https://github.com/lvgalvao/workshop-aberto-dw-do-zero.git
cd workshop-aberto-dw-do-zero
```

### 2. Configurar o Ambiente Virtual
Crie um ambiente virtual e ative-o.

#### No Windows:
```bash
python -m venv .venv
.\venv\Scripts\activate
```

#### No macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
Instale as dependências do projeto listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Configurar a Chave da API
Atualize o arquivo `src/config.py` com a sua chave da API Alpha Vantage.

```python
ALPHAVANTAGE_API_KEY = "sua_chave_api_aqui"
CSV_FILE_PATH = "../data/external/movimentacao_acoes.csv"
```

### 5. Preparar os Dados
Crie a estrutura de diretórios e adicione o arquivo CSV com os dados de movimentação das ações no diretório apropriado.

```bash
mkdir -p data/external
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/dw
touch data/external/movimentacao_acoes.csv
```

Adicione os dados de movimentação de ações ao arquivo `data/external/movimentacao_acoes.csv` conforme o exemplo fornecido anteriormente.

### Exemplo de CSV com Movimentação de Ações

**Arquivo: `data/external/movimentacao_acoes.csv`**
```csv
date,symbol,action,quantity,purchase_price
2024-01-15,PETR4,buy,100,28.50
2024-02-15,PETR4,sell,50,30.00
2024-03-10,VALE3,buy,200,82.00
2024-04-12,VALE3,sell,100,85.00
2024-01-20,ITUB4,buy,150,23.00
2024-02-20,ITUB4,sell,75,25.00
2024-01-25,BBDC4,buy,120,22.00
2024-03-25,BBDC4,sell,60,24.00
2024-01-30,ABEV3,buy,180,15.00
2024-04-30,ABEV3,sell,90,17.00
```

### Explicação

- **`date`**: Data da transação.
- **`symbol`**: Símbolo da ação.
- **`action`**: Tipo de transação (`buy` para compra, `sell` para venda).
- **`quantity`**: Quantidade de ações transacionadas.
- **`purchase_price`**: Preço de compra das ações.

### 6. Ingestão de Dados
Execute o script de ingestão de dados para coletar os dados da API e carregar os dados do CSV.

```bash
python src/ingest_data.py
```

### 7. Processamento de Dados
Execute o script de processamento de dados para limpar, transformar e integrar os dados coletados.

```bash
python src/process_data.py
```

### 8. Criação do Data Warehouse
Execute o script de criação do Data Warehouse para armazenar os dados integrados no SQLite.

```bash
python src/create_dw.py
```

### 9. Análise de Dados
Execute o script de análise de dados para avaliar os ganhos e perdas e gerar visualizações.

```bash
python src/analysis.py
```

### 10. Revisão dos Resultados
Após executar o script de análise, revise os gráficos gerados para avaliar os ganhos e perdas de cada companhia ao longo do tempo.

### Estrutura de Arquivos e Diretórios Final
```
market_value_analysis/
│
├── data/
│   ├── external/
│   │   └── movimentacao_acoes.csv
│   ├── raw/
│   │   ├── PETR4_stock_data.json
│   │   ├── VALE3_stock_data.json
│   │   ├── ITUB4_stock_data.json
│   │   ├── BBDC4_stock_data.json
│   │   └── ABEV3_stock_data.json
│   ├── processed/
│   │   └── integrated_data.csv
│   └── dw/
│       └── market_value_dw.db
│
├── src/
│   ├── __init__.py
│   ├── ingest_data.py
│   ├── process_data.py
│   ├── create_dw.py
│   ├── analysis.py
│   ├── config.py
│   └── utils.py
│
├── requirements.txt
│
└── README.md
```