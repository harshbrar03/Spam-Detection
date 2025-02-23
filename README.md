
# 📧 **Spam Detection Using Machine Learning**

## 📝 **Project Overview**
This project focuses on developing an efficient **Spam Detection System** that classifies email messages as **Spam** or **Ham (Non-Spam)** using **Machine Learning** techniques. Built in **Python**, the project integrates a user-friendly **Tkinter-based GUI** to enable users to test the model in real-time.

## 🎯 **Project Objectives**
- Detect spam messages with high accuracy.
- Preprocess raw email text data for machine learning models.
- Develop an interpretable and deployable spam detection model.
- Provide an intuitive **Tkinter GUI** for seamless user interaction.

## 📂 **Project Structure:**
```
├── main.ipynb              # Jupyter Notebook with model development & analysis
├── saving the model/       # Contains saved model and vectorizer files
│   ├── spam_classifier.pkl
│   └── count_vectorizer.pkl
├── gui.py                  # Tkinter-based GUI application
└── README.md               # Project documentation (this file)
```

## 🛠️ **Approach & Methodology**
### **1. Data Preprocessing:**
- Converted text to lowercase.
- Removed punctuation, special characters, and numeric values.
- Eliminated common stopwords (e.g., "the", "is", "and").
- Applied stemming using **PorterStemmer** to reduce words to their base forms.

### **2. Feature Extraction:**
- Utilized **CountVectorizer** to convert text into numerical vectors.
- Selected the top 5,000 features to ensure model efficiency.

### **3. Model Selection & Training:**
- Chose **Multinomial Naïve Bayes (MNB)** for its effectiveness in text classification tasks.
- Split the dataset (5,572 emails) into **80% training** and **20% testing** using **stratified sampling** to preserve class distribution.

### **4. Model Evaluation:**
- Achieved a high **accuracy of 96.86%**.
- Maintained a **spam recall of 91%**, ensuring most spam emails were detected.
- Evaluated model performance using a **confusion matrix** and **classification report**.

### **5. Deployment & GUI:**
- Saved the trained model and vectorizer using **Pickle** for future use.
- Developed a **Tkinter-based GUI** where users can input email text and instantly receive a classification result (Spam or Ham).

## 📊 **Results & Performance**
- **Accuracy:** 96.86%
- **Spam Recall:** 91%
- **Precision:** 87%
- **Confusion Matrix:**
  ```
  [[945  21]  # 21 ham emails misclassified as spam
   [ 14 135]] # 14 spam emails misclassified as ham
  ```

## 🚀 **Key Highlights:**
- Efficient spam detection with minimal false negatives.
- Easy-to-use GUI for real-time email classification.
- Clean, well-documented, and production-ready code.

## 🏆 **Acknowledgments:**
- Dataset sourced from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).

