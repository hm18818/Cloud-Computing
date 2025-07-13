import streamlit as st
from typing import Tuple
import pandas as pd
import datetime

# Expanded keyword-category-email-URL mapping based on full document
CATEGORY_KEYWORDS = {
    "Railway Concession Pass": {
        "keywords": ["railway pass", "railway concession"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Head Signature on Application Form": {
        "keywords": ["gate form", "cat form", "application signature"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Email Group ID Issue": {
        "keywords": ["email group id", "not receiving emails"],
        "email": "helpdesk@kiit.ac.in",
        "url": None
    },
    "Library Access": {
        "keywords": ["library access", "library book", "library fine"],
        "email": "beda_sahoo@kiit.ac.in",
        "url": None
    },
    "Fee & SAP Issues": {
        "keywords": ["fee discrepancy", "sap update", "payment issue"],
        "email": "manoj.meher@kiit.ac.in",
        "url": None
    },
    "Student Activity Centre": {
        "keywords": ["student club", "extracurricular activity"],
        "email": "studentssupport@kiit.ac.in",
        "url": "https://ksac.kiit.ac.in/"
    },
    "Grievance Helpdesk": {
        "keywords": ["grievance", "student complaint"],
        "email": "grievance.psp@kiit.ac.in",
        "url": "https://kiit.ac.in/grievance/"
    },
    "Guest House Booking": {
        "keywords": ["guest house", "stay request"],
        "email": "kiitguesthouse@kiit.ac.in",
        "url": None
    },
    "Anti Ragging Committee": {
        "keywords": ["ragging", "anti ragging", "bullying"],
        "email": None,
        "url": "https://kiit.ac.in/antiragging/"
    },
    "Internal Complaint Committee": {
        "keywords": ["sexual harassment", "internal complaint"],
        "email": None,
        "url": "https://kiit.ac.in/internal-complaint-committee/"
    },
    "Cyber Helpdesk": {
        "keywords": ["cyber crime", "online fraud"],
        "email": "cyber.helpline@kiit.ac.in",
        "url": None
    },
    "SAP Helpdesk": {
        "keywords": ["sap help", "student portal issue"],
        "email": "helpdesksap.eam@kiit.ac.in",
        "url": None
    },
    "Counselling Services": {
        "keywords": ["counselling", "mental support", "stress", "anxiety"],
        "email": "student.counselling@kiit.ac.in",
        "url": "https://kiit.ac.in/student-counselling/"
    },
    "Career & Placement Support": {
        "keywords": ["career support", "job placement", "internship"],
        "email": "placement@kiit.ac.in",
        "url": None
    },
    "Sports & Fitness": {
        "keywords": ["sports", "fitness", "yoga"],
        "email": "rashmi.pradhan@kiit.ac.in",
        "url": "https://kiit.ac.in/campuslife/sports/"
    },
    "Mentorship": {
        "keywords": ["tutor mentor", "know your mentor"],
        "email": None,
        "url": "https://kiit.ac.in/sap/know-your-mentor/"
    },
    "Other": {
        "keywords": [],
        "email": "deanoffice@kiit.ac.in",
        "url": None
    }
}

history = []

def classify_query(query: str) -> Tuple[str, str, str, str]:
    query_lower = query.lower()
    matched_keyword = ""
    for category, data in CATEGORY_KEYWORDS.items():
        for keyword in data["keywords"]:
            if keyword in query_lower:
                matched_keyword = keyword
                return category, data.get("email", "Not listed"), data.get("url"), matched_keyword
    return "Other", CATEGORY_KEYWORDS["Other"]["email"], CATEGORY_KEYWORDS["Other"]["url"], ""

def generate_email_to_student(query: str, category: str, email: str) -> str:
    email_body = f"""
Dear Student,

Thank you for reaching out with your concern:

> {query.strip()}

After reviewing your query, it is recommended that you contact the respective department at: {email}

Feel free to let me know if you need any further help.

Regards,
Mentor
"""
    return email_body

def main():
    st.set_page_config(page_title="KIIT Query Router", layout="centered")
    st.title("📩 KIIT Mentee Query Email Routing Tool")
    st.write("Classify a mentee's query and get department email, link, and a ready-to-send response.")

    with st.expander("🗂 Upload CSV of Queries"):
        csv_file = st.file_uploader("Upload a CSV file with a 'Query' column", type="csv")
        if csv_file:
            df = pd.read_csv(csv_file)
            if "Query" in df.columns:
                results = []
                for query in df["Query"]:
                    category, email, url, keyword = classify_query(query)
                    results.append({
                        "Query": query,
                        "Category": category,
                        "Email": email,
                        "Matched Keyword": keyword,
                        "URL": url
                    })
                result_df = pd.DataFrame(results)
                st.dataframe(result_df)
                st.download_button("Download Classified CSV", result_df.to_csv(index=False), "classified_queries.csv")
            else:
                st.error("CSV must contain a column titled 'Query'.")

    st.subheader("🔍 Classify Individual Query")
    query = st.text_area("Enter the query from student:", height=150)

    if st.button("Classify and Suggest"):
        if query.strip():
            category, email, url, keyword = classify_query(query)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append({"Timestamp": timestamp, "Query": query, "Category": category, "Email": email, "Keyword": keyword})
            st.success(f"📌 Category: {category}")
            if keyword:
                st.caption(f"🔍 Matched on: '{keyword}'")
            if email:
                st.info(f"📧 Email ID: `{email}`")
            if url:
                st.markdown(f"🔗 [Useful Link]({url})" if url.startswith("http") else f"📞 Contact Info: {url}")

            st.subheader("📩 Ready-to-Copy Reply Email")
            st.text_area("Email Draft:", generate_email_to_student(query, category, email), height=200)
        else:
            st.warning("Please enter a valid query.")

    with st.expander("📜 Session History"):
        if history:
            hist_df = pd.DataFrame(history)
            st.dataframe(hist_df)
            st.download_button("Download History", hist_df.to_csv(index=False), "query_history.csv")
        else:
            st.info("No queries classified yet.")

if __name__ == "__main__":
    main()
