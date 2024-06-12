import streamlit as st

from phi.tools.streamlit.components import check_password

st.set_page_config(
    page_title="AI tutor",
    page_icon="🧑‍🏫",
)
st.title("Aacharya: An AI tutor")


def main() -> None:
    st.markdown("---")
    st.markdown("### Select a task :")
    st.markdown("#### 1. Tutor: Simplify lessons for you")
    st.markdown("#### 2. Test: Test your knowledge")
    st.markdown("#### 3. AMA: Helps you learn any topic from anywhere")

    st.sidebar.success("Select a task from above")


if check_password():
    main()
