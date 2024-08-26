import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Define a dictionary to map language names to model identifiers
models = {
    'French': 'Helsinki-NLP/opus-mt-en-fr',
    'Spanish': 'Helsinki-NLP/opus-mt-en-es',
    'German': 'Helsinki-NLP/opus-mt-en-de',
    'Italian': 'Helsinki-NLP/opus-mt-en-it',
    'Urdu': 'Helsinki-NLP/opus-mt-en-ur',
    'Arabic': 'Helsinki-NLP/opus-mt-en-ar', 
    # Add more language models if needed
}

def load_model(model_name):
    """Load the model and tokenizer based on the selected model name."""
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

def translate_text(text, model, tokenizer):
    """Translate text using the provided model and tokenizer."""
    inputs = tokenizer.encode(text, return_tensors="pt")
    translated = model.generate(inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

def main():
    st.title("Multilingual Translator")

    # User input for English text
    text_to_translate = st.text_area("Enter text in English:")

    # Language options
    selected_language = st.selectbox("Select target language:", list(models.keys()))

    if st.button("Translate"):
        if text_to_translate:
            # Load the selected model
            model_name = models[selected_language]
            model, tokenizer = load_model(model_name)
            
            translated_text = translate_text(text_to_translate, model, tokenizer)
            st.write(f"**Translation in {selected_language}:**")
            st.write(translated_text)
        else:
            st.warning("Please enter text to translate.")

    # Add footer
    st.markdown("---")
    st.markdown("Developed by **Safwan** and deployed on **[Hugging Face](https://huggingface.co/spaces/Safwanahmad619/Language-Translator)**.")

if __name__ == "__main__":
    main()
