import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
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
    if torch.cuda.is_available():
        inputs = inputs.to("cuda")

    outputs = model.generate(
        inputs,
        max_length=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.replace(user_input, "").strip()
    st.markdown(f"**LLaMA:** {response}")
