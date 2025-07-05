import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

@st.cache_resource

def load_model():
    model_name = "EleutherAI/gpt-neo-1.3B"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer