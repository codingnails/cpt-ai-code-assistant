# CPT AI Code Assistant

💡 A simple Streamlit app that explains CPT medical codes in plain language using OpenAI GPT and LangChain.

---

## Overview

This prototype app allows users to input a CPT (Current Procedural Terminology) code and a short description, then generates an easy-to-understand explanation powered by OpenAI's GPT models.

It’s designed for healthcare professionals, patients, or anyone curious about medical billing codes, providing accessible insights without medical jargon.

---

## Features

- Input CPT code and short description  
- AI-generated natural language explanation  
- User-friendly Streamlit web interface  
- Easily customizable prompt templates  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- OpenAI API key ([Get yours here](https://platform.openai.com/account/api-keys))  
- (Optional) Create and activate a virtual environment  

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/codingnails/cpt-ai-code-assistant.git   
   cd cpt-ai-code-assistant
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

### Running the App

Start the Streamlit app with:

```bash
streamlit run main.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Project Structure

```
cpt-ai-code-assistant/
├── app/
│   ├── chains/                # LangChain chains (CPT explainer)
│   ├── prompts/               # Prompt templates for GPT
│   └── main.py                # Streamlit UI entry point
├── data/                      # to store mock data
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and setup
```

---

## Customization

* Modify prompts in `app/prompts/system_prompt.txt` and `app/prompts/human_prompt.txt`
* Adjust model parameters in `app/chains/cpt_explainer.py`
* Enhance the UI in `main.py`

---

## Limitations

* Prototype only — not production-ready
* No official CPT dataset included (requires AMA license)
* Quality metrics and tests are not implemented (optional for future)
* Dependent on OpenAI API availability and usage limits

---

## Contact

For questions or suggestions, please open an issue or contact [rupaligupta.tech@gmail.com](mailto:rupaligupta.tech@gmail.com).


