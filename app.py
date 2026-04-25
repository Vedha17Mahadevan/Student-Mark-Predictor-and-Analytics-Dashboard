import streamlit as st

st.set_page_config(page_title="Student mark predictor", layout="wide")

# remove sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
.block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

st.title("Student mark predictor")

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("MARK DETAILS")

    num_subjects = st.number_input("Enter no. of subjects", 1, 10, 3)
    max_marks = st.number_input("Total marks per subject", 10, 100, 30)

    marks = []
    for i in range(int(num_subjects)):
        marks.append(
            st.number_input(f"Marks for subject {i+1}", 0, max_marks, key=i)
        )

    st.subheader("PERFORMANCE")

    attendance = st.number_input("Attendance (%)", 0, 100, 75)
    hours = st.number_input("Study per day (hrs)", 0, 12, 5)

    if st.button("Analyze"):
        st.session_state.data = {
            "marks": marks,
            "attendance": attendance,
            "hours": hours
        }
        st.switch_page("pages/results.py")

with col2:
    st.image("assets/predict.png", use_container_width=True)