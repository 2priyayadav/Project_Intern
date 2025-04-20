import streamlit as st
import pandas as pd
from query_functions import query_handling_using_LLM_updated

st.set_page_config(page_title="SHL Assessment Recommendation System", layout="centered")

# 🌌 Styling + Header
st.markdown(
    """
    <style>
        html, body {
            background-color: #0e1117;
            color: #f0f2f6;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #1c1e24;
            color: #f0f2f6;
            border-radius: 8px;
            border: 1px solid #555;
        }
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #306998;
        }
        hr {
            border-top: 1px solid #444;
        }
    </style>
    <h1 style='text-align: center; color: #4B8BBE;'>🤖 SHL Assessment Recommender</h1>
    <h4 style='text-align: center; color: #aaa;'>Find the best assessment using AI!</h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# 🔍 User Input
query = st.text_input("🔍 Enter your search query here:", placeholder="e.g. Python SQL coding test")

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("🤔 Thinking... Fetching the best matches for you!"):
            try:
                df = query_handling_using_LLM_updated(query)

                if isinstance(df, pd.DataFrame) and not df.empty:
                    # 🧹 Clean and format the dataframe
                    df = df.drop_duplicates(subset=["Assessment Name", "Description"], keep="first")

                    if 'Score' in df.columns:
                        df = df.drop(columns=['Score'])

                    if "Duration" in df.columns:
                        df = df.rename(columns={"Duration": "Duration in mins"})

                    # Clean line breaks
                    df = df.replace({r'\n': ' ', r'\r': ' '}, regex=True)

                    # Format link
                    if 'URL' in df.columns:
                        df['URL'] = df['URL'].apply(lambda x: f"<a href='{x}' target='_blank'>🔗 View</a>" if pd.notna(x) else "")

                    # Reorder + display only valid columns
                    display_cols = ["Assessment Name", "Test Type", "Description", "Remote Testing Support", "Adaptive/IRT", "Duration in mins", "URL"]
                    df = df[[col for col in display_cols if col in df.columns]]

                    # ✅ Custom HTML Table
                    table_html = """
                    <style>
                        table.custom-table {
                            width: 100%;
                            border-collapse: separate;
                            border-spacing: 0;
                            font-family: 'Segoe UI', sans-serif;
                            font-size: 15px;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                            margin-top: 1rem;
                        }
                        table.custom-table thead {
                            background: linear-gradient(to right, #4B8BBE, #306998);
                            color: white;
                            font-weight: 600;
                        }
                        table.custom-table th, table.custom-table td {
                            padding: 14px 18px;
                            text-align: left;
                            vertical-align: top;
                        }
                        table.custom-table tbody tr {
                            background-color: #181c24;
                            color: #f0f2f6;
                            border-bottom: 1px solid #333;
                        }
                        table.custom-table tbody tr:nth-child(even) {
                            background-color: #1f242e;
                        }
                        table.custom-table tbody tr:hover {
                            background-color: #2a303c;
                        }
                        a {
                            color: #61dafb;
                            text-decoration: none;
                            font-weight: 500;
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                    </style>
                    <table class="custom-table">
                        <thead><tr>""" + "".join([f"<th>{col}</th>" for col in df.columns]) + "</tr></thead><tbody>"

                    for _, row in df.iterrows():
                        table_html += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"

                    table_html += "</tbody></table>"

                    st.success("✅ Here are your top assessment recommendations:")
                    st.markdown(table_html, unsafe_allow_html=True)

                else:
                    st.warning("😕 No assessments matched your query. Try rephrasing it!")

            except Exception as e:
                st.error(f"🚨 Something went wrong: {e}")
