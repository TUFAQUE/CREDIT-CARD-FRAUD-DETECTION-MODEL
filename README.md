# 💳 Credit Card Fraud Detection using Machine Learning

### 🚀 Project Overview

This project aims to **detect fraudulent credit card transactions** using advanced **Machine Learning techniques**.
Financial fraud is one of the most critical issues banks face, and this model helps identify suspicious transactions based on past data.
We’ve used **XGBoost**, **SMOTE**, and **evaluation metrics like ROC-AUC** to build a robust classification system.

---

## 🧠 Key Highlights

* **Algorithm Used:** XGBoost Classifier
* **Challenge Tackled:** Highly imbalanced dataset
* **Techniques:** Data scaling, SMOTE oversampling, ROC-AUC evaluation
* **Goal:** Build a reliable model to classify fraud vs. non-fraud transactions

---

## 🧩 Dataset

* **Source:** [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
* The dataset contains transaction details made by European cardholders in 2013.
* It includes **Time**, **Amount**, and **PCA-transformed features (V1–V28)** to preserve confidentiality.
* `Class` column →

  * `0`: Normal Transaction
  * `1`: Fraudulent Transaction

---

## 🛠️ Installation & Requirements

Before running the notebook, make sure you have the required libraries installed:

```bash
!pip install xgboost imbalanced-learn
```

You can also install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📘 File Structure

```
📂 Credit-Card-Fraud-Detection/
│
├── 📄 CreditCardModel.ipynb       # Main Jupyter Notebook
├── 📄 README.md                   # Project Documentation
└── 📄 requirements.txt            # (optional) Library list
```

---

## 🧪 Workflow Summary

| Step                      | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **1. Data Loading**       | Imported and explored dataset from Kaggle        |
| **2. Preprocessing**      | Scaled numerical features using StandardScaler   |
| **3. Handling Imbalance** | Used SMOTE to balance minority (fraud) class     |
| **4. Model Building**     | Trained **XGBoost Classifier**                   |
| **5. Evaluation**         | ROC-AUC, Confusion Matrix, Classification Report |
| **6. Testing**            | Custom input example to check model predictions  |

---

## 📊 Model Performance

| Metric                | Score                          |
| --------------------- | ------------------------------ |
| **ROC-AUC**           | ~0.98                          |
| **Precision (Fraud)** | High (depending on seed)       |
| **Recall (Fraud)**    | High — minimal false negatives |

---

## 🧾 Example Prediction

You can test the model by giving a **random transaction sample** and see if it predicts *fraudulent* or *legitimate*:

```python
sample = X_test.iloc[0].values.reshape(1, -1)
prediction = model.predict(sample)
print("🔍 Predicted:", "Fraud" if prediction[0] == 1 else "Not Fraud")
```

---

## 🧠 Learning Outcomes

* Real-world application of **classification models** on imbalanced data
* Hands-on with **SMOTE**, **XGBoost**, and **evaluation plots**
* Understanding **ROC**, **Precision-Recall**, and **Confusion Matrix** interpretation

---

## 🌟 Future Improvements

* Add **real-time transaction monitoring**
* Deploy as a **web dashboard (Streamlit / FastAPI)**
* Integrate **Explainability (SHAP values)** for interpretability

---

## 👨‍💻 Author

**Tufaque Sayyed**
🎓 B.Tech in Artificial Intelligence & Machine Learning
🔗 [LinkedIn Profile](https://www.linkedin.com/in/tufaque-sayyed-843596364/)
🌐 [Portfolio Website](https://tufaquesayyed.vercel.app)

---

## 📜 License

This project is open-sourced under the **MIT License**. Feel free to use and modify it with proper credits.

---

### ⭐ If you found this project useful, don’t forget to star the repo!

