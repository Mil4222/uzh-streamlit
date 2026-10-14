import streamlit as st
import pandas as pd

# --- Title and text ---
st.title("University of Zurich")
st.markdown("### Study programs explorer")
st.markdown("UZH was founded in **1833**. This app shows a small selection of study programs and lets you **filter** them.")
st.markdown("*Note: small example dataset, typed in by hand.*")

# --- Data ---
data = {
    "program": ["Economics", "Business Administration", "Law", "Medicine",
                "Psychology", "Informatics", "Biology",
                "Economics", "Banking and Finance", "Informatics", "Psychology", "Law"],
    "faculty": ["Economics", "Economics", "Law", "Medicine",
                "Arts and Social Sciences", "Science", "Science",
                "Economics", "Economics", "Science", "Arts and Social Sciences", "Law"],
    "level": ["Bachelor", "Bachelor", "Bachelor", "Bachelor",
              "Bachelor", "Bachelor", "Bachelor",
              "Master", "Master", "Master", "Master", "Master"],
}
df = pd.DataFrame(data)

# --- Show all data ---
st.markdown("## All study programs")
st.dataframe(df)

# --- Filter 1: radio ---
st.markdown("## Filter by degree level")
level = st.radio("Which level?", ["All", "Bachelor", "Master"])
if level == "All":
    filtered = df
else:
    filtered = df[df["level"] == level]
st.dataframe(filtered)

# --- Filter 2: multiselect ---
st.markdown("## Filter by faculty")
faculties = st.multiselect("Choose faculties:", df["faculty"].unique(), default=["Economics"])
st.dataframe(df[df["faculty"].isin(faculties)])
