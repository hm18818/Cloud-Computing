import streamlit as st
from typing import Tuple

CATEGORY_KEYWORDS = {
    "bonafide_certificate": {
        "keywords": ["bonafide", "education loan", "scholarship", "passport", "higher studies"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "grade_report_certificate": {
        "keywords": ["grade report", "provisional degree", "degree certificate", "conduct certificate", "college leaving"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "elective_queries": {
        "keywords": ["elective", "open elective", "department elective"],
        "email": "compliance.cse@kiit.ac.in"
    },
    "marks_discrepancy_2022_2023": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2022", "btech 2023", "mtech", "phd"],
        "email": "acoe.cese@kiit.ac.in"
    },
    "marks_discrepancy_2024_2025": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2024", "btech 2025"],
        "email": "acoe.csit@kiit.ac.in"
    },
    "fee_issue": {
        "keywords": ["fee", "payment", "refund", "receipt", "sap update"],
        "email": "manoj.meher@kiit.ac.in"
    },
    "admission_issues": {
        "keywords": ["name correction", "dob", "address change", "scholarship issue", "demand letter"],
        "email": "admission@kiit.ac.in"
    },
    "hostel": {
        "keywords": ["hostel", "room", "warden", "accommodation"],
        "email": "hostel@kiit.ac.in"
    },
    "laptop": {
        "keywords": ["laptop", "delivery", "technical fault"],
        "email": "laptop.service@kiit.ac.in"
    },
    "it_support": {
        "keywords": ["email id", "portal", "login", "technical", "password"],
        "email": "helpdesk@kiit.ac.in"
    },
    "library": {
        "keywords": ["library", "book", "access", "fine"],
        "email": "beda_sahoo@kiit.ac.in"
    },
    "tnp": {
        "keywords": ["placement", "internship", "training", "noc"],
        "email": "tnp.scs@kiit.ac.in"
    },
    "sports": {
        "keywords": ["sports", "recreational", "yoga", "fitness"],
        "email": "rashmi.pradhan@kiit.ac.in"
    },
    "student_activity": {
        "keywords": ["student club", "activity", "ksac"],
        "email": "studentssupport@kiit.ac.in"
    },
    "guest_house": {
        "keywords": ["guest house booking"],
        "email": "kiitguesthouse@kiit.ac.in"
    },
    "counselling": {
        "keywords": ["counselling", "mental health", "stress"],
        "email": "student.counselling@kiit.ac.in"
    },
    "grievance": {
        "keywords": ["grievance", "complaint"],
        "email": "grievance.psp@kiit.ac.in"
    },
    "cyber": {
        "keywords": ["cyber", "online fraud", "cybersecurity"],
        "email": "cyber.helpline@kiit.ac.in"
    },
    "sap": {
        "keywords": ["sap", "student profile", "academic portal"],
        "email": "helpdesksap.eam@kiit.ac.in"
    },
    "default": {
        "keywords": [],
        "email": "deanoffice@kiit.ac.in"
    }
}

def classify_query(query: str) -> Tuple[str, str]:
    query_lower = query.lower()
    for category, details in CATEGORY_KEYWORDS.items():
        for keyword in details["keywords"]:
            if keyword in query_lower:
                return category.replace("_", " ").capitalize(), details["email"]
    return "Unknown", CATEGORY_KEYWORDS["default"]["email"]

def main():
    st.set_page_config(page_title="Mentee Query Router", layout="centered")
    st.title("💬 KIIT Mentee Query Email Routing Tool")
    st.write("Enter a student\'s complaint or query to get the appropriate department email ID.")

