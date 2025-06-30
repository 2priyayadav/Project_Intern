# import streamlit as st
# import pandas as pd
# from query_functions import query_handling_using_LLM_updated
# # from bs4 import BeautifulSoup


# st.set_page_config(page_title="SHL Assessment Recommendation System", layout="centered")

# st.markdown(
#     """
#     <style>
#         html, body {
#             background-color: #0e1117;
#             color: #f0f2f6;
#             font-family: 'Segoe UI', sans-serif;
#         }
#         .main {
#             padding: 2rem;
#         }
#         .stTextInput > div > div > input {
#             background-color: #1c1e24;
#             color: #f0f2f6;
#             border-radius: 8px;
#             border: 1px solid #555;
#         }
#         .stButton>button {
#             background-color: #4B8BBE;
#             color: white;
#             font-weight: bold;
#             border-radius: 8px;
#             padding: 0.5rem 1.5rem;
#             border: none;
#         }
#         .stButton>button:hover {
#             background-color: #306998;
#         }
#         hr {
#             border-top: 1px solid #444;
#         }
#     </style>
#     <h1 style='text-align: center; color: #4B8BBE;'>🤖 SHL Assessment Recommender</h1>
#     <h4 style='text-align: center; color: #aaa;'>Find the best assessment using AI! :)</h4>
#     <hr>
#     """,
#     unsafe_allow_html=True
# )

# query = st.text_input("🔍 Enter your search query here:", placeholder="e.g. Python SQL coding test")

# if st.button("Search"):
#     if query.strip() == "":
#         st.warning("Please enter a valid query.")
#     else:
#         with st.spinner("🤔 Thinking... Fetching the best matches for you!"):
#             try:
#                 df = query_handling_using_LLM_updated(query)

#                 if isinstance(df, pd.DataFrame) and not df.empty:
#                     if 'Score' in df.columns:
#                         df = df.drop(columns=['Score'])

#                     if "Duration" in df.columns:
#                         df = df.rename(columns={"Duration": "Duration in mins"})

#                     display_cols = ["Assessment Name", "Test Type", "Description", "Remote Testing Support", "Adaptive/IRT", "Duration in mins", "URL"]
#                     df = df[[col for col in display_cols if col in df.columns]]

#                     df['URL'] = df['URL'].apply(lambda x: f"<a href='{x}' target='_blank'>🔗 View</a>" if pd.notna(x) else "")

#                     st.success("✅ Here are your top assessment recommendations:")

#                     table_html = """
#                     <style>
#                         table.custom-table {
#                             width: 100%;
#                             border-collapse: separate;
#                             border-spacing: 0;
#                             font-family: 'Segoe UI', sans-serif;
#                             font-size: 15px;
#                             border-radius: 12px;
#                             overflow: hidden;
#                             box-shadow: 0 4px 12px rgba(0,0,0,0.3);
#                             margin-top: 1rem;
#                         }
#                         table.custom-table thead {
#                             background: linear-gradient(to right, #4B8BBE, #306998);
#                             color: white;
#                             font-weight: 600;
#                         }
#                         table.custom-table th, table.custom-table td {
#                             padding: 14px 18px;
#                             text-align: left;
#                             vertical-align: top;
#                         }
#                         table.custom-table tbody tr {
#                             background-color: #181c24;
#                             color: #f0f2f6;
#                             border-bottom: 1px solid #333;
#                         }
#                         table.custom-table tbody tr:nth-child(even) {
#                             background-color: #1f242e;
#                         }
#                         table.custom-table tbody tr:hover {
#                             background-color: #2a303c;
#                         }
#                         a {
#                             color: #61dafb;
#                             text-decoration: none;
#                             font-weight: 500;
#                         }
#                         a:hover {
#                             text-decoration: underline;
#                         }
#                     </style>
#                     <table class="custom-table">
#                         <thead>
#                             <tr>
#                     """

