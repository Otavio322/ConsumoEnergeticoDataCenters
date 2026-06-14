# Predição de Consumo Elétrico em Data Centers

Sistema de Machine Learning para previsão do consumo elétrico (MWh) de data centers, com base em suas características operacionais. O projeto contempla desde a análise dos dados até uma aplicação web funcional para realizar predições.

## Objetivo

Prever o **consumo elétrico diário (MWh)** de um data center a partir de variáveis como capacidade instalada, eficiência energética, sistema de resfriamento, eficiência no uso de água e consumo de água.

- **Tipo de problema:** Regressão
- **Variável alvo (Y):** `Consumo_Eletrico_MWh`
- **Variáveis explicativas (X):** `Capacidade_MW`, `Eficiencia_Energetica`, `Sistema_Resfriamento`, `Eficiencia_Agua`, `Consumo_Agua_Galoes`

## Base de Dados

- **Fonte:** Data Center Hybrid Dataset
- **Registros:** 126.770 (após limpeza)
- **Variáveis:** numéricas e categóricas, incluindo dados de localização, capacidade, eficiência energética e hídrica

## Etapas do Projeto

### 1. Coleta, Pré-processamento e Análise Descritiva
- Limpeza dos dados (remoção de valores ausentes)
- Seleção das variáveis relevantes
- Label Encoding das variáveis categóricas (Sistema de Resfriamento e Nível de Estresse Hídrico)
- Análise descritiva: histogramas, gráficos de barras, matriz de correlação e dispersão

### 2. Experimentos e Escolha do Modelo
- Treinamento de 3 modelos: **Regressão Linear**, **KNN** e **Árvore de Decisão**
- 30 execuções independentes, com cálculo de MAE médio e desvio padrão
- Modelo escolhido: **Árvore de Decisão** (menor MAE médio: ~69)
- Exportação do modelo final com `pickle`

### 3. Aplicação Web (Flask)
- Backend em Flask que carrega o modelo treinado e retorna a predição
- Frontend em HTML/CSS com formulário para entrada das variáveis
- Resultado da predição exibido diretamente na página

## Estrutura do Projeto

```
ATIVIDADEDATASCIENCE/
├── instances/
│   └── data_center_hybrid.csv         # Base de dados utilizada
├── models/
│   └── consumo_energia.pkl            # Modelo treinado (Árvore de Decisão)
├── notebook/
│   └── Consumo_Energetico_*.ipynb     # Notebook com análise e experimentos (Colab)
├── static/
│   └── style.css                      # Estilização da aplicação
├── templates/
│   └── index.html                     # Formulário e exibição do resultado
├── app.py                             # Aplicação principal Flask
├── classifier.py                      # Carrega o modelo e realiza a predição
├── requirements.txt                   # Dependências do projeto
└── README.md
```

## Como Executar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd ATIVIDADEDATASCIENCE
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python app.py
```

4. Acesse no navegador:
```
http://127.0.0.1:5000
```

## Tecnologias Utilizadas

- **Python**
- **Pandas / NumPy** — manipulação e tratamento dos dados
- **Scikit-learn** — treinamento e avaliação dos modelos
- **Matplotlib / Seaborn** — visualizações e análise descritiva
- **Flask** — backend e servidor web
- **HTML / CSS** — interface do usuário
- **Pickle** — serialização do modelo treinado
- **Google Colab** — ambiente de experimentação

## Resultados

| Modelo | MAE Médio | Desvio Padrão |
|---|---|---|
| Regressão Linear | 90.95 | 1.84 |
| KNN | 223.79 | 6.26 |
| **Árvore de Decisão** | **69.20** | **2.09** |

O modelo final (Árvore de Decisão, `max_depth=10`) obteve **MAE ≈ 64 MWh** no conjunto de teste, o que representa um erro de aproximadamente 10% em relação à média de consumo (605 MWh).

## Limitações e Melhorias Futuras

- Treinamento realizado com amostra de 20% da base completa
- Possibilidade de adicionar autenticação de usuários
- Salvar predições em banco de dados
- Criar dashboard com estatísticas
- Exportação de relatórios das predições