# ELI5 Engineer

ELI5 Engineer is an AI-powered Streamlit app that explains engineering concepts in three layers:

1. Explain Like I'm 5
2. Technical Explanation
3. Real-world Applications

It is designed as a clean MVP for fast learning, teaching, demos, and internal tooling experiments.

## Overview

The app takes any engineering topic and uses the OpenAI API to generate a structured explanation that works for both beginners and technical audiences. It is intentionally simple to run, easy to extend, and modular enough to serve as a solid starting point for a larger product.

## Features

- Streamlit interface with a focused, one-topic workflow
- AI-generated explanations in three clearly separated sections
- Loading spinner for a better user experience
- Safe handling for empty input and missing API keys
- Modular prompt management in `prompts.py`
- Reusable OpenAI integration logic in `utils.py`

## Project Structure

```text
eli5-engineer/
├── app.py
├── utils.py
├── prompts.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:

```bash
cp .env.example .env
```

5. Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

6. Start the Streamlit app:

```bash
streamlit run app.py
```

## Example Usage

Enter a topic such as:

- Load balancing
- PID control
- Finite element analysis
- Transformers in AI

The app will generate:

- A child-friendly analogy
- A structured technical explanation
- Practical real-world applications

## Future Improvements

- Save explanation history
- Add streaming responses for faster perceived performance
- Support diagrams or visuals for concepts
- Offer different engineering domains as filters
- Add export options such as PDF or Markdown
- Introduce user accounts and saved favorites

## Notes

- The app loads environment variables with `python-dotenv`.
- By default, the OpenAI client uses `gpt-5.4`.
- You can optionally override the model with `OPENAI_MODEL` in your `.env` file.
