import streamlit as st

# Initialize session state for page navigation if not already set
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_new_member():
    st.session_state.page = "new_member_details"

def go_to_home():
    st.session_state.page = "home"

def register_btn():
    st.success("Registration Successful!")
    st.session_state.page = "home"

def update_btn():
    st.session_state.page = "update"

def update_details_btn():
    st.session_state.page = 'home'
    st.success("Details updated successfully!")

def act_deact_mem():
    st.session_state.page = "activate_deactivate_mem"

def act_deact_btn():
    st.session_state.page = 'home'
    st.success("Details updated successfully!")

def show_page(page):
    if page == "home":
        st.write("# Managing Memberships or Subscriptions")
        st.button("Register New Member", on_click=go_to_new_member)
        st.button("Update Details", on_click=update_btn)
        st.button("Manage Membership", on_click=act_deact_mem)

    elif page == "new_member_details":
        st.title("New Member Registration")
        st.write("Please provide details for the new member.")
        name = st.text_input("Enter your full name")
        col1, col2 = st.columns(2)
        with col1:
            number = st.text_input("Enter mobile no.")
        with col2:
            email = st.text_input("Enter your email")
        membership_type = st.selectbox("Membership Type",["Monthly", "Quarterly", "Yearly"],index=0)
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("Start Date")
        with col2:
            end_date = st.date_input("End Date")
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Submit",on_click=register_btn)

    elif page == "update":
        st.title("Update your details")
        col1, col2 = st.columns(2)
        with col1:
            number = st.text_input("Enter mobile no.")
        with col2:
            email = st.text_input("Enter your email")
        membership_type = st.selectbox("Membership Type",["Monthly", "Quarterly", "Yearly"],index=0)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Update", on_click=update_details_btn)

    elif page == "activate_deactivate_mem":
        st.title("Activate/Deactivate Membership")
        act_deact = st.selectbox("Activate/Deactivate", ["Activate", "Deactivate"], index=0)
        col1, col2 = st.columns(2)
        with col1:
            st.button("Home", on_click=go_to_home)
        with col2:
            st.button("Update", on_click=act_deact_btn)

show_page(st.session_state.page)
