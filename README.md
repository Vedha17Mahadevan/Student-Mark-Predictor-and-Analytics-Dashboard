# 🎓 Student Marks Predictor & Analytics Dashboard

An end-to-end AI project that predicts student exam performance and visualizes usage analytics. This project demonstrates a **complete ML pipeline**:

Model Training → Web App → Data Collection → Business Intelligence Dashboard

---

## 🚀 Features

* Predict final exam marks using Machine Learning
* Interactive web interface (Streamlit)
* Automatic data logging of predictions
* Analytics dashboard (Power BI)
* Real-time performance insights

---

## 🧠 Machine Learning Model

Algorithm used: **Linear Regression**

### Input Features

* Hours Studied
* Attendance Percentage
* Internal Marks

### Output

* Predicted Final Marks

---

## 🏗️ System Architecture

```
Google Colab (Model Training)
        ↓
Trained Model (.pkl)
        ↓
Streamlit Web App (Prediction)
        ↓
CSV Database (records.csv)
        ↓
Power BI Dashboard (Analytics)
        ↓
Embedded inside Website
```

---

## 📂 Project Structure

```
student_ai_project/
│── app.py
│── student_marks_model.pkl
│── records.csv (auto-generated)
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone repository

```
git clone https://github.com/YOUR_USERNAME/student-marks-predictor.git
cd student-marks-predictor
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
streamlit run app.py
```

---

## 📊 Dashboard (Power BI)

The app stores every prediction in `records.csv`.

Power BI reads this file and creates:

* Average predicted marks
* Study hours vs performance
* Attendance vs performance
* Usage trends over time

---

## 🧪 Example Prediction

Input:

```
Hours Studied: 6
Attendance: 85%
Internal Marks: 22
```

Output:

```
Predicted Final Marks: 74.3
```

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas & NumPy
* Power BI

---

## 🎯 Learning Outcomes

This project demonstrates:

* Machine Learning model training
* Model deployment
* Data engineering
* Dashboard analytics

---

## 📌 Future Improvements

* Add user login system
* Store data in database (MySQL/Firebase)
* Improve model with more features
* Deploy online (Render/Streamlit Cloud)
