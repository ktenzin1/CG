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
        "Other Employers",
        "Looking for Work - Apply Now",
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

    st.write("""
We connect families with trusted nannies, housekeepers, and caregivers.

Click below to submit your request.
""")

    st.markdown("""
### 👉 Apply Here
https://forms.gle/X36yA25gmfpdRhR5A
""")

elif page == "Other Employers":

    st.header("Request an Employee")

    st.write("""
We connect employers with trusted Warehouse Associates, Office Assistants, Restaurant Staff, and more.
Click below to submit your request.
""")

    st.markdown("""
### 👉 Apply Here
https://forms.gle/XmcHx4YiJWG2FJYi6
""")

elif page == "Looking for Work - Apply Now":

    st.header("Apply for Employment")

    st.write("We help qualified individuals find employment with families and businesses. Click below to submit your application.")

    st.markdown("""
### 👉 Apply Here
https://forms.gle/edAw8KJ9aTZe4XXLA
""")
    

elif page == "Contact":

    st.header("Contact Us")

    st.write("📞 Phone: (555) 555-5555")

    st.write("📧 Email: caringgememploymentagency@gmail.com")

    st.write("Business Hours")

    st.write("""
Monday-Friday

9:00 AM - 6:00 PM
""")