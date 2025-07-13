import streamlit as st
from typing import Tuple
import pandas as pd
import datetime
import openai
import os

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
    match_scores = {}
    keyword_map = {}

    for category, data in CATEGORY_KEYWORDS.items():
        match_count = 0
        for keyword in data["keywords"]:
            if keyword in query_lower:
                match_count += 1
                keyword_map[category] = keyword_map.get(category, []) + [keyword]
        if match_count > 0:
            match_scores[category] = match_count

    if match_scores:
        best_category = max(match_scores, key=match_scores.get)
        email = CATEGORY_KEYWORDS[best_category].get("email", "Not listed")
        url = CATEGORY_KEYWORDS[best_category].get("url")
        matched_keywords = ", ".join(keyword_map[best_category])

        st.subheader("🔎 Matching Categories")
        for cat, count in sorted(match_scores.items(), key=lambda x: -x[1]):
            words = ", ".join(keyword_map[cat])
            st.markdown(f"**{cat}** — {count} match(es) → _{words}_")

        return best_category, email, url, matched_keywords

    # Semantic fallback using OpenAI
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    categories = list(CATEGORY_KEYWORDS.keys())
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that classifies student queries based on department."},
                {"role": "user", "content": f"Given the following categories: {categories}.\nClassify this query: {query}"}
            ],
            temperature=0.2,
        )
        best_category = response["choices"][0]["message"]["content"].strip()
        if best_category not in CATEGORY_KEYWORDS:
            best_category = "Other"
    except Exception as e:
        st.warning("Semantic fallback failed. Using default.")
        best_category = "Other"

    email = CATEGORY_KEYWORDS[best_category].get("email", "Not listed")
    url = CATEGORY_KEYWORDS[best_category].get("url")
    return best_category, email, url, "semantic"
