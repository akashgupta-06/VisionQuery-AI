# VisionQuery AI

*A multimodal Generative AI app that understands images and answers natural-language questions.*

VisionQuery AI is a Streamlit-based application powered by Google Gemini that allows users to upload an image and ask contextual questions about it. The system performs visual reasoning and returns intelligent, human-like insights.

This project demonstrates how to build **real-world, multimodal GenAI products**—not just scripts.

---

## ✨ Features

- Upload any image (JPG / PNG)
- Ask natural-language questions about the image
- AI understands visual context and responds intelligently
- Works with:
  - Image-only prompts
  - Image + text prompts
- Clean, product-style UI
- Secure API key handling via `.env`

---

## 🧠 Use Cases

- Visual inspection tools
- OCR and scene understanding
- Product analysis from images
- Education & learning assistants
- AI-powered image interpretation

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit** – Frontend UI
- **Google Gemini (google-genai SDK)** – Multimodal AI
- **Pillow (PIL)** – Image handling
- **python-dotenv** – Secure config management

---

## 📁 Project Structure

VisionQuery-AI/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── assets/
│   ├── demo.png
     └── sample.jpg

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/VisionQuery-AI.git
cd VisionQuery-AI
```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file

   ```
   cp .env.example .env
   ```
4. Add your API key to `.env`

   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the app:

   ```
   streamlit run app.py
   ```
