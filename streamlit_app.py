import streamlit as st

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )

st.success('This is a success message!', icon="✅")

st.info('This is a purely informational message', icon="ℹ️")

st.error('This is an error', icon="🚨")

st.warning('This is a warning', icon="⚠️")


