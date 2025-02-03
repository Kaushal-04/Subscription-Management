import streamlit as st
from database import add_member, update_member, fetch_member_by_id

# Initialize session state for page navigation if not already set
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_new_member():
    st.session_state.page = "new_member_details"

def go_to_update():
    st.session_state.page = "update"

def go_to_home():
    st.session_state.page = "home"

def go_to_manage_membership():
    st.session_state.page = "activate_deactivate_mem"

def register_btn(name, number, email, membership_type, start_date, end_date):
    if name and number and email and membership_type and start_date and end_date:
        mem_info = {
            "name": name,
            "mobile": number,
            "email": email,
            "mem_type": membership_type,
            "start_date": start_date,
            "end_date": end_date
        }
        add_member(mem_info)
        st.success("Registration Successful!")
        st.session_state.page = "home"
    else:
        st.error("All fields are required!")

def update_details_btn(id, number, email, membership_type):
    if id and number and email and membership_type:
        update_info = {
            "id": id,
            "mobile": number,
            "email": email,
            "mem_type": membership_type
        }
        update_member(update_info)
        st.success("Details updated successfully!")
        st.session_state.page = "home"
    else:
        st.error("All fields are required!")

def act_deact_btn():
    st.success("Membership status updated successfully!")
    st.session_state.page = 'home'

def show_page(page):
    if page == "home":
        st.write("# Managing Memberships or Subscriptions")
        st.button("Register New Member", on_click=go_to_new_member)
        st.button("Update Details", on_click=go_to_update)
        st.button("Manage Membership", on_click=go_to_manage_membership)

    elif page == "new_member_details":
        st.title("New Member Registration")
        name = st.text_input("Enter your full name")
        col1, col2 = st.columns(2)
        with col1:
            number = st.text_input("Enter mobile no.")
        with col2:
            email = st.text_input("Enter your email")
        membership_type = st.selectbox("Membership Type", ["Monthly", "Quarterly", "Yearly"], index=0)
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date")
        with col2:
            end_date = st.date_input("End Date")
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Submit", on_click=register_btn, args=(name, number, email, membership_type, start_date, end_date))

    elif page == "update":
        st.title("Update your details")
        id = st.text_input("Enter Member ID")
        col1, col2 = st.columns(2)
        with col1:
            number = st.text_input("Enter mobile no.")
        with col2:
            email = st.text_input("Enter your email")
        membership_type = st.selectbox("Membership Type", ["Monthly", "Quarterly", "Yearly"], index=0)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Update", on_click=update_details_btn, args=(id, number, email, membership_type))

    elif page == "activate_deactivate_mem":
        st.title("Activate/Deactivate Membership")
        act_deact = st.selectbox("Activate/Deactivate", ["Activate", "Deactivate"], index=0)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Update", on_click=act_deact_btn)

show_page(st.session_state.page)
