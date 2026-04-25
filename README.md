# 🎓 Student Performance Analyzer

A smart, interactive web app that predicts student performance based on academic behavior and provides insights on how to improve.

---

## 🚀 Features

- 📊 Predict final marks based on:
  - Study hours
  - Attendance
  - Subject-wise marks

- 🧠 Intelligent analysis using:
  - Average performance
  - Weakest subject detection
  - Consistency (variance)
  - Effort & discipline factors

- 📈 Visual insights:
  - Subject-wise performance graph

- 💡 Explainable results:
  - Shows *why* a prediction was made
  - Highlights weak areas and improvement suggestions

---

## 🧠 How it Works

The model uses a combination of:

- Feature engineering:
  - Average marks
  - Maximum & minimum marks
  - Variance (consistency)
  - Study hours
  - Attendance

- Machine Learning:
  - Random Forest Regressor

- Simulated dataset with realistic patterns:
  - Weak subject penalties
  - Consistency penalties
  - Real-world noise

---

## 📁 Project Structure

``` bash
project/
│
├── app.py # Input page
├── model.py # ML model
├── generate_data.py # Dataset generator
├── student_marks.csv # Generated dataset
│
├── pages/
│ └── results.py # Results + analytics
│
├── assets/
│ └── predict.png # UI image
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-performance-analyzer.git
cd student-performance-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate dataset

```bash
python generate_data.py
```

### 4. Run the app

```bash
streamlit run app.py
```