#                     for col in df.columns:
#                         table_html += f"<th>{col}</th>"
#                     table_html += "</tr></thead><tbody>"

#                     for _, row in df.iterrows():
#                         table_html += "<tr>"
#                         for cell in row:
#                             table_html += f"<td>{cell}</td>"
#                         table_html += "</tr>"

#                     table_html += "</tbody></table>"

#                     st.markdown(table_html, unsafe_allow_html=True)

#                 else:
#                     st.warning("😕 No assessments matched your query. Try rephrasing it!")

#             except Exception as e:
#                 st.error(f"🚨 Something went wrong: {e}")






# import streamlit as st
# import pandas as pd
# from query_functions import query_handling_using_LLM_updated
# from streamlit_lottie import st_lottie
# import requests

# # ------------------ Streamlit Config ------------------ #
# st.set_page_config(
#     page_title="SHL Assessment Recommendation System",
#     layout="wide",
#     page_icon="🤖"
# )

# # ------------------ Load Lottie Animation ------------------ #
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_robot = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tutvdkg0.json")
# lottie_background = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_dgjK9H.json")

# # ------------------ Custom Styling ------------------ #
# st.markdown(
#     """
#     <style>
#         html, body {
#             background-color: #0e1117;
#             color: #f0f2f6;
#             font-family: 'Segoe UI', sans-serif;
#         }
#         body {
#             background-image: radial-gradient(#2a303c 1px, transparent 1px);
#             background-size: 20px 20px;
#         }
#         .main {
#             padding: 2rem;
#         }
#         .stTextInput > div > div > input,
#         .stSelectbox > div > div > div {
#             background-color: #1c1e24;
#             color: #f0f2f6;
#             border-radius: 8px;
#             border: 1px solid #555;
#         }
#         .stButton>button {
#             background-color: #4B8BBE;
#             color: white;
#             font-weight: bold;
#             border-radius: 8px;
#             padding: 0.5rem 1.5rem;
#             border: none;
#         }
#         .stButton>button:hover {
#             background-color: #306998;
#         }
#         hr {
#             border-top: 1px solid #444;
#             margin-top: 2rem;
#             margin-bottom: 2rem;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ------------------ Header Section ------------------ #
# col1, col2 = st.columns([1, 2])
# with col1:
#     st_lottie(lottie_robot, height=180)
# with col2:
#     st.markdown("<h1 style='color: #4B8BBE;'>🤖 SHL Assessment Recommender</h1>", unsafe_allow_html=True)
#     st.markdown("<h4 style='color: #aaa;'>Find the best assessment using AI! 🎯</h4>", unsafe_allow_html=True)

# st.markdown("---")

# # ------------------ Sidebar Info ------------------ #
# with st.sidebar:
#     st.image("https://static.streamlit.io/logos/brand-logo-secondary-colormark-darktext.png", width=200)
#     st.markdown("### 👩‍💻 Built by Priya Yadav")
#     st.markdown("AI-powered assessment search engine using LLMs and SHL data.")
#     st.markdown("#### 💬 Example Queries:")
#     st.markdown("- Python SQL coding test\n- Aptitude assessment\n- Data analyst MCQ")
#     st.markdown("🔗 [GitHub Repo](https://github.com/your-repo-url)")

# # ------------------ Query Input ------------------ #
# query_options = [
#     "Python SQL coding test",
#     "Aptitude test for freshers",
#     "Logical reasoning MCQ",
#     "Data analyst assessment",
#     "Java backend developer test"
# ]

# query = st.selectbox(
#     "🔍 Search from common queries or type your own:",
#     options=[""] + query_options,
#     index=0,
#     help="Start typing to see suggestions or select from the dropdown."
# )

# # ------------------ Main Search Button ------------------ #
# if st.button("Search"):
#     if query.strip() == "":
#         st.warning("Please enter a valid query.")
#     else:
#         with st.spinner("🤔 Thinking... Fetching the best matches for you!"):
#             try:
#                 df = query_handling_using_LLM_updated(query)

