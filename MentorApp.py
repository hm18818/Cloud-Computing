import streamlit as st
from typing import Tuple

# Define keyword-category-email-URL mapping
CATEGORY_KEYWORDS = {
    "Bonafide Certificate": {
        "keywords": ["bonafide", "education loan", "scholarship", "passport", "higher studies"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Grade/Provisional Certificates": {
        "keywords": ["grade report", "provisional degree", "degree certificate", "conduct certificate", "college leaving"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Elective Queries": {
        "keywords": ["elective", "open elective", "department elective"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Marks Discrepancy (2022-2023, MTech, PhD)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2022", "btech 2023", "mtech", "phd"],
        "email": "acoe.cese@kiit.ac.in",
        "url": None
    },
    "Marks Discrepancy (2024-2025)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2024", "btech 2025"],
        "email": "acoe.csit@kiit.ac.in",
        "url": None
    },
    "Fee/Payment Issues": {
        "keywords": ["fee", "payment", "refund", "receipt", "sap update"],
        "email": "manoj.meher@kiit.ac.in",
        "url": None
    },
    "Admission Related": {
        "keywords": ["name correction", "dob", "address change", "scholarship issue", "demand letter"],
        "email": "admission@kiit.ac.in",
        "url": None
    },
    "Hostel": {
        "keywords": ["hostel", "room", "warden", "accommodation"],
        "email": "hostel@kiit.ac.in",
        "url": "https://kiit.ac.in/code-of-conduct-of-boarders/"
    },
    "Laptop/Technical Faults": {
        "keywords": ["laptop", "delivery", "technical fault"],
        "email": "laptop.service@kiit.ac.in",
        "url": None
    },
    "IT Support/Portal": {
        "keywords": ["email id", "portal", "login", "technical", "password"],
        "email": "helpdesk@kiit.ac.in",
        "url": None
    },
    "Library": {
        "keywords": ["library", "book", "access", "fine"],
        "email": "beda_sahoo@kiit.ac.in",
        "url": None
    },
    "Placement/Internship": {
        "keywords": ["placement", "internship", "training", "noc"],
        "email": "tnp.scs@kiit.ac.in",
        "url": None
    },
    "Sports/Yoga": {
        "keywords": ["sports", "recreational", "yoga", "fitness"],
        "email": "rashmi.pradhan@kiit.ac.in",
        "url": "https://kiit.ac.in/campuslife/sports/"
    },
    "Student Activity/Clubs": {
        "keywords": ["student club", "activity", "ksac"],
        "email": "studentssupport@kiit.ac.in",
        "url": "https://ksac.kiit.ac.in/"
    },
    "Guest House": {
        "keywords": ["guest house booking"],
        "email": "kiitguesthouse@kiit.ac.in",
        "url": None
    },
    "Counselling/Mental Health": {
        "keywords": ["counselling", "mental health", "stress"],
        "email": "student.counselling@kiit.ac.in",
        "url": "https://kiit.ac.in/student-counselling/"
    },
    "Grievance": {
        "keywords": ["grievance", "complaint"],
        "email": "grievance.psp@kiit.ac.in",
        "url": "https://kiit.ac.in/grievance/"
    },
    "Cyber Security": {
        "keywords": ["cyber", "online fraud", "cybersecurity"],
        "email": "cyber.helpline@kiit.ac.in",
        "url": None
    },
    "SAP Portal Help": {
        "keywords": ["sap", "student profile", "academic portal"],
        "email": "helpdesksap.eam@kiit.ac.in",
        "url": None
    },
    "Other": {
        "keywords": [],
        "email": "deanoffice@kiit.ac.in",
        "url": None
    }
}

def classify_query(query: str) -> Tuple[str, str, str]:
    query_lower = query.lower()
    for category, data in CATEGORY_KEYWORDS.items():
        for keyword in data["keywords"]:
            if keyword in query_lower:
                return category, data["email"], data["url"]
    return "Other", CATEGORY_KEYWORDS["Other"]["email"], CATEGORY_KEYWORDS["Other"]["url"]

def main():
    st.set_page_config(page_title="Mentee Query Router", layout="centered")
    st.title("\U0001F4E9 KIIT Mentee Query Email Routing Tool")
    st.write("Classify a mentee's query and get the right email contact and resource link.")

    query = st.text_area("Enter Mentee's Query or Complaint", height=150)

    if st.button("Classify and Suggest Contact"):
        if query.strip():
            category, email, url = classify_query(query)
            st.success(f"**Category Identified:** {category}")
            st.info(f"**Recommended Email ID:** `{email}`")
            if url:
                st.markdown(f"**Useful Link:** [Click here]({url})")
        else:
            st.warning("Please enter a query to classify.")

if __name__ == "__main__":
    main()
