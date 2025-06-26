# TinyLLaMA Chatbot

A beginner-friendly chatbot using Meta’s TinyLLaMA model, Streamlit, and Hugging Face 
This project allows you to chat with a small, efficient open-source language model using a clean web interface.
This project is a simple and beginner-friendly AI chatbot built using Meta’s TinyLLaMA language model and Streamlit. It leverages Hugging Face’s transformers library to load and run a lightweight open-source model locally, making it a great starting point for understanding how language models work in real-time applications. The chatbot takes user input, processes it with the TinyLLaMA model, and responds naturally through a clean and interactive web interface. Ideal for students, developers, and hobbyists who want to explore LLMs without needing heavy computing resources.
![Screenshot (820)](https://github.com/user-attachments/assets/234f72f8-0e36-44c5-bf02-3f902d049ed9)
![Screenshot (821)](https://github.com/user-attachments/assets/6df94107-4f97-4f31-8770-15f3d0915b2a)


---

##  Demo

To run the chatbot locally:

```bash
streamlit run app.py
```

---

## Project Structure

```
llama_chatbot/
├── app.py             # Streamlit chatbot code
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

##  Requirements

- Python 3.8+
- pip
- Internet connection (to download the model)

###  Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, here’s what to install manually:

```bash
pip install torch transformers streamlit
```

---

## Sample Prompts to Try

- What is artificial intelligence?
- Tell me a fun fact.
- Explain Python like I’m five.
- Write a short poem about the moon.
- Who is the president of India?

---

## How It Works

1. The app loads the TinyLLaMA model and tokenizer from Hugging Face.
2. You enter a question or prompt via a simple Streamlit UI.
3. The model processes the input and generates a natural language response.
4. The chatbot shows the response in the browser.

---

## Model Used

- [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

> TinyLLaMA is a lightweight and efficient open-source large language model trained for chat-based tasks.

---

##  Deploy (Optional)

You can deploy this chatbot using:
- **Streamlit Community Cloud**: [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Or host locally and share over a network

---

##  License

MIT License

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Made with  using open-source tools.
