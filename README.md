# AI Email Generator

A simple Streamlit app that uses Groq and LangChain to generate professional emails from a topic and selected tone.

## Features

- Generate AI-written emails in seconds
- Choose from `Formal`, `Friendly`, or `Professional` tone
- Clean Streamlit interface with sidebar controls
- Preview the generated email in the browser
- Download the result as a `.txt` file

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- `llama-3.1-8b-instant`

## Project Structure

```text
ai-email-generator/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .streamlit/
```

## Requirements

- Python 3.10+ recommended
- A Groq API key

## Installation

```bash
git clone https://github.com/nandhini0778/AI_Email_generator.git
cd ai-email-generator
pip install -r requirements.txt
```

## Configure API Key

The app expects a Groq API key in either an environment variable or Streamlit secrets.

### Option 1: Environment Variable

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_api_key"
streamlit run app.py
```

### Option 2: Streamlit Secrets

Create `.streamlit/secrets.toml` and add:

```toml
GROQ_API_KEY = "your_api_key"
```

Then run:

```bash
streamlit run app.py
```

## Usage

1. Enter an email topic in the sidebar.
2. Select the tone.
3. Click `Generate Email`.
4. Review the generated email.
5. Download it as a text file if needed.

## Example Topics

- Leave request
- Meeting follow-up
- Project deadline update
- Client introduction
- Internship application

## Notes

- If the API key is missing, the app will stop and show an error.
- Generated content depends on the selected tone and the topic you provide.

## License

This project is open for educational use.

## Output

<img width="1911" height="981" alt="Screenshot (79)" src="https://github.com/user-attachments/assets/179490f4-b8aa-45fa-aa68-177ed69588eb" />

