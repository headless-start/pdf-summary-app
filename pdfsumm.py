import os
import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with OpenRouter.ai's base URL and your API key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,  
)

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to summarize text using OpenRouter.ai
def summarize_text(text):
    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://your-site-url.com",  # Not putting anything now, plans to host this app
                "X-Title": "Your Site Name",  # Not putting anything now
            },
            extra_body={},
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text.",
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text:\n\n{text}",
                },
            ],
        )
        # Check if the response is valid
        if response and response.choices and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            st.error("The API returned an invalid response. Please try again.")
            return None
    except Exception as e:
        st.error(f"An error occurred while summarizing the text: {e}")
        return None

# Streamlit App
def main():
    st.title("📄 PDF Summary Tool")
    st.write("Upload a PDF file, and I'll summarize it for you!")

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file is not None:
        # Extract text from the PDF
        with st.spinner("Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            st.success("Text extracted successfully!")

        # Display the extracted text (optional)
        if st.checkbox("Show extracted text"):
            st.write(text)

        # Summarize the text
        if st.button("Summarize"):
            with st.spinner("Generating summary..."):
                summary = summarize_text(text)
                if summary:
                    st.success("Summary generated!")
                    st.write("### Summary:")
                    st.write(summary)

                    # Download button for the summary
                    st.download_button(
                        label="Download Summary",
                        data=summary,
                        file_name="summary.txt",
                        mime="text/plain",
                    )

# Run the app
if __name__ == "__main__":
    main()