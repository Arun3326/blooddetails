import streamlit as st
import pandas as pd

# Initialize session state for data storage if it doesn't exist
if 'data' not in st.session_state:
    st.session_state.data = []

st.title("🩸 Blood Bank Person Detail Storage")

# Input form
with st.form("blood_bank_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    contact = st.text_input("Contact Number")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and contact:
            person = {
                "Name": name,
                "Age": age,
                "Blood Group": blood_group,
                "Contact": contact
            }
            st.session_state.data.append(person)
            st.success("✅ Person details added!")
        else:
            st.error("❗ Please fill in all required fields.")

# Optional: Button to clear data
if st.button("Clear All Records"):
    st.session_state.data = []
    st.warning("🗑️ All records cleared.")