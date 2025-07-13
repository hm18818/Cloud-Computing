import streamlit as st
from typing import Tuple

# Define keyword-category-email mapping
CATEGORY_KEYWORDS = {
    "Bonafide Certificate": {
        "keywords": ["bonafide", "education loan", "scholarship", "passport", "higher studies"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "Grade/Provisional Certificates": {
        "keywords": ["grade report", "provisional degree", "degree certificate", "conduct certificate", "college leaving"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "Elective Queries": {
        "keywords": ["elective", "open elective", "department elective"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "Marks Discrepancy (2022-2023, MTech, PhD)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2022", "btech 2023", "mtech", "phd"],
        "email": "acoe.cese@kiit.ac.in"
    },
    "Marks Discrepancy (2024-2025)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2024", "btech 2025"],
        "email": "acoe.csit@kiit.ac.in"
    },
    "Fee/Payment Issues": {
        "keywords": ["fee", "payment", "refund", "receipt", "sap update"],
        "email": "manoj.meher@kiit.ac.in"
    },
    "Admission Related": {
        "keywords": ["name correction", "dob", "address change", "scholarship issue", "demand letter"],
        "email": "admission@kiit.ac.in"
    },
    "Hostel": {
        "keywords": ["hostel", "room", "warden", "accommodation"],
        "email": "hostel@kiit.ac.in"
    },
    "Laptop/Technical Faults": {
        "keywords": ["laptop", "delivery", "technical fault"],
        "email": "laptop.service@kiit.ac.in"
    },
    "IT Support/Portal": {
        "keywords": ["email id", "portal", "login", "technical", "password"],
        "email": "helpdesk@kiit.ac.in"
    },
    "Library": {
        "keywords": ["library", "book", "access", "fine"],
        "email": "beda_sahoo@kiit.ac.in"
    },
    "Placement/Internship": {
        "keywords": ["placement", "internship", "training", "noc"],
        "email": "tnp.scs@kiit.ac.in"
    },
    "Sports/Yoga": {
        "keywords": ["sports", "recreational", "yoga", "fitness"],
        "email": "rashmi.pradhan@kiit.ac.in"
    },
    "Student Activity/Clubs": {
        "keywords": ["student club", "activity", "ksac"],
        "email": "studentssupport@kiit.ac.in"
    },
    "Guest House": {
        "keywords": ["guest house booking"],
        "email": "kiitguesthouse@kiit.ac.in"
    },
    "Counselling/Mental Health": {
        "keywords": ["counselling", "mental health", "stress"],
        "email": "student.counselling@kiit.ac.in"
    },
    "Grievance": {
        "keywords": ["grievance", "complaint"],
        "email": "grievance.psp@kiit.ac.in"
    },
    "Cyber Security": {
        "keywords": ["cyber", "online fraud", "cybersecurity"],
        "email": "cyber.helpline@kiit.ac.in"
    },
    "SAP Portal Help": {
        "keywords": ["sap", "student profile", "academic portal"],
        "email": "helpdesksap.eam@kiit.ac.in"
    },
    "Other": {
        "keywords": [],
        "email": "deanoffice@kiit.ac.in"
    }
}

# Classifier function
def classify_query(query: str) -> Tuple[str, str]:
    query_lower = query.lower()
    for category, data in CATEGORY_KEYWORDS.items():
        for keyword in data["keywords"]:
            if keyword in query_lower:
                return category, data["email"]
    return "Other", CATEGORY_KEYWORDS["Other"]["email"]

# Streamlit UI
def main():
    st.set_page_config(page_title="Mentee Query Router", layout="centered")
    st.title("📧 KIIT Mentee Query Email Routing Tool")
    st.markdown("Use this tool to forward mentee complaints or queries to the appropriate department.")

    st.subheader("✍️ Enter Query or Complaint:")
    query = st.text_area("Describe the issue here:", height=150, placeholder="E.g., I need a bonafide certificate for passport application.")

    if st.button("🔍 Classify & Suggest Email"):
        if query.strip():
            category, email = classify_query(query)
            st.success(f"**Category Identified:** {category}")
            st.info(f"**Recommended Email ID:** `{email}`")
        else:
            st.warning("Please enter a query to classify.")

if __name__ == "__main__":
    main()
