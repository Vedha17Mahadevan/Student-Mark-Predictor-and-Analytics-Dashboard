import streamlit as st
import pandas as pd
from model import train_model, predict_marks

st.set_page_config(layout="wide")

# remove sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
.block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.title("Student mark predictor")

data = st.session_state.get("data", None)

if data is None:
    st.warning("Go back and enter details")
    st.stop()

marks = data["marks"]
attendance = data["attendance"]
hours = data["hours"]

model = train_model()

prediction, avg, max_m, min_m, var = predict_marks(
    model, hours, attendance, marks
)

# -------- RESULTS --------
st.subheader("RESULTS")

c1, c2, c3 = st.columns(3)

with c1:
    st.info(f"Average Score\n\n{avg:.2f}")

with c2:
    st.info(f"Predicted Marks\n\n{prediction:.2f}")

with c3:
    st.info(f"Attendance\n\n{attendance}%")

# -------- GRAPH --------
st.subheader("GRAPH")

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame({
        "Subjects": [f"S{i+1}" for i in range(len(marks))],
        "Marks": marks
    })
    st.bar_chart(df.set_index("Subjects"))

# -------- RECOMMENDATION --------
with col2:
    st.subheader("Recommendation")

    if prediction < 50:
        st.write("• Study basics more")
        st.write("• Increase study time")
    elif prediction < 75:
        st.write("• Practice regularly")
        st.write("• Improve weak subjects")
    else:
        st.write("• Maintain consistency")
        st.write("• Aim higher")

# -------- EXPLANATION --------
st.subheader("🧠 Why this prediction?")

if avg < 15:
    st.write("• Low average marks are reducing your score")

if min_m < 10:
    st.write("• Weak subject detected – penalty applied")

if var > 50:
    st.write("• High inconsistency in marks")

if attendance < 60:
    st.write("• Low attendance affects performance")

if hours < 3:
    st.write("• Study time is low")

if avg > 25 and attendance > 80:
    st.write("• Strong academic performance")
