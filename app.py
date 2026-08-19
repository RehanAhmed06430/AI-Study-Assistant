import streamlit as st

from chains import study_chain


# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)


# Title
st.title("🤖 AI Study Assistant")

st.write(
    "Learn smarter, revise faster, and prepare for interviews with AI."
)


# User inputs
topic = st.text_input(
    "📚 Enter Topic",
    placeholder="e.g. Binary Search"
)


language = st.selectbox(
    "💻 Select Programming Language",
    [
        "C++",
        "Python",
        "Java",
        "JavaScript",
        "C"
    ]
)


# Generate button
if st.button("🚀 Generate Study Material"):

    if not topic.strip():

        st.warning("Please enter a topic first.")

    else:

        with st.spinner("Generating your study material..."):

            result = study_chain.invoke({
                "topic": topic,
                "language": language
            })


        # Explanation
        st.header("📖 Explanation")

        st.write(result["explanation"])


        # Notes
        st.header("📝 Short Notes")

        st.write(result["notes"])


        # Interview Questions
        st.header("🎯 Interview Questions")

        st.write(result["interview"])


        # Code
        st.header("💻 Code")

        st.code(
            result["code"],
            language=language.lower()
        )


        # Quick Revision
        st.header("⚡ Quick Revision")

        st.write(result["quickrevision"])