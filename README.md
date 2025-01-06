# **Pipeline Leak Detection with Synthetic Data**

This project demonstrates a machine learning-based approach to pipeline leak detection, inspired by a study on acoustic emission (AE) sensors. The key steps include synthetic data generation, exploratory data analysis (EDA), and predictive modeling.

---

## **Project Highlights**
### **1. Synthetic Data Generation**
- Created data based on pipeline scenarios such as varying leak sizes and pressure levels.
- Features include time-domain and frequency-domain characteristics (e.g., mean frequency, variance, spectral kurtosis).


### **2. Exploratory Data Analysis (EDA)**
- Visualized feature distributions and relationships to understand patterns.
- Used scatter plots, box plots, and PCA for cluster visualization.
### Example images

#### Distribution:
![image](https://github.com/user-attachments/assets/0d9db767-01ab-403d-abbc-32ab989a7777)

#### Correlation:
![image](https://github.com/user-attachments/assets/217bb64b-3956-4193-9b06-1c51784ae2ab)

#### Plots:
![image](https://github.com/user-attachments/assets/1e397cf7-2087-4fb0-b3e7-54d0b94e1e57)



### **3. Predictive Modeling**
- Trained and evaluated multiple machine learning models:
  - Logistic Regression, Decision Tree, Random Forest, SVM, XGBoost.
- Used K-Folds Cross-Validation for robust evaluation.

---

## **Results**
- Successfully classified pipeline conditions (**leak vs. normal**).
- Achieved high performance with models like **Random Forest** and **XGBoost**.
- Demonstrated the effectiveness of using engineered features for leak detection.

#### Example results
![image](https://github.com/user-attachments/assets/c7cb1ddd-e487-4cea-aa2d-c7ece958a5ed)

## **Future Work**
To further enhance this project and refine the models, the following tasks are proposed:

1. **Hyperparameter Tuning**
   - Optimize model performance by systematically searching for the best hyperparameters using techniques like grid search or random search.

2. **Model Stacking**
   - Explore ensemble techniques, such as stacking, to combine the strengths of multiple models and potentially improve overall predictive accuracy.

---

## **Reference**
This project is inspired by the study **"Machine Learning-Based Acoustic Emission System for Pipeline Leak Detection"** published by MDPI Sensors.  
You can find the original paper [here](https://www.mdpi.com/1424-8220/23/6/3226?utm_source=chatgpt.com).
