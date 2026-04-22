import streamlit as st
from rag_pipeline import create_vector_store, get_qa_chain

st.set_page_config(page_title="AI RAG Chatbot")

st.title("🤖 AI Chatbot (RAG)")
st.write("Upload a text file and ask questions")

# Initialize state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "history" not in st.session_state:
    st.session_state.history = []

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

# When file uploaded
if uploaded_file is not None and st.session_state.qa_chain is None:
    with open("data.txt", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded!")

    vector_store = create_vector_store("data.txt")
    st.session_state.qa_chain = get_qa_chain(vector_store)

    st.rerun()  # force refresh

# Chat UI
if st.session_state.qa_chain is not None:
    st.markdown("### 💬 Ask your question")

    query = st.text_input("Type your question here:")

    if query:
        answer = st.session_state.qa_chain(query)

        # store history
        st.session_state.history.append((query, answer))

    # display chat history
    for q, a in st.session_state.history:
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 Bot:** {a}")

else:
    st.info("👆 Upload a file to start")