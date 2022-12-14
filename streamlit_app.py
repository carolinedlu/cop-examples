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

st.success('This is a success message!', icon="â")

st.info('This is a purely informational message', icon="âšī¸")

st.error('This is an error', icon="đ¨")

st.warning('This is a warning', icon="â ī¸")


