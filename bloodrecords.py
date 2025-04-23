import streamlit as st
import pandas as pd

# Initialize session state for 'data' if not already initialized
if "data" not in st.session_state:
    st.session_state["data"] = []

st.set_page_config(page_title="Blood Bank App", layout="centered")
st.title("🩸 Blood Bank Person Detail Storage")

# Form to input data
with st.form("blood_bank_form", clear_on_submit=True):
    st.subheader("➕ Add New Person")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)

    with col2:
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        contact = st.text_input("Contact Number")

    submitted = st.form_submit_button("Add Record")

    if submitted:
        if name.strip() and contact.strip():
            new_person = {
                "Name": name.strip().title(),
                "Age": age,
                "Blood Group": blood_group,
                "Contact": contact.strip()
            }
            st.session_state["data"].append(new_person)
            st.success(f"✅ {name} added successfully.")
        else:
            st.error("❗ Name and Contact are required fields.")

# Display section
if "data" in st.session_state and st.session_state["data"]:
    st.divider()
    st.subheader("📋 Blood Bank Records")

    # Search bar
    search_name = st.text_input("🔍 Search by name", "")

    # Convert data to DataFrame
    df = pd.DataFrame(st.session_state["data"])

    # Filter if search is used
    if search_name:
        filtered_df = df[df["Name"].str.contains(search_name, case=False, na=False)]
    else:
        filtered_df = df

    # Display count and table
    st.write(f"Total Records: {len(filtered_df)}")
    st.dataframe(filtered_df, use_container_width=True)

    # Option to clear all
    if st.button("🗑️ Clear All Records"):
        st.session_state["data"] = []
        st.warning("All records have been cleared.")
else:
    st.info("No records yet. Add a new person using the form above.")