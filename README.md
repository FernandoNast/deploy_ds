# 💼 Churn Prediction API – Previsão de Abandono de Clientes

Este projeto é uma API de Machine Learning construída com **FastAPI** que realiza a previsão de **churn** (abandono de clientes) com base em dados de uma instituição financeira fictícia.

---

## 🧠 Descrição do Problema

Seu objetivo é prever o **churn** (abandono de clientes) em um banco de dados fictício de uma instituição financeira.

Para isso, são fornecidos dois datasets:

- `Abandono_clientes.csv`: 10.000 registros e 13 colunas. A coluna `Exited` indica se o cliente abandonou o banco (1) ou não (0).
- `Abandono_teste.csv`: 1.000 registros e 12 colunas (sem a coluna `Exited`).

A missão é construir um pipeline de Machine Learning capaz de prever a coluna `Exited` com base nos dados fornecidos.

---

## 🧰 Tecnologias utilizadas

- Python 3.9
- FastAPI
- Scikit-learn
- XGBoost
- Gunicorn
- Render (deploy gratuito)
- Pickle (para salvar e carregar modelos)

---

## 📁 Estrutura do Projeto

```
.
├── api/
│   ├── handler.py                 # Endpoints da API
│   └── model_churn/
│       ├── __init__.py
│       └── model_churn.py         # Classe com lógica de carregamento e predição
├── data/
│   ├── Abandono_clientes.csv      # Base de treino
│   └── Abandono_teste.csv         # Base de teste (sem rótulo)
├── model/
│   ├── model_randomForest.pkl     # Modelo treinado (opcional)
│   └── model_xgboost.pkl          # Modelo em produção
├── requirements.txt               # Dependências
├── Procfile                       # Arquivo de deploy no Render
```

---

## 🔧 Como rodar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/fernandonast/churn-prediction-api.git
cd churn-prediction-api
```

2. **Crie um ambiente virtual (opcional):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a API:**

```bash
uvicorn api.handler:app --reload
```

5. Acesse a documentação interativa (Swagger):

```
http://localhost:8000/docs
```

---

## 🌐 API em produção

A aplicação está hospedada gratuitamente no Render:

🔗 **https://churn-prediction-api.onrender.com**

---

## 🧪 Exemplo de uso (via Postman ou cURL)

### `POST /predict`

#### Corpo da requisição (exemplo):

```json
{
  "CreditScore": 600,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 3,
  "Balance": 60000.0,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 50000.0
}
```

#### Resposta esperada:

```json
{
  "churn": true,
  "probabilidade": 0.81
}
```

> ⚠️ O formato da entrada pode variar conforme o modelo utilizado.

---

## 🧑 Autor

- **Fernando Nast**
- [LinkedIn](https://www.linkedin.com/in/fernandonast)
- [GitHub](https://github.com/fernandonast)

---

## 📌 Observações

- Projeto desenvolvido com fins educacionais para praticar deploy de modelos de Machine Learning como APIs RESTful.
- O modelo em produção é baseado no algoritmo **XGBoost**.