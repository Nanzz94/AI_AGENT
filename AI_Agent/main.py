import streamlit as st
import pandas as pd
from utils import extract_information_from_groq

# Set up the Streamlit app
st.title("Information Retrieval Agent")

# Step 1: Upload CSV file
st.header("Step 1: Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("File Uploaded Successfully!")
    st.write("Preview of Data:", data.head())

    # Step 2: Select Main Column
    st.header("Step 2: Select Main Column")
    columns = data.columns.tolist()
    main_column = st.selectbox("Select the main column (e.g., company names)", columns)

    # Step 3: Enter Custom Query
    st.header("Step 3: Define Custom Query")
    query_template = st.text_input(
        "Enter your query template (e.g., 'Get the email and address for {company}')"
    )

    # Confirm column and query
    if main_column and query_template:
        st.write(f"Selected Column: {main_column}")
        st.write(f"Query Template: {query_template}")

        # Step 4: Run Information Retrieval
        if st.button("Run Information Retrieval"):
            # Get the list of entities from the selected column
            entities = data[main_column].unique().tolist()
            results_df = extract_information_from_groq(entities, query_template)  # Call function with list of entities and query template

            # Display extracted information
            st.write("Extracted Information:", results_df)

            # Step 5: Download CSV
            st.download_button(
                label="Download Results as CSV",
                data=results_df.to_csv(index=False),
                file_name="extracted_data.csv",
                mime="text/csv"
            )
