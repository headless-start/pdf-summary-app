# 📄 PDF Summary Tool  

## 📌 Project Overview  
This project demonstrates the **loading, preprocessing, and summarization** of text from **PDF files** using **Streamlit** and **DeepSeek R1** through the **OpenRouter** API. The application allows users to upload a PDF, extract its text, and generate a concise summary. The summary can be downloaded as a `.txt` file for offline use.  

---

## 🚀 Key Features  
1. **PDF Summarization**  
   - Users can upload a PDF file (up to 200MB) and get the summary of the document.  

---

## 🔍 How It Works  
1. **Upload a PDF**:  
   - Users upload a PDF file using the file uploader in the app.  
2. **Extract Text**:  
   - The app extracts text from the PDF using the `PyPDF2` library. You can tick "Show extracted text" to check it first.  
3. **Generate Summary**:  
   - The extracted text is sent to DeepSeek R1 (`deepseek/deepseek-r1:free`) on OpenRouter, called through the `openai` Python client, which returns the summary.  
4. **Display and Download**:  
   - The summary is displayed on the app, and users can download it as a `.txt` file.  

**Check Demo Here**:  
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdfdeepv1.streamlit.app/)  

---

## 🛠 System Requirements  

### Dependencies  
- Python 3.8+  
- Libraries: `streamlit`, `PyPDF2`, `openai`, `python-dotenv`  
- Hardware: CPU (GPU not required)  

### API key  
The app reads an OpenRouter API key from the `OPENAI_API_KEY` environment variable (a `.env` file works too, it's loaded with `python-dotenv` and already gitignored).  

```bash
echo "OPENAI_API_KEY=your-openrouter-key" > .env
streamlit run pdfsumm.py
```  

---

## 📄 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  