#                 if isinstance(df, pd.DataFrame) and not df.empty:
#                     if 'Score' in df.columns:
#                         df = df.drop(columns=['Score'])

#                     if "Duration" in df.columns:
#                         df = df.rename(columns={"Duration": "Duration in mins"})

#                     display_cols = ["Assessment Name", "Test Type", "Description", "Remote Testing Support", "Adaptive/IRT", "Duration in mins", "URL"]
#                     df = df[[col for col in display_cols if col in df.columns]]

#                     df['URL'] = df['URL'].apply(lambda x: f"<a href='{x}' target='_blank'>🔗 View</a>" if pd.notna(x) else "")

#                     st.success("✅ Here are your top assessment recommendations:")

#                     # Custom Table Rendering
#                     table_html = """
#                     <style>
#                         table.custom-table {
#                             width: 100%;
#                             border-collapse: separate;
#                             border-spacing: 0;
#                             font-family: 'Segoe UI', sans-serif;
#                             font-size: 15px;
#                             border-radius: 12px;
#                             overflow: hidden;
#                             box-shadow: 0 4px 12px rgba(0,0,0,0.3);
#                             margin-top: 1rem;
#                         }
#                         table.custom-table thead {
#                             background: linear-gradient(to right, #4B8BBE, #306998);
#                             color: white;
#                             font-weight: 600;
#                         }
#                         table.custom-table th, table.custom-table td {
#                             padding: 14px 18px;
#                             text-align: left;
#                             vertical-align: top;
#                         }
#                         table.custom-table tbody tr {
#                             background-color: #181c24;
#                             color: #f0f2f6;
#                             border-bottom: 1px solid #333;
#                         }
#                         table.custom-table tbody tr:nth-child(even) {
#                             background-color: #1f242e;
#                         }
#                         table.custom-table tbody tr:hover {
#                             background-color: #2a303c;
#                         }
#                         a {
#                             color: #61dafb;
#                             text-decoration: none;
#                             font-weight: 500;
#                         }
#                         a:hover {
#                             text-decoration: underline;
#                         }
#                     </style>
#                     <table class="custom-table">
#                         <thead>
#                             <tr>
#                     """
#                     for col in df.columns:
#                         table_html += f"<th>{col}</th>"
#                     table_html += "</tr></thead><tbody>"

#                     for _, row in df.iterrows():
#                         table_html += "<tr>"
#                         for cell in row:
#                             table_html += f"<td>{cell}</td>"
#                         table_html += "</tr>"

#                     table_html += "</tbody></table>"
#                     st.markdown(table_html, unsafe_allow_html=True)
#                 else:
#                     st.warning("😕 No assessments matched your query. Try rephrasing it!")

#             except Exception as e:
#                 st.error(f"🚨 Something went wrong: {e}")

# # ------------------ Recommended for You Section ------------------ #
# st.markdown("## 🧠 Recommended for You")

# recommendations = [
#     {
#         "title": "Python Aptitude Test",
#         "desc": "Covers loops, functions, and OOP basics.",
#         "url": "https://example.com/python-test"
#     },
#     {
#         "title": "SQL + Logical MCQ",
#         "desc": "Intermediate level with real-time queries.",
#         "url": "https://example.com/sql-test"
#     },
#     {
#         "title": "AI Fundamentals",
#         "desc": "Machine learning basics and conceptual MCQ.",
#         "url": "https://example.com/ai-test"
#     },
# ]

# rec_cols = st.columns(len(recommendations))
# for idx, rec in enumerate(recommendations):
#     with rec_cols[idx]:
#         st.markdown(f"### 🔸 {rec['title']}")
#         st.markdown(f"*{rec['desc']}*")
#         st.markdown(f"[👉 Try Now]({rec['url']})", unsafe_allow_html=True)


