# LangChain Tutorial: AI Chatbot with Groq and Ollama

A comprehensive tutorial project demonstrating how to build AI-powered chatbots using LangChain, integrating Groq's fast LLMs and Ollama's local models. This project includes a FastAPI backend for API endpoints and a Streamlit frontend for an interactive UI.

## 🚀 Features

- **Dual LLM Integration**: Use Groq for cloud-based, high-speed responses and Ollama for local, privacy-focused models.
- **FastAPI Backend**: RESTful API with LangServe for easy model serving.
- **Streamlit Frontend**: User-friendly web interface for generating essays and poems.
- **Modular Design**: Separate API and client components for scalability.
- **Error Handling**: Robust error management in both backend and frontend.
- **Environment Management**: Secure API key handling with `.env` files.

## 📁 Project Structure

```
langchain_tutorial/
├── api/                    # FastAPI backend
│   ├── app.py             # Main FastAPI application
│   ├── client.py          # Streamlit client
│   └── README.md          # This file
├── chatbot/               # Additional chatbot implementations
│   ├── app.py
│   └── localama.py
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── .env                  # Environment variables (not committed)
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Git
- Ollama (for local models)
- GitHub account (for API keys)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/api.git
   cd api
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

5. **Install Ollama** (for local models):
   - Download from [ollama.ai](https://ollama.ai)
   - Pull the required model: `ollama pull gemma3:1b`

## 🚀 Usage

### Running the FastAPI Backend

```bash
cd api
python app.py
```

The API will be available at `http://localhost:8000`.

### API Endpoints

- `GET /`: API documentation (Swagger UI)
- `POST /chat/groq/invoke`: Chat with Groq model
- `POST /essay/invoke`: Generate essays using Groq
- `POST /poem/invoke`: Generate poems using Ollama

### Running the Streamlit Client

```bash
cd api
streamlit run client.py
```

Open your browser to `http://localhost:8501` for the interactive UI.

### Example API Usage

```python
import requests

# Generate an essay
response = requests.post("http://localhost:8000/essay/invoke",
                        json={"input": {"topic": "Climate Change"}})
print(response.json())

# Generate a poem
response = requests.post("http://localhost:8000/poem/invoke",
                        json={"input": {"topic": "Nature"}})
print(response.json())
```

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (get from [groq.com](https://groq.com))
- `LANGCHAIN_API_KEY`: LangChain API key for tracing (optional)

### Model Configuration

- Groq Model: `llama-3.3-70b-versatile`
- Ollama Model: `gemma3:1b`

Modify `app.py` to change models or add new ones.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com) for the LLM framework
- [Groq](https://groq.com) for fast inference
- [Ollama](https://ollama.ai) for local model serving
- [FastAPI](https://fastapi.tiangolo.com) for the web framework
- [Streamlit](https://streamlit.io) for the UI

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Ensure virtual environment is activated and dependencies are installed.
2. **API Key Errors**: Check your `.env` file and ensure keys are valid.
3. **Connection Refused**: Make sure the FastAPI server is running.
4. **Ollama Errors**: Ensure Ollama is installed and the model is pulled.

### Getting Help

- Check the [LangChain Documentation](https://python.langchain.com)
- Open an issue on GitHub
- Join the [LangChain Discord](https://discord.gg/langchain)

---

# ME