# Heart Disease Prediction - iTech Internship

This project is part of my Week 1 internship learning tasks.  
The goal is to **analyze a heart disease dataset**, preprocess the data, train machine learning models, and evaluate their performance.

---

---

## 📝 Dataset

- **File:** `heart.csv`
- **Description:** Contains patient data for predicting heart disease (`target` column: 0 = no disease, 1 = disease)
- **Features:** Age, sex, blood pressure, cholesterol, etc.

---

## 🔹 Steps in Notebook

### 1. Import Libraries
- Pandas, NumPy, Matplotlib, Seaborn  
- Scikit-learn: Logistic Regression, Random Forest, metrics, learning curve  
- XGBoost  

### 2. Data Exploration
- Displayed top rows (`df.head()`), summary info (`df.info()`), and statistics (`df.describe()`)
- Checked for null values and duplicates, removed duplicates

### 3. Preprocessing
- Split features (`X`) and target (`y`)
- Scaled features using `StandardScaler`
- Split dataset into training and test sets

### 4. Correlation Heatmap
- Visualized correlations between features using Seaborn

### 5. Model Training & Evaluation

#### Logistic Regression
- Hyperparameter tuning using `GridSearchCV`
- Evaluated with **Train Accuracy: 0.8589
Test Accuracy: 0.8197, 0.8254, ROC 0.9267**

#### Random Forest
- Hyperparameter tuning using `GridSearchCV`
- Evaluated with **Train Accuracy: 0.9129
Test Accuracy: 0.8852, 0.8923, 0.945**

#### XGBoost
- Hyperparameter tuning using `GridSearchCV`
- Evaluated with **Random Forest:
Train Accuracy: 0.9419
Test Accuracy: 0.8525
,  0.8571, 0.9418**

### 6. ROC Curves
- Compared Logistic Regression, Random Forest, and XGBoost using ROC curves

### 7. Learning Curves
- Visualized training vs validation accuracy for each model

### 8. Confusion Matrices
- Displayed classification performance for each model

---

## 📊 Summary of Results

| Model                | Train Accuracy | Test Accuracy | F1 Score | ROC AUC |
|---------------------|----------------|---------------|----------|---------|
| Logistic Regression | 0.8589         | 0.8197        | 0.8254   | 0.9267  |
| Random Forest       | 0.9129         | 0.8852        | 0.8923   | 0.945   |
| XGBoost             | 0.9419         |  0.8525       | 0.8571   | 0.9418  |


---

## 🛠️ Libraries Used
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
- `scikit-learn`  
- `xgboost`

---