#  nice one 
# import streamlit as st
# import pandas as pd
# from query_functions import query_handling_using_LLM_updated
# from streamlit_lottie import st_lottie
# import requests

# # ------------------ Config ------------------ #
# st.set_page_config(
#     page_title="SHL Assessment Recommendation System",
#     layout="wide",
#     page_icon="🤖"
# )

# # ------------------ Lottie Loader ------------------ #
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# lottie_robot = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_tutvdkg0.json")

# # ------------------ CSS Styling ------------------ #
# st.markdown("""
# <style>
# html, body {
#     background: linear-gradient(to right, #e0f7ff, #ffffff);
#     color: #1e1e1e;
#     font-family: 'Segoe UI', sans-serif;
#     margin: 0;
# }
# body {
#     background-attachment: fixed;
# }
# .stTextInput > div > div > input,
# .stSelectbox > div > div > div {
#     background-color: #f1f9ff;
#     color: #1e1e1e;
#     border-radius: 10px;
#     border: none;
#     padding: 10px;
#     box-shadow: 0 0 10px rgba(0,0,0,0.1);
# }
# .stButton>button {
#     background: linear-gradient(135deg, #4da8ff, #5170fd);
#     color: white;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 0.5rem 1.5rem;
#     border: none;
#     transition: 0.3s ease;
# }
# .stButton>button:hover {
#     transform: scale(1.05);
#     background: linear-gradient(135deg, #5170fd, #4da8ff);
# }
# .sidebar .sidebar-content {
#     background-color: #f0f4ff;
#     padding: 2rem;
#     position: sticky;
#     top: 0;
#     height: 100vh;
#     overflow: auto;
#     color: #1e1e1e;
# }
# hr {
#     border-top: 1px solid #ccc;
#     margin-top: 2rem;
#     margin-bottom: 2rem;
# }
# .card {
#     background: #dceeff;
#     border-radius: 15px;
#     padding: 1.5rem;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#     transition: 0.3s;
#     color: #1e1e1e;
# }
# .card:hover {
#     transform: scale(1.03);
#     background: #cce6ff;
# }
# .card a {
#     color: #0a74da;
#     font-weight: 600;
#     text-decoration: none;
# }
# .card a:hover {
#     text-decoration: underline;
# }
# </style>
# """, unsafe_allow_html=True)

# # ------------------ Header ------------------ #
# col1, col2 = st.columns([1, 2])
# with col1:
#     st_lottie(lottie_robot, height=180)
# with col2:
#     st.markdown("<h1 style='color: #1e1e1e;'>🤖 SHL Assessment Recommender</h1>", unsafe_allow_html=True)
#     st.markdown("<h4 style='color: #333;'>Find the best assessment using AI! 🎯</h4>", unsafe_allow_html=True)

# st.markdown("---")

# # ------------------ Sidebar ------------------ #
# with st.sidebar:
#     st.image("https://static.streamlit.io/logos/brand-logo-secondary-colormark-darktext.png", width=200)
#     st.markdown("### 👩‍💻 Built by Priya Yadav")
#     st.markdown("#### 🔍 Try:")
#     st.markdown("- Python SQL test\n- Aptitude MCQ\n- Data science quiz")
#     st.markdown("🔗 [View GitHub](https://github.com/your-repo-url)")

# # ------------------ Search Input ------------------ #
# query_options = [
#     "Python SQL coding test",
#     "Aptitude test for freshers",
#     "Logical reasoning MCQ",
#     "Data analyst assessment",
#     "Java backend developer test"
# ]

# query = st.selectbox(
#     "🔍 Search from common queries or type your own:",
#     options=[""] + query_options,
#     index=0,
#     help="Start typing to see suggestions or select from the dropdown."
# )

# # ------------------ Search Action ------------------ #
# if st.button("Search"):
#     if query.strip() == "":
#         st.warning("Please enter a valid query.")
#     else:
#         with st.spinner("🤔 Thinking... Fetching the best matches for you!"):
#             try:
#                 df = query_handling_using_LLM_updated(query)

