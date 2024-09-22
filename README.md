# Multilingual Translator

This Streamlit application allows users to translate English text into various languages using pre-trained Transformer-based machine translation models.
- **User-Friendly Interface:** Simple and intuitive UI for entering text and selecting the target language.

## Features


- Supports translation to the following languages: French, Spanish, German, Italian, Urdu, and Arabic.
- Provides a clean and user-friendly interface for entering the text to be translated and selecting the target language.
- Displays the translated text in the selected language.
- Deployed on Hugging Face.

## How it Works

1. **User Input**: The application presents a text area where the user can enter the English text they want to translate.
2. **Language Selection**: The user can select the target language from a dropdown menu. The application supports translation to French, Spanish, German, Italian, Urdu, and Arabic.
3. **Translation Process**:
   - The application loads the pre-trained Transformer-based machine translation model and tokenizer corresponding to the selected target language.
   - The input text is encoded using the tokenizer, and then passed to the translation model's `generate` method to produce the translated text.
   - The translated text is decoded, skipping any special tokens, and displayed to the user.
4. **Deployment**: The Multilingual Translator application is deployed on the Hugging Face platform, making it accessible to users without the need for local setup.

## Dependencies

- Python 3.7 or higher
- Streamlit
- Transformers (from Hugging Face)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/multilingual-translator.git
2. Change to the project directory:
   ```bash
   cd multilingual-translator
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
#  Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
2. The application will open in your default web browser.
3. Enter the English text you want to translate in the text area.
4. Select the target language from the dropdown menu.
5. Click the "Translate" button to see the translated text.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- The deployment of this application on Hugging Face was made possible by the Hugging Face platform.
  <br>
[Translator](https://huggingface.co/spaces/Safwanahmad619/Language-Translator) 



