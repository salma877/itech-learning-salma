# Bank Loan Prediction - iTech Internship

This project predicts whether a customer will accept a personal loan using a bank dataset.  
It explores the data, preprocesses it, trains Decision Tree and Random Forest models, and evaluates them using multiple metrics.

---

---

## 📝 Dataset

- **File:** `bankloan.csv`
- **Description:** Contains customer demographics and financial data  
- **Target Column:** `Personal.Loan` (0 = No, 1 = Yes)  
- **Features:** Age, Experience, Income, ZIP code, Family, CCAvg, Education, Mortgage, Securities Account, CD Account, Online, CreditCard

---

## 🔹 Steps in Notebook

### 1. Data Exploration
- Displayed top rows and dataset info (`df.head()`, `df.info()`)  
- Checked for missing values and duplicates  

### 2. Preprocessing
- Dropped unnecessary columns (`ID`, `ZIP.Code`)  
- Scaled numerical features using `StandardScaler`  
- Split dataset into training and testing sets  

### 3. Model Training & Hyperparameter Tuning

#### Decision Tree
- Hyperparameter tuning using `GridSearchCV`  
- Best parameters: `criterion='entropy'`, `max_depth=5`, `min_samples_split=2`  
- Train Accuracy: ~0.96  
- Test Accuracy: ~0.94  

#### Random Forest
- Hyperparameter tuning using `GridSearchCV`  
- Best parameters: `criterion='entropy'`, `n_estimators=50`, `max_depth=None`, `min_samples_split=2`  
- Train Accuracy: ~1.0  
- Test Accuracy: ~0.96  

---

### 4. Model Evaluation
- **Metrics:** Accuracy, F1 Score, ROC AUC  
- **Confusion Matrices:** Visualized using Seaborn heatmaps  

| Model          | Accuracy | F1 Score | ROC AUC |
|----------------|----------|----------|---------|
| Decision Tree  | 0.9400   | 0.9400   | 0.9600  |
| Random Forest  | 0.9600   | 0.9600   | 0.9800  |

---

### 5. Learning Curves
- Plotted training vs validation accuracy to visualize model performance  

### 6. Supabase Integration
- Results were inserted into a Supabase table named `model_results`  
- Each record contains: `model_name`, `accuracy`, `f1_score`, `roc_auc`  

```python
supabase.table("model_results").insert(results).execute()



