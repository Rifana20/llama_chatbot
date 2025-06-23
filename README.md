# 🦙 TinyLLaMA Chatbot

A beginner-friendly chatbot using Meta’s TinyLLaMA model, Streamlit, and Hugging Face 🤖  
This project allows you to chat with a small, efficient open-source language model using a clean web interface.
![Screenshot (820)](https://github.com/user-attachments/assets/234f72f8-0e36-44c5-bf02-3f902d049ed9)
![Screenshot (821)](https://github.com/user-attachments/assets/6df94107-4f97-4f31-8770-15f3d0915b2a)


---

## 🚀 Demo

To run the chatbot locally:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
llama_chatbot/
├── app.py             # Streamlit chatbot code
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## 📦 Requirements

- Python 3.8+
- pip
- Internet connection (to download the model)

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, here’s what to install manually:

```bash
pip install torch transformers streamlit
```

---

## 💬 Sample Prompts to Try

- What is artificial intelligence?
- Tell me a fun fact.
- Explain Python like I’m five.
- Write a short poem about the moon.
- Who is the president of India?

---

## 🧠 How It Works

1. The app loads the TinyLLaMA model and tokenizer from Hugging Face.
2. You enter a question or prompt via a simple Streamlit UI.
3. The model processes the input and generates a natural language response.
4. The chatbot shows the response in the browser.

---

## 🌐 Model Used

- [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

> TinyLLaMA is a lightweight and efficient open-source large language model trained for chat-based tasks.

---

## 🛠 Example Code Snippet

Here's a short snippet from `app.py`:

```python
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

st.title("🦙 Tiny LLaMA Chatbot")

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    ).to(device)
    return tokenizer, model

tokenizer, model = load_model()
user_input = st.text_input("You:", placeholder="Ask me anything...")

if user_input:
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt").to(model.device)
    outputs = model.generate(inputs, max_length=256, do_sample=True, temperature=0.7, top_p=0.9)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.replace(user_input, "").strip()
    st.markdown(f"**LLaMA:** {response}")
```

---

## 📤 Deploy (Optional)

You can deploy this chatbot using:
- **Streamlit Community Cloud**: [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Or host locally and share over a network

---

## 📜 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Made with ❤️ using open-source tools.
