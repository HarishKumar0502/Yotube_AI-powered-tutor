import os
import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from youtube_transcript_api import CouldNotRetrieveTranscript
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq

from pytube import YouTube
from youtube_transcript_api import(
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,

)
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

def youtube_tran(url):
    try:
        Vid_id=YouTube(url).video_id
        api=YouTubeTranscriptApi()
        transcript_list= api.list(Vid_id)
        transcript =transcript_list.find_transcript(["en"])
        data=transcript.fetch()
        text="\n".join([item.text for item in data])
        return text
    except TranscriptsDisabled:
        st.error("Transcript Disabled")
    except NoTranscriptFound:
        st.error("Transcripted not found ")
    except VideoUnavailable:
        st.error("Video is unavailable")
    except CouldNotRetrieveTranscript:
        st.error("Could not retrival transcript")
    except Exception as e:
            st.error(f"unecpeted error {e}")

def save_transcript_t0_file(text,filename="transcript.txt"):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(text)

st.set_page_config(page_title="AI Powered Tutor")
st.set_page_config(page_title="AI Powered Tutor")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "qa_chain" not in st.session_state:
    st.session_state["qa_chain"] = None
st.title("AI power tutor")
st.write("Ask a question from youtube lecture")

vid_url=st.text_input("Enter Youtube URL")

if st.button("Procees Video"):
    if vid_url:
        transcript_text=youtube_tran(vid_url)
        if transcript_text:
            save_transcript_t0_file(transcript_text)

            loader=TextLoader("transcript.txt",encoding="utf-8")
            documents=loader.load()

            splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
            docs=splitter.split_documents(documents)
            embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            vectorstores=FAISS.from_documents(docs,embedding)
            retriever = vectorstores.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k": 2}
                    )
            llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0
                )
            prompt = ChatPromptTemplate.from_template("""You are a helpful AI tutor.

                    Answer ONLY from the given context.

                    Context:
                    {context}

                    Question:
                    {input}
                    """)
            document_chain = create_stuff_documents_chain(
                llm,
                prompt)
            qa_chain = create_retrieval_chain(
                retriever,
                document_chain)

            st.session_state["qa_chain"]=qa_chain
            st.success("Transcripted successfull, you can ask question")

        else:
            st.warning("please enter url")
if st.session_state["qa_chain"] is not None:

    # Display previous messages
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask your question")

    if question:

        # User message
        st.session_state["messages"].append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("Thinking..."):
            response = st.session_state["qa_chain"].invoke(
                {
                    "input": question
                }
            )

        answer = response["answer"]

        # Assistant message
        st.session_state["messages"].append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.markdown(answer)