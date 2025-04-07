# Version 1.0.0 

# import sys
# import os
# import time
# import pandas as pd
# import streamlit as st
# from io import BytesIO
# from fpdf import FPDF

# # -------------------------
# # Fix import path for custom modules
# ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# SRC_DIR = os.path.join(ROOT_DIR, "src")
# sys.path.insert(0, SRC_DIR)

# # -------------------------
# # Set page configuration as the first Streamlit command
# st.set_page_config(page_title="AI-Based Fraud Detector", layout="wide")

# # -------------------------
# # Import our custom modules
# from anomaly_detection import detect_anomalies
# from gemini_integration import get_explanation
# from utils import load_data

# # -------------------------
# # Inject custom CSS for a modern look
# st.markdown("""
#     <style>
#     body {
#         background-color: #f0f2f6;
#     }
#     h1, h2, h3, h4 {
#         color: #333333;
#     }
#     .stMarkdown p {
#         font-size: 16px;
#         line-height: 1.5;
#     }
#     .loading-spinner {
#         font-style: italic;
#         color: #555;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # -------------------------
# # Initialize session state for processing control
# if 'proceed' not in st.session_state:
#     st.session_state.proceed = False
# if 'filters_applied' not in st.session_state:
#     st.session_state.filters_applied = False

# # -------------------------
# # Detailed About Section
# if not st.session_state.proceed:
#     st.title("💰 AI-Based Financial Fraud Detector")
#     st.markdown("""
#     ## About This Tool
#     This tool leverages AI to analyze your financial transactions and detect unusual activity that may indicate fraud.
    
#     **Key Features:**
#     - **Automated Fraud Detection:** Uses anomaly detection techniques to flag unusual transactions.
#     - **Gemini AI Integration:** Provides clear, AI-generated explanations for flagged transactions upon request.
#     - **Data Flexibility:** Use our sample data or upload your own CSV file.
#     - **Dynamic Filtering & Sorting:** Filter transactions by amount, date, and anomaly status.
#     - **Detailed Transaction View:** Select a transaction for an in-depth view and generate a Gemini explanation on demand.
#     - **Interactive Report Generation:** Generate and download a comprehensive PDF report summarizing your transactions.
    
#     This tool is designed for quick analysis and transparency while ensuring controlled API usage for fair use.
#     """)
#     st.markdown("---")

# # -------------------------
# # Sidebar: Data Source Selection
# st.sidebar.subheader("📁 Data Source Selection")
# data_option = st.sidebar.radio("Select Data Source", options=["Use Sample Data", "Upload CSV File"])

# uploaded_file = None
# if data_option == "Upload CSV File":
#     uploaded_file = st.sidebar.file_uploader("Upload your transaction CSV", type=["csv"])

# # Only show the proceed button when either:
# # - Sample data is selected, or
# # - A file is uploaded when 'Upload CSV File' is selected.
# if data_option == "Use Sample Data" or (data_option == "Upload CSV File" and uploaded_file is not None):
#     if st.sidebar.button("Proceed"):
#         st.session_state.proceed = True
# else:
#     st.sidebar.info("Please upload your CSV file to proceed.")

# # -------------------------
# # Process Data Only After User Proceeds
# if st.session_state.proceed:
#     # Data loading
#     if data_option == "Upload CSV File":
#         df = pd.read_csv(uploaded_file)
#         st.sidebar.success("✅ File uploaded successfully!")
#     else:
#         sample_path = os.path.join(ROOT_DIR, "data", "transactions.csv")
#         df = load_data(sample_path)
#         st.sidebar.info("💡 Using sample transactions.csv")
    
#     # Check if data loaded properly
#     if df.empty:
#         st.error("❌ No data loaded. Please check your CSV file.")
#         st.stop()
    
#     # Run anomaly detection if not already present
#     if 'is_anomaly' not in df.columns:
#         df = detect_anomalies(df)
    
#     # -------------------------
#     # Sidebar: Dynamic Filtering & Sorting Section with Apply Button
#     st.sidebar.subheader("🔍 Filter & Sort Transactions")
#     min_amt = st.sidebar.number_input("Minimum Amount", min_value=0.0, value=float(df["Amount"].min()))
#     max_amt = st.sidebar.number_input("Maximum Amount", min_value=0.0, value=float(df["Amount"].max()))
#     show_anomalies_only = st.sidebar.checkbox("Show Anomalies Only", value=False)
    
#     # When Apply Filters is clicked, update session state.
#     if st.sidebar.button("Apply Filters"):
#         st.session_state.filters_applied = True
    
#     # If filters are applied, process and display the filtered dataframe
#     if st.session_state.filters_applied:
#         filtered_df = df[(df["Amount"] >= min_amt) & (df["Amount"] <= max_amt)]
#         if show_anomalies_only:
#             filtered_df = filtered_df[filtered_df["is_anomaly"] == True]
        
#         # Sorting options (only if there is data)
#         if not filtered_df.empty:
#             sort_column = st.sidebar.selectbox("Sort By", options=filtered_df.columns, index=filtered_df.columns.get_loc("Amount"))
#             sort_order = st.sidebar.radio("Sort Order", options=["Ascending", "Descending"])
#             filtered_df = filtered_df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))
#         else:
#             st.sidebar.warning("No data matches the filter criteria.")
        
#         # -------------------------
#         # Main Display: Filtered Transaction Data
#         st.subheader("📋 Filtered Transaction Data")
#         st.dataframe(filtered_df, use_container_width=True)
        
#         # -------------------------
#         # Detailed Transaction View with Button to Generate Gemini Explanation
#         st.subheader("🔎 Detailed Transaction View")
#         if not filtered_df.empty:
#             transaction_ids = filtered_df["TransactionID"].astype(str) if "TransactionID" in filtered_df.columns else filtered_df.index.astype(str)
#             selected_id = st.selectbox("Select Transaction ID", options=transaction_ids)
            
#             if "TransactionID" in filtered_df.columns:
#                 selected_row = filtered_df[filtered_df["TransactionID"].astype(str) == selected_id]
#             else:
#                 selected_row = filtered_df.loc[[int(selected_id)]]
            
#             st.markdown("**Transaction Details:**")
#             st.json(selected_row.to_dict(orient="records")[0])
            
#             # Button to generate Gemini explanation
#             if st.button("Generate Gemini Explanation"):
#                 st.markdown("**Gemini Explanation:**")
#                 explanation_placeholder = st.empty()
#                 with st.spinner("Gemini is processing the transaction..."):
#                     explanation = get_explanation(selected_row.iloc[0])
#                     # Simulate typing effect
#                     displayed_text = ""
#                     for char in explanation:
#                         displayed_text += char
#                         explanation_placeholder.markdown(f"{displayed_text}")
#                         time.sleep(0.02)
#         else:
#             st.info("No transactions available for detailed view.")
        
#         # -------------------------
#         # Interactive Report Generation
#         st.subheader("📄 Generate Report")
#         if st.button("Generate Report"):
#             # Generate a PDF report using FPDF
#             class PDF(FPDF):
#                 def header(self):
#                     self.set_font('Arial', 'B', 16)
#                     self.cell(0, 10, 'Fraud Detection Report', 0, 1, 'C')
#                     self.ln(10)
                
#                 def footer(self):
#                     self.set_y(-15)
#                     self.set_font('Arial', 'I', 8)
#                     self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
            
#             pdf = PDF()
#             pdf.add_page()
#             pdf.set_font("Arial", size=12)
#             pdf.cell(0, 10, f"Total Transactions: {len(df)}", ln=True)
#             pdf.cell(0, 10, f"Anomalies Detected: {int(df['is_anomaly'].sum())}", ln=True)
#             pdf.cell(0, 10, f"Minimum Amount: {df['Amount'].min()}", ln=True)
#             pdf.cell(0, 10, f"Maximum Amount: {df['Amount'].max()}", ln=True)
#             pdf.ln(10)
#             pdf.multi_cell(0, 10, "This report summarizes the fraud detection results based on the current dataset.")
            
#             # Generate PDF as string and then encode to bytes
#             pdf_str = pdf.output(dest='S')    # <-- Changed: Using dest='S' to get PDF as a string
#             pdf_bytes = pdf_str.encode('latin1')   # <-- Changed: Encoding the string to bytes using 'latin1'

#             st.download_button(
#                 label="Download Report as PDF",
#                 data=pdf_bytes,
#                 file_name="fraud_detection_report.pdf",
#                 mime="application/pdf"
#             )
#             st.success("Report generated successfully!")
#     else:
#         st.info("Please adjust filters and click **Apply Filters** to update the results.")
# else:
#     st.info("Please select a data source and click **Proceed** from the sidebar to begin processing.")



# Version 2.0.0(Checked)

import sys
import os
import time
import pandas as pd
import streamlit as st
from io import BytesIO
from fpdf import FPDF

# -------------------------
# Fix import path for custom modules
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.insert(0, SRC_DIR)

# -------------------------
# Set page configuration as the first Streamlit command
st.set_page_config(page_title="AI-Based Fraud Detector", layout="wide")

# -------------------------
# Import our custom modules
from anomaly_detection import detect_anomalies
from gemini_integration import get_explanation
from utils import load_data

# -------------------------
# Inject custom CSS for a modern look
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    h1, h2, h3, h4 {
        color: #333333;
    }
    .stMarkdown p {
        font-size: 16px;
        line-height: 1.5;
    }
    .loading-spinner {
        font-style: italic;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------
# Initialize session state for processing control
if 'proceed' not in st.session_state:
    st.session_state.proceed = False
if 'filters_applied' not in st.session_state:
    st.session_state.filters_applied = False
if 'gemini_explanation' not in st.session_state:
    st.session_state.gemini_explanation = None

# -------------------------
# Detailed About Section
if not st.session_state.proceed:
    st.title("💰 AI-Based Financial Fraud Detector")
    st.markdown("""
    ## About This Tool
    This tool leverages AI to analyze your financial transactions and detect unusual activity that may indicate fraud.

    **Key Features:**
    - **Automated Fraud Detection:** Uses anomaly detection techniques to flag unusual transactions.
    - **Gemini AI Integration:** Provides clear, AI-generated explanations for flagged transactions upon request.
    - **Data Flexibility:** Use our sample data or upload your own CSV file.
    - **Dynamic Filtering & Sorting:** Filter transactions by amount, date, and anomaly status.
    - **Detailed Transaction View:** Select a transaction for an in-depth view and generate a Gemini explanation on demand.
    - **Interactive Report Generation:** Generate and download a comprehensive PDF report summarizing your transactions.

    This tool is designed for quick analysis and transparency while ensuring controlled API usage for fair use.
    """)
    st.markdown("---")

# -------------------------
# Sidebar: Data Source Selection
st.sidebar.subheader("📁 Data Source Selection")
data_option = st.sidebar.radio("Select Data Source", options=["Use Sample Data", "Upload CSV File"])

uploaded_file = None
if data_option == "Upload CSV File":
    uploaded_file = st.sidebar.file_uploader("Upload your transaction CSV", type=["csv"])

if data_option == "Use Sample Data" or (data_option == "Upload CSV File" and uploaded_file is not None):
    if st.sidebar.button("Proceed"):
        st.session_state.proceed = True
else:
    st.sidebar.info("Please upload your CSV file to proceed.")

# -------------------------
# Process Data Only After User Proceeds
if st.session_state.proceed:
    if data_option == "Upload CSV File":
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("✅ File uploaded successfully!")
        else:
            st.warning("⚠️ Please upload a CSV file to proceed.")
            st.stop()
    else:
        sample_path = os.path.join(ROOT_DIR, "data", "transactions.csv")
        df = load_data(sample_path)
        st.sidebar.info("💡 Using sample transactions.csv")

    if df.empty:
        st.error("❌ No data loaded. Please check your CSV file.")
        st.stop()

    if 'is_anomaly' not in df.columns:
        df = detect_anomalies(df)

    st.sidebar.subheader("🔍 Filter & Sort Transactions")
    min_amt = st.sidebar.number_input("Minimum Amount", min_value=0.0, value=float(df["Amount"].min()))
    max_amt = st.sidebar.number_input("Maximum Amount", min_value=0.0, value=float(df["Amount"].max()))
    show_anomalies_only = st.sidebar.checkbox("Show Anomalies Only", value=False)

    if st.sidebar.button("Apply Filters"):
        st.session_state.filters_applied = True

    if st.session_state.filters_applied:
        filtered_df = df[(df["Amount"] >= min_amt) & (df["Amount"] <= max_amt)]
        if show_anomalies_only:
            filtered_df = filtered_df[filtered_df["is_anomaly"] == True]

        if not filtered_df.empty:
            sort_column = st.sidebar.selectbox("Sort By", options=filtered_df.columns, index=filtered_df.columns.get_loc("Amount"))
            sort_order = st.sidebar.radio("Sort Order", options=["Ascending", "Descending"])
            filtered_df = filtered_df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))
        else:
            st.sidebar.warning("No data matches the filter criteria.")

        st.subheader("📋 Filtered Transaction Data")
        st.dataframe(filtered_df, use_container_width=True)

        st.subheader("🔎 Detailed Transaction View")
        if not filtered_df.empty:
            transaction_ids = filtered_df["TransactionID"].astype(str) if "TransactionID" in filtered_df.columns else filtered_df.index.astype(str)
            selected_id = st.selectbox("Select Transaction ID", options=transaction_ids)

            if "TransactionID" in filtered_df.columns:
                selected_row = filtered_df[filtered_df["TransactionID"].astype(str) == selected_id]
            else:
                selected_row = filtered_df.loc[[int(selected_id)]]

            st.markdown("**Transaction Details:**")
            st.json(selected_row.to_dict(orient="records")[0])

            if st.button("Generate Gemini Explanation"):
                st.markdown("**Gemini Explanation:**")
                explanation_placeholder = st.empty()
                with st.spinner("Gemini is processing the transaction..."):
                    explanation = get_explanation(selected_row.iloc[0])
                    st.session_state['gemini_explanation'] = explanation
                    displayed_text = ""
                    for char in explanation:
                        displayed_text += char
                        explanation_placeholder.markdown(f"{displayed_text}")
                        time.sleep(0.02)
        else:
            st.info("No transactions available for detailed view.")

        # -------------------------
        # Show Generate Report button only after Gemini explanation is generated
        if st.session_state.gemini_explanation:
            st.subheader("📄 Generate Report")
            if st.button("Generate Report"):
                class PDF(FPDF):
                    def header(self):
                        self.set_font('Arial', 'B', 16)
                        self.cell(0, 10, 'Fraud Detection Report', 0, 1, 'C')
                        self.ln(10)

                    def footer(self):
                        self.set_y(-15)
                        self.set_font('Arial', 'I', 8)
                        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

                pdf = PDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, f"Total Transactions: {len(df)}", ln=True)
                pdf.cell(0, 10, f"Anomalies Detected: {int(df['is_anomaly'].sum())}", ln=True)
                pdf.cell(0, 10, f"Minimum Amount: {df['Amount'].min()}", ln=True)
                pdf.cell(0, 10, f"Maximum Amount: {df['Amount'].max()}", ln=True)
                pdf.ln(10)
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(0, 10, "Gemini Explanation:", ln=True)
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, st.session_state['gemini_explanation'])
                pdf.ln(10)
                pdf.multi_cell(0, 10, "This report summarizes the fraud detection results and includes the Gemini generated explanation for the selected transaction.")

                pdf_str = pdf.output(dest='S')
                pdf_bytes = pdf_str.encode('latin1')

                st.download_button(
                    label="Download Report as PDF",
                    data=pdf_bytes,
                    file_name="fraud_detection_report.pdf",
                    mime="application/pdf"
                )
                st.success("Report generated successfully!")
    else:
        st.info("Please adjust filters and click **Apply Filters** to update the results.")
else:
    st.info("Please select a data source and click **Proceed** from the sidebar to begin processing.")
