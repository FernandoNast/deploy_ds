# Churn Prediction API – Customer Attrition Forecast

This project aims the deployment of a Machine Learning API built with **Flask**, capable of predicting **churn** (customer attrition) based on data from a financial institution. The motivation includes:

- Making the model accessible. Training a good model is not enough, it needs to be deployed so other people, systems or applications can use it. For example, a credit risk model is only useful if integrated into a banking app, website or API;
  
- Automating and scaling the solution. With deployment, the model can process thousands of requests automatically, 24/7, without manual intervention, enabling real-world usage;
   
- Integrating with real systems. APIs expose the model so it can be consumed by:
  - Web/mobile frontends;
  - CRMs and ERPs;
  - Data pipelines in production;
  - Bots, services or automated workflows.

- Monitoring performance in real time. After deployment, it’s possible to track prediction quality, latency, errors and even retrain using real-world data. Without this, models may become outdated unnoticed;

- Learning real engineering practices:
  - Modular code structure;
  - Working in production environments;
  - Resolving dependency issues, paths, permissions;
  - Logging, versioning and software best practices.

---

##  Problem Description

The goal is to predict **customers churn** in a financial institution.

Two datasets are provided:

- `Abandono_clientes.csv`: 10,000 rows and 13 columns. The `Exited` column indicates if the customer left the bank (1) or not (0).
- `Abandono_teste.csv`: 1,000 rows and 12 columns (without the `Exited` column).

The mission is to build a Machine Learning pipeline to predict the `Exited` column based on the provided data.

Studying churn is important because it enables data-driven strategic decisions, helps understand why customers are leaving, and guides improvements in products, pricing, service, UX, etc.

It’s also an analytical feedback mechanism to enhance business strategy and personalize retention actions with predictive models, such as:
- Offering targeted discounts;
- Triggering proactive interventions;
- Prioritizing high-risk, high-value clients.

---

## Technologies Used

- Python 3.12.9
- Flask
- Scikit-learn
- XGBoost
- Gunicorn
- Render (free cloud deployment)
- Pickle (to save and load models)

---

## Project Structure

```
.
├── api/
│   ├── handler.py                 # API endpoints
│   └── model_churn/
│       ├── __init__.py
│       └── model_churn.py         # Class with logic for loading and predicting
├── data/
│   ├── Abandono_clientes.csv      # Training data
│   └── Abandono_teste.csv         # Test data (unlabeled)
├── model/
│   ├── model_randomForest.pkl     # Optional trained model
│   └── model_xgboost.pkl          # Production model
├── requirements.txt               # Dependencies
├── Procfile                       # Deployment config for Render
```

---

## Running Locally

1. **Clone the repository:**

```bash
git clone https://github.com/fernandonast/churn-prediction-api.git
cd churn-prediction-api
```

2. **Create a virtual environment (optional):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the API locally:**

```bash
python api/handler.py
```
> ⚠️ You'll need to change some paths or at least revise them to run locally. These include paths to find `handler.py` or even the model. 
> 
> Generalizing it is in the next steps.
---

## 🌐 Production API

This application is deployed for free on **Render**, a modern cloud platform for hosting web apps, APIs, and services with continuous deployment from GitHub. You can use the endpoint below:

🔗 **https://deploy-ds.onrender.com/model_churn/predict**

Render supports Flask apps with Gunicorn and offers a free plan suitable for learning projects, prototypes, and small APIs.

---

## Example Request (Postman or cURL)

### `POST /predict`

#### Example JSON body:

Considering the initial problem of input by spreadsheet, below is an example:

```json
[
  {
    "CustomerId": 15795593,
    "Surname": "Chuang",
    "CreditScore": 651,
    "Geography": "Germany",
    "Gender": "Male",
    "Age": 24,
    "Tenure": 5,
    "Balance": 158484.85,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 161234.9
  },
    {
    "CustomerId": 15634602,
    "Surname": "Hargrave",
    "CreditScore": 619,
    "Geography": "France",
    "Gender": "Female",
    "Age": 42,
    "Tenure": 2,
    "Balance": 0,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 101348.88
  },
    {
    "CustomerId": 15699309,
    "Surname": "Gerasimov",
    "CreditScore": 510,
    "Geography": "Spain",
    "Gender": "Female",
    "Age": 38,
    "Tenure": 4,
    "Balance": 0,
    "NumOfProducts": 1,
    "HasCrCard": 1,
    "IsActiveMember": 0,
    "EstimatedSalary": 118913.53
  }
]
```

#### Expected Response:

```json
[
  {
      "CustomerId": 15795593,
      "Surname": "Chuang",
      "CreditScore": 651,
      "Geography": "Germany",
      "Gender": "Male",
      "Age": 24,
      "Tenure": 5,
      "Balance": 158484.85,
      "NumOfProducts": 1,
      "HasCrCard": 1,
      "IsActiveMember": 1,
      "EstimatedSalary": 161234.9,
      "predictedValues": 0
  },
  {
      "CustomerId": 15634602,
      "Surname": "Hargrave",
      "CreditScore": 619,
      "Geography": "France",
      "Gender": "Female",
      "Age": 42,
      "Tenure": 2,
      "Balance": 0.0,
      "NumOfProducts": 1,
      "HasCrCard": 1,
      "IsActiveMember": 1,
      "EstimatedSalary": 101348.88,
      "predictedValues": 1
  },
  {
      "CustomerId": 15699309,
      "Surname": "Gerasimov",
      "CreditScore": 510,
      "Geography": "Spain",
      "Gender": "Female",
      "Age": 38,
      "Tenure": 4,
      "Balance": 0.0,
      "NumOfProducts": 1,
      "HasCrCard": 1,
      "IsActiveMember": 0,
      "EstimatedSalary": 118913.53,
      "predictedValues": 0
  }
]
```

> ⚠️ The response includes the original data plus a `predictedValues` field indicating churn prediction (`1` for churn, `0` for retention).

---

## Author

- **Fernando Nast**
- [LinkedIn](https://www.linkedin.com/in/fernandonast)
- [GitHub](https://github.com/fernandonast)

---

## 📌 Notes

- Project developed for educational purposes to practice deploying Machine Learning models as RESTful APIs.
- The production model is based on the **XGBoost** algorithm.