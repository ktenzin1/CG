import streamlit as st

st.set_page_config(
    page_title="Caring Gem Employment Agency",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Caring Gem Employment Agency")

st.write(
    """
Helping employers find trusted employees and helping employees
find meaningful employment.
"""
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Services",
        "Families",
        "Caregivers",
        "Contact"
    ]
)

if page == "Home":

    st.header("Welcome")

    st.write("""
We connect employers with experienced:

- Nannies
- Housekeepers
- Elderly Caregivers
- Warehouse Associates
- Office Assistants
- Restaurant Staff
- And more!
Have a role to fill that isn't listed? Contact us today and we will help you find the right employee for your needs.
""")

    st.success("Looking for help? Contact us today!")

elif page == "Services":

    st.header("Our Services")

    st.subheader("For Families")

    st.write("""
- Full-Time Nannies
- Part-Time Nannies
- Live-In or Live-Out Caregivers
- Housekeepers
- Elder Care
""")
    
    st.subheader("For Employers")

    st.write("""
We help employers find trusted employees for your businesses.
- Warehouse Associates
- Office Assistants
- Restaurant Staff
- And more!
Have a role to fill that isn't listed? Contact us today and we will help you find the right employee for your needs.
""")

    st.subheader("For Caregivers")

    st.write("""
We help qualified caregivers find employment with families.
""")
    
    
elif page == "Families":

    st.header("Request a Caregiver")

    name = st.text_input("Your Name")

    phone = st.text_input("Phone")

    email = st.text_input("Email")

    service = st.selectbox(
        "Service Needed",
        [
            "Nanny",
            "Housekeeper",
            "Elder Care"
        ]
    )

    details = st.text_area("Tell us what you need")

    if st.button("Submit Request"):
        st.success("Thank you! We will contact you soon.")

elif page == "Other Employers":

    st.header("Request an Employee")

    name = st.text_input("Your Name")

    phone = st.text_input("Phone")

    email = st.text_input("Email")

    position = st.selectbox(
        "Position Needed",
        [
            "Warehouse Associate",
            "Office Assistant",
            "Restaurant Staff"
        ]
    )

    details = st.text_area("Tell us what you need")

    if st.button("Submit Request"):
        st.success("Thank you! We will contact you soon.")

elif page == "Looking for Work - Apply Now":

    st.header("Apply for Employment")

    name = st.text_input("Full Name")

    phone = st.text_input("Phone Number")

    experience = st.text_area("Experience")

    if st.button("Submit Application"):
        st.success("Application received!")

elif page == "Contact":

    st.header("Contact Us")

    st.write("📞 Phone: (555) 555-5555")

    st.write("📧 Email: info@example.com")

    st.write("Business Hours")

    st.write("""
Monday-Friday

9:00 AM - 6:00 PM
""")