import streamlit as st
from typing import Tuple

# Define keyword-category-email-URL mapping (updated with detailed PoC list)
CATEGORY_KEYWORDS = {
    "Bonafide Certificate": {
        "keywords": ["bonafide", "education loan", "course continuing", "passport", "higher studies"],
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
    "Rank Certificate/No Backlog": {
        "keywords": ["rank certificate", "no backlog"],
        "email": "compliance.cse@kiit.ac.in",
        "url": None
    },
    "Registration Card": {
        "keywords": ["registration card"],
        "email": None,
        "url": "Tel: 8144967820 (Mrs. Tunalata Nayak)"
    },
    "Marks Discrepancy (2022-2023, MTech, PhD)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2022", "btech 2023", "mtech", "phd", "backlog"],
        "email": "acoe.cese@kiit.ac.in",
        "url": None
    },
    "Marks Discrepancy (2024-2025)": {
        "keywords": ["marks", "grade", "answer sheet", "btech 2024", "btech 2025"],
        "email": "acoe.csit@kiit.ac.in",
        "url": None
    },
    "Admission Issues": {
        "keywords": ["name correction", "dob", "address change", "scholarship issue"],
        "email": "swapna.mohanty@kiit.ac.in",
        "url": None
    },
    "Extension for Fee Payment": {
        "keywords": ["extension", "academic fee", "hostel fee"],
        "email": "director.admission@kiit.ac.in",
        "url": None
    },
    "Loan Demand Letter": {
        "keywords": ["demand letter"],
        "email": "admission@kiit.ac.in",
        "url": None
    },
    "Laptop Issues": {
        "keywords": ["laptop", "delivery", "technical fault"],
        "email": "laptop.service@kiit.ac.in",
        "url": None
    },
    "Email Group ID": {
        "keywords": ["email group"],
        "email": "helpdesk@kiit.ac.in",
        "url": None
    },
    "Library Access": {
        "keywords": ["library", "book", "access", "fine"],
        "email": "beda_sahoo@kiit.ac.in",
        "url": None
    },
    "Fee Discrepancy": {
        "keywords": ["fee", "sap update"],
        "email": "manoj.meher@kiit.ac.in",
        "url": None
    },
    "Hostel Matters": {
        "keywords": ["hostel", "room", "accommodation"],
        "email": "hostel@kiit.ac.in",
        "url": "https://kiit.ac.in/code-of-conduct-of-boarders/"
    },
    "Training & Placement": {
        "keywords": ["placement", "internship", "training"],
        "email": "tnp.scs@kiit.ac.in",
        "url": None
    },
    "Sports Access": {
        "keywords": ["sports", "recreational", "fitness"],
        "email": "sports.kiit@gmail.com",
        "url": "https://kiit.ac.in/campuslife/sports/"
    },
    "Student Activities": {
        "keywords": ["activity", "club", "ksac"],
        "email": "shyam.behura@kids.ac.in",
        "url": "https://ksac.kiit.ac.in/"
    },
    "Grade Sheet Download": {
        "keywords": ["grade sheet", "download"],
        "email": "slcm.kiit@kiit.ac.in",
        "url": None
    },
    "Guest House Booking": {
        "keywords": ["guest house"],
        "email": "kiitguesthouse@kiit.ac.in",
        "url": None
    },
    "Mentorship": {
        "keywords": ["mentor", "tutor mentor"],
        "email": None,
        "url": "https://kiit.ac.in/sap/know-your-mentor/"
    },
    "Counselling": {
        "keywords": ["counselling", "mental health"],
        "email": "student.counselling@kiit.ac.in",
        "url": "https://kiit.ac.in/student-counselling/"
    },
    "Online Counselling Support": {
        "keywords": ["online counselling", "kiit care"],
        "email": None,
        "url": "https://kiitportal.kiituniversity.net/irj/portal/"
    },
    "Cyber Helpdesk": {
        "keywords": ["cyber", "online fraud"],
        "email": "cyber.helpline@kiit.ac.in",
        "url": None
    },
    "SAP Help": {
        "keywords": ["sap", "student portal"],
        "email": "helpdesksap.eam@kiit.ac.in",
        "url": None
    },
    "Career Support": {
        "keywords": ["career counselling", "placement support"],
        "email": "placement@kiit.ac.in",
        "url": None
    },
    "Grievance": {
        "keywords": ["grievance", "complaint"],
        "email": "grievance.psp@kiit.ac.in",
        "url": "https://kiit.ac.in/grievance/"
    },
    "Internal Complaint": {
        "keywords": ["sexual harassment", "icc", "internal complaint"],
        "email": None,
        "url": "https://kiit.ac.in/internal-complaint-committee/"
    },
    "Anti Ragging": {
        "keywords": ["ragging", "anti ragging"],
        "email": None,
        "url": "https://kiit.ac.in/antiragging/"
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
                return category, data.get("email", "Not listed"), data.get("url")
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
            if email:
                st.info(f"**Recommended Email ID:** `{email}`")
            if url:
                st.markdown(f"**Useful Link or Info:** [Click here]({url})" if url.startswith("http") else f"**Contact Info:** {url}")
        else:
            st.warning("Please enter a query to classify.")

if __name__ == "__main__":
    main()
