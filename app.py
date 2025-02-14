import os
import re
from datetime import datetime

def validate_user_inputs(data):
    name = data.get("name", "").strip()
    mobile = data.get("mobile", "").strip()
    email = data.get("email", "").strip()
    membership_type = data.get("mem_type", "").strip()
    start_date = data.get("start_date", "")
    end_date = data.get("end_date", "")

    if not name:
        return "Name is required."
    
    if not re.match(r"^\d{10}$", mobile):
        return "Mobile number must be exactly 10 digits and contain only numbers."

    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return "Invalid email format."

    if membership_type not in ["Monthly", "Quarterly", "Yearly"]:
        return "Invalid membership type selected."

    if not start_date or not end_date:
        return "Start date and end date are required."

    return True  # Validation successful

if __name__ == '__main__':
    os.system("streamlit run member_management.py")
