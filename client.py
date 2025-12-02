import requests
import streamlit as st

def get_groq_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke",
                                 json={'input': {'topic': input_text}}, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('output', {}).get('content', 'No content returned')
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the server. Ensure FastAPI is running."
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e.response.status_code} - {e.response.reason}"
    except ValueError:
        return "Error: Invalid JSON response from server."
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:8000/poem/invoke",
                                 json={'input': {'topic': input_text}}, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get('output', 'No output returned')
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to the server. Ensure FastAPI is running."
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e.response.status_code} - {e.response.reason}"
    except ValueError:
        return "Error: Invalid JSON response from server."
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="LangChain Demo with Groq & Ollama", page_icon="🤖", layout="wide")

# Sidebar
with st.sidebar:
    st.header("ℹ️ Instructions")
    st.markdown("""
    - Enter a topic in the input fields.
    - Click 'Generate' to create content.
    - Ensure the FastAPI server is running at `http://localhost:8000`.
    - Essays use Groq API; Poems use Ollama.
    """)
    if st.button("Clear All", key="clear_btn"):
        st.session_state.essay_input = ""
        st.session_state.poem_input = ""
        st.rerun()

st.title("🤖 LangChain Demo with Groq and Ollama APIs")
st.markdown("Generate essays and poems using AI models via FastAPI backend.")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Essay Generator")
    st.markdown("Enter a topic to generate an essay using Groq API.")
    input_text = st.text_input("Topic for Essay", placeholder="e.g., Climate Change", key="essay_input")
    if st.button("Generate Essay", key="essay_btn"):
        if input_text.strip():
            with st.spinner("Generating essay..."):
                result = get_groq_response(input_text)
            if "Error:" in result:
                st.error(result)
            else:
                st.success("Essay Generated!")
                st.text_area("Essay Output", value=result, height=200, key="essay_output")
        else:
            st.warning("Please enter a topic.")

with col2:
    st.subheader("🎨 Poem Generator")
    st.markdown("Enter a topic to generate a poem using Ollama API.")
    input_text1 = st.text_input("Topic for Poem", placeholder="e.g., Nature", key="poem_input")
    if st.button("Generate Poem", key="poem_btn"):
        if input_text1.strip():
            with st.spinner("Generating poem..."):
                result = get_ollama_response(input_text1)
            if "Error:" in result:
                st.error(result)
            else:
                st.success("Poem Generated!")
                st.text_area("Poem Output", value=result, height=200, key="poem_output")
        else:
            st.warning("Please enter a topic.")

st.markdown("---")
st.markdown("**Built with Streamlit, FastAPI, LangChain, Groq, and Ollama.**")