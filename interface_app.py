import streamlit as st
import pandas as pd

# Load the Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("road_maintenance_rulebase.xlsx")
    return df

df = load_data()

st.title("🛠️ Road Maintenance Expert System")

# Input fields
distress_type = st.selectbox("Distress Type", df["Distress Type"].unique())
severity = st.selectbox("Severity", df["Severity"].unique())
traffic_type = st.selectbox("Traffic Type", df["Traffic Type"].unique())
budget_level = st.selectbox("Budget Level", df["Budget Level"].unique())
material = st.selectbox("Material", df["Material"].unique())

# Filter the rulebase
filtered = df[
    (df["Distress Type"] == distress_type) &
    (df["Severity"] == severity) &
    (df["Traffic Type"] == traffic_type) &
    (df["Budget Level"] == budget_level) &
    (df["Material"] == material)
]

# Show output
if not filtered.empty:
    st.subheader("🧾 Recommended Treatment")
    st.write("**Treatment:**", filtered.iloc[0]["Treatment"])
    st.write("**Procedure:**", filtered.iloc[0]["Procedure"])
    st.write("**Cost per m²:**", filtered.iloc[0]["Cost_per_m2"])
    st.write("**Time Required:**", filtered.iloc[0]["Time"])
    st.write("**Manpower:**", filtered.iloc[0]["Manpower"])
    st.write("**Equipment Needed:**", filtered.iloc[0]["Equipment"])
    st.write("**IRC Code:**", filtered.iloc[0]["IRC_Code"])
else:
    st.warning("No matching treatment found for the selected inputs.")