#                 if isinstance(df, pd.DataFrame) and not df.empty:
#                     if 'Score' in df.columns:
#                         df = df.drop(columns=['Score'])
#                     if "Duration" in df.columns:
#                         df = df.rename(columns={"Duration": "Duration in mins"})

#                     display_cols = ["Assessment Name", "Test Type", "Description", "Remote Testing Support", "Adaptive/IRT", "Duration in mins", "URL"]
#                     df = df[[col for col in display_cols if col in df.columns]]

#                     df['URL'] = df['URL'].apply(lambda x: f"<a href='{x}' target='_blank'>🔗 View</a>" if pd.notna(x) else "")

#                     st.success("✅ Here are your top assessment recommendations:")
#                     for _, row in df.iterrows():
#                         st.markdown("""
#                             <div class='card'>
#                                 <h3>🧪 {}</h3>
#                                 <p><b>Type:</b> {}</p>
#                                 <p><b>Support:</b> {} | <b>Adaptive:</b> {}</p>
#                                 <p><b>Duration:</b> {}</p>
#                                 <p>{}</p>
#                                 {}
#                             </div>
#                             <br>
#                         """.format(row['Assessment Name'], row['Test Type'], row['Remote Testing Support'], row['Adaptive/IRT'], row['Duration in mins'], row['Description'], row['URL']), unsafe_allow_html=True)
#                 else:
#                     st.warning("😕 No assessments matched your query. Try rephrasing it!")

#             except Exception as e:
#                 st.error(f"🚨 Something went wrong: {e}")

# # ------------------ Recommendation Cards ------------------ #
# st.markdown("## 🧠 Recommended for You")

# recommendations = [
#     {
#         "title": "Python Aptitude Test",
#         "desc": "Covers loops, functions, and OOP basics.",
#         "url": "https://example.com/python-test"
#     },
#     {
#         "title": "SQL + Logical MCQ",
#         "desc": "Intermediate level with real-time queries.",
#         "url": "https://example.com/sql-test"
#     },
#     {
#         "title": "AI Fundamentals",
#         "desc": "Machine learning basics and conceptual MCQ.",
#         "url": "https://example.com/ai-test"
#     },
# ]

# rec_cols = st.columns(len(recommendations))
# for idx, rec in enumerate(recommendations):
#     with rec_cols[idx]:
#         st.markdown(f"""
#         <div class='card'>
#             <h4>📘 {rec['title']}</h4>
#             <p>{rec['desc']}</p>
#             <a href='{rec['url']}' target='_blank'>👉 Try Now</a>
#         </div>
#         """, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
from query_functions import query_handling_using_LLM_updated

# ------------------ Config ------------------ #
st.set_page_config(
    page_title="SHL Assessment Recommendation System",
    layout="wide",
    page_icon="🤖"
)

