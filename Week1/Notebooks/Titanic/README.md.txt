# Titanic Survival Prediction - iTech Internship

This project is part of my Week 1 internship learning tasks.  
The goal is to **analyze the Titanic dataset**, preprocess the data, train multiple machine learning models, and evaluate their performance for predicting passenger survival.

---

---

## 📝 Dataset

- **File:** `titanic.csv`
- **Description:** Contains passenger information and survival status (`Survived`: 0 = No, 1 = Yes)
- **Features:** Passenger class (`Pclass`), sex, age, fare, family info (`SibSp`, `Parch`), and port of embarkation

---

## 🔹 Steps in Notebook

### 1. Import Libraries
- Pandas, NumPy, Matplotlib, Seaborn  
- Scikit-learn: Logistic Regression, Random Forest, metrics, learning curves  
- XGBoost  

### 2. Data Exploration
- Displayed top rows (`df.head()`), dataset info (`df.info()`), and statistics (`df.describe()`)
- Checked and handled missing values (`Age`, `Embarked`)  
- Removed duplicates  

### 3. Preprocessing
- Dropped non-numeric or unnecessary columns (`PassengerId`, `Name`, `Ticket`, `Cabin`)  
- Encoded categorical features (`Sex`, `Embarked`, Age and Fare bins)  
- Added engineered features:
  - `FamilySize` = SibSp + Parch + 1  
  - `IsAlone` = 1 if `FamilySize` = 1 else 0  
- Scaled numerical features (`Age`, `Fare`, `FamilySize`)  

### 4. Correlation Heatmap
- Visualized correlation between numeric features

### 5. Model Training & Evaluation

#### Logistic Regression
- Trained on processed data  
- Metrics:
  - **Train Accuracy:** 0.8006  
  - **Test Accuracy:** 0.7989  
  - **F1 Score:** 0.75  
  - **ROC AUC:** 0.8844  

#### Random Forest
- Trained on processed data  
- Metrics:
  - **Train Accuracy:** 0.8610  
  - **Test Accuracy:** 0.8101  
  - **F1 Score:** 0.7463  
  - **ROC AUC:** 0.8927  

#### XGBoost
- Trained on processed data  
- Metrics:
  - **Train Accuracy:** 0.8890  
  - **Test Accuracy:** 0.8212  
  - **F1 Score:** 0.7647  
  - **ROC AUC:** 0.8878  

---

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
| Logistic Regression | 0.8006         | 0.7989        | 0.7500   | 0.8844  |
| Random Forest       | 0.8610         | 0.8101        | 0.7463   | 0.8927  |
| XGBoost             | 0.8890         | 0.8212        | 0.7647   | 0.8878  |

---

## 🛠️ Libraries Used
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
- `scikit-learn`  
- `xgboost`

---


