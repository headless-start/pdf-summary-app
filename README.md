# 📄 PDF Summary Tool  

## 📌 Project Overview  
This project demonstrates the **loading, preprocessing, and summarization** of text from **PDF files** using **Streamlit** and **LLM APIs like (Deepseek r1,o3-mini)**. The application allows users to upload a PDF, extract its text, and generate a concise summary. The summary can be downloaded as a `.txt` file for offline use.  

---

## 🚀 Key Features  
1. **PDF Summarization**  
   - Users can upload a PDF file (up to 200MB) and get the summary of the document.  

---

## 🔍 How It Works  
1. **Upload a PDF**:  
   - Users upload a PDF file using the file uploader in the app.  
2. **Extract Text**:  
   - The app extracts text from the PDF using the `PyPDF2` library.  
3. **Generate Summary**:  
   - The extracted text is sent to the LLM API (Deepseek r1, o3-mini), which generates a summary.  
4. **Display and Download**:  
   - The summary is displayed on the app, and users can download it as a `.txt` file.  

**Check Demo Here**:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdfdeepv1.streamlit.app/)  

---

## 🛠 System Requirements  

### Dependencies  
- Python 3.8+  
- Libraries: `streamlit`, `PyPDF2`, `openai`  
- Hardware: CPU (GPU not required)  

---

## 📄 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  
