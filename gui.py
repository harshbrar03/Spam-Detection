import tkinter as tk
from tkinter import messagebox
import pickle

# Function to predict spam or ham
def predict_email(email_text):
    loaded_model = pickle.load(open("saving the model/spam_classifier.pkl", "rb"))
    loaded_vectorizer = pickle.load(open("saving the model/count_vectorizer.pkl", "rb"))
    
    # Preprocess and vectorize input email
    email_transformed = loaded_vectorizer.transform([email_text])
    
    # Predict
    prediction = loaded_model.predict(email_transformed)[0]
    return "Spam" if prediction == 1 else "Ham"

# Function to classify email from GUI
def classify_email():
    email_text = email_entry.get("1.0", tk.END).strip()  # Get user input
    if email_text:
        result = predict_email(email_text)
        result_label.config(text=f"Prediction: {result}", fg="red" if result == "Spam" else "green")
    else:
        messagebox.showwarning("Input Error", "Please enter an email text.")

# GUI Setup
root = tk.Tk()
root.title("Spam Email Detector")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="Spam Email Detector", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="blue")
title_label.pack(pady=10)

# Email Input Box
email_entry = tk.Text(root, height=5, width=50, font=("Arial", 12))
email_entry.pack(pady=10)

# Predict Button
predict_button = tk.Button(root, text="Check Email", font=("Arial", 12, "bold"), bg="blue", fg="white", command=classify_email)
predict_button.pack(pady=10)

# Prediction Result
result_label = tk.Label(root, text="Prediction: ", font=("Arial", 14), bg="#f4f4f4")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()