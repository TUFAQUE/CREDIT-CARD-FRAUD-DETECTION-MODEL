# 💳 Credit Card Fraud Detection — From Notebook to Production

> Forked from [Tufaque Sayyed's](https://github.com/tufaquesayyed) original research notebook. The goal was stated but never finished — deploy it. So I did.

🌐 **Live at:** [credit-card-fraud-detection-model-ashen.vercel.app](https://credit-card-fraud-detection-model-ashen.vercel.app/)

---

<img width="1745" height="865" alt="image" src="https://github.com/user-attachments/assets/c41c56e4-bb4c-405f-900b-d87a1ce08730" />

---

## What I Built On Top

The original repo had a solid Jupyter notebook — good model, good evaluation, but no deployment. I opened an issue, then went ahead and built the whole thing out.

Here's what changed:

**Model Extraction & Packaging**
- Pulled the trained XGBoost model and both StandardScaler instances out of the notebook
- Wrapped the scalers in a `ColumnTransformer` (sklearn) to handle them cleanly as a unit
- Chained that into a full sklearn `Pipeline` alongside XGBoost
- Serialized everything into a single `.joblib` file — one artifact, no state drift

**Backend**
- Built a FastAPI backend exposing prediction endpoints
- Supports both single-transaction and batch inference (up to 100 rows)
- Deployed on **Render**

**Frontend**
- Clean, minimal HTML/CSS frontend — no framework bloat
- Two input modes: manual entry (all 30 features) and CSV upload for batch runs
- Each prediction shows **model confidence (probability)**, the **threshold** used, and the **final verdict**
- Live inference log — every prediction per batch is streamed and displayed in real time
- No login, no friction
- Deployed on **Vercel**

---

<img width="1523" height="846" alt="image" src="https://github.com/user-attachments/assets/32443963-e4e4-4373-ac0d-05e19af8b14d" />

---

## Original Model (unchanged)

| Detail | Value |
|---|---|
| Algorithm | XGBoost Classifier |
| Dataset | [Kaggle Credit Card Fraud](https://www.kaggle.com/mlg-ulb/creditcardfraud) — European cardholders, 2013 |
| Features | Time, Amount, V1–V28 (PCA-transformed) |
| Imbalance handling | SMOTE oversampling |
| ROC-AUC | ~0.98 |

The dataset is heavily skewed toward legitimate transactions. SMOTE was used during training to give the model a fair shot at learning fraud patterns without just predicting "not fraud" for everything.

---

## How the Pipeline Works

```
Raw Input (30 features)
       ↓
ColumnTransformer → StandardScaler on [Time, Amount]
       ↓
XGBoost Classifier
       ↓
Probability + Threshold → Final Prediction
```

Keeping the scalers inside the pipeline means the same preprocessing that happened during training happens at inference — no manual scaling step that could drift or get forgotten.

---

## Repo Structure

```
📂 credit-card-fraud-detection/
│
├── 📄 CreditCardModel.ipynb        # Original notebook (model training)
├── 📄 model_pipeline.joblib        # Exported sklearn Pipeline
│
├── 📂 backend/
│   ├── main.py                     # FastAPI app
│   ├── requirements.txt
│   └── ...
│
├── 📂 frontend/
│   ├── index.html                  # Prediction UI
│   ├── sample_transactions_100.csv
│
└── 📄 README.md
│   └── ...
```

---

<img width="1448" height="816" alt="image" src="https://github.com/user-attachments/assets/13b48a6a-6970-4905-9c02-367e65491260" />

---

## Running It Locally

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**

Just open `frontend/index.html` in a browser, or point it at your local FastAPI instance.

---

## What's Left (Honest To-Do)

- [ ] SHAP values for per-prediction explainability
- [ ] Auth layer if this ever needs to be multi-tenant
- [ ] Threshold tuning UI (let users adjust the decision boundary)
- [ ] Better error messages for malformed CSVs

---

## Original Work

Model, training pipeline, and research by **Tufaque Sayyed**
🌐 [Portfolio](https://tufaquesayyed.vercel.app)

Deployment, packaging, and frontend by **[Arjun Gupta]**
[GitHub](https://github.com/Neural-GPT)

---

📜 MIT License — use it, fork it, improve it.