# ------------------ CSS Styling ------------------ #
st.markdown("""
<style>
html, body {
    background: linear-gradient(to right, #e0f7ff, #ffffff);
    color: #1e1e1e;
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
}
body {
    background-attachment: fixed;
}
.stTextInput > div > div > input {
    background-color: #f1f9ff;
    color: #1e1e1e;
    border-radius: 10px;
    border: none;
    padding: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    width: 100%;
}
.stButton>button {
    background: linear-gradient(135deg, #4da8ff, #5170fd);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5rem 1.5rem;
    border: none;
    transition: 0.3s ease;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #5170fd, #4da8ff);
}
.sidebar .sidebar-content {
    background-color: #f0f4ff;
    padding: 2rem;
    position: sticky;
    top: 0;
    height: 100vh;
    overflow: auto;
    color: #1e1e1e;
}
hr {
    border-top: 1px solid #ccc;
    margin-top: 2rem;
    margin-bottom: 2rem;
}
.github-button {
    display: inline-block;
    margin-top: 10px;
    background-color: #24292e;
    color: white !important;
    padding: 8px 14px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.github-button:hover {
    background-color: #57606a;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Header ------------------ #
st.image("https://img.icons8.com/external-flat-icons-inmotus-design/100/external-Software-Engineer-it-services-flat-icons-inmotus-design.png", width=120)
st.markdown("<h1 style='color: #1e1e1e;'>🤖 SHL Assessment Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #333;'>Find the best assessment using AI! 🎯</h4>", unsafe_allow_html=True)

st.markdown("---")

# ------------------ Sidebar ------------------ #
with st.sidebar:
    st.markdown("### 👩‍💻 Built by Priya Yadav")
    st.markdown("#### 🔍 Try:")
    st.markdown("- Python SQL test\n- Aptitude MCQ\n- Data science quiz")
    st.markdown("🔗 [View GitHub](https://github.com/2priyayadav/Project_Intern/tree/main)")
    st.markdown("""
        <a class='github-button' href='https://github.com/2priyayadav/Project_Intern/tree/main' target='_blank'>⭐ Star on GitHub</a>
    """, unsafe_allow_html=True)

# ------------------ Search Input ------------------ #
query_options = [
    "Python SQL coding test",
    "Aptitude test for freshers",
    "Logical reasoning MCQ",
    "Data analyst assessment",
    "Java backend developer test"
]

selected_query = st.selectbox(
    "📌 Choose from common queries:",
    options=["" ] + query_options,
    index=0,
    help="Select a popular search or use your own below."
)

manual_query = st.text_input("🔍 Or type your own query:", value="")
query = manual_query if manual_query.strip() else selected_query

# ------------------ Search Action ------------------ #
if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("🤔 Thinking... Fetching the best matches for you!"):
            try:
                df = query_handling_using_LLM_updated(query)

                if isinstance(df, pd.DataFrame) and not df.empty:
                    if 'Score' in df.columns:
                        df = df.drop(columns=['Score'])
                    if "Duration" in df.columns:
                        df = df.rename(columns={"Duration": "Duration in mins"})

                    display_cols = ["Assessment Name", "Test Type", "Description", "Remote Testing Support", "Adaptive/IRT", "Duration in mins", "URL"]
                    df = df[[col for col in display_cols if col in df.columns]]

                    df['URL'] = df['URL'].apply(lambda x: f"🔗 [View]({x})" if pd.notna(x) else "")

                    st.success("✅ Here are your top assessment recommendations:")
                    st.dataframe(df, use_container_width=True)

                else:
                    st.warning("😕 No assessments matched your query. Try rephrasing it!")

            except Exception as e:
                st.error(f"🚨 Something went wrong: {e}")

# ------------------ Recommendation Cards ------------------ #
st.markdown("## 🧠 Recommended for You")

recommendations = [
    {
        "title": "Python Aptitude Test",
        "desc": "Covers loops, functions, and OOP basics."
    },
    {
        "title": "SQL + Logical MCQ",
        "desc": "Intermediate level with real-time queries."
    },
    {
        "title": "AI Fundamentals",
        "desc": "Machine learning basics and conceptual MCQ."
    },
]

rec_cols = st.columns(len(recommendations))
for idx, rec in enumerate(recommendations):
    with rec_cols[idx]:
        with open("samples/sample_assessment.pdf", "rb") as f:
            sample = f.read()
        st.markdown(f"""
        <div style='background: #dceeff; border-radius: 15px; padding: 1.5rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); transition: 0.3s; color: #1e1e1e;'>
            <h4>📘 {rec['title']}</h4>
            <p>{rec['desc']}</p>
        """, unsafe_allow_html=True)
        st.download_button("📥 Download Sample", sample, file_name="sample_assessment.pdf")
        st.markdown("</div>", unsafe_allow_html=True)

