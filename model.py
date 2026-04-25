import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def train_model():
    data = pd.read_csv("student_marks.csv")

    X = data[["Hours_Studied", "Attendance", "Avg", "Max", "Min", "Var"]]
    y = data["Final_Marks"]

    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    return model


def predict_marks(model, hours, attendance, marks):
    marks = np.array(marks)

    avg = np.mean(marks)
    max_m = np.max(marks)
    min_m = np.min(marks)
    var = np.var(marks)

    features = [[hours, attendance, avg, max_m, min_m, var]]

    prediction = model.predict(features)[0]

    return prediction, avg, max_m, min_m, var