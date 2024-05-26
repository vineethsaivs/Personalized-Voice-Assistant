# Personalized-Voice-Assistant

```markdown
# Personalized Voice Assistant with Self-Learning Capabilities

This project is a personalized voice assistant that uses various machine learning models and libraries to process and respond to user input in the user's own voice and style. It's built with Python and Streamlit.

## Features

- Audio recording and processing
- MP3 file uploading and processing
- Conversational retrieval chain for handling user input
- Text splitting and embedding for document processing
- Personalized reminders based on user's tasks and interactions

## Installation

Clone the repository:

```bash
git clone https://github.com/vineethsaivs/Personalized-Voice-Assistant.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:

```bash
streamlit run streamlit.py
```

## Environment Variables

This project uses the following environment

 variables

:

- `DG_API_KEY`: Your Deepgram API key
- `GROQ_API_KEY`: Your GROQ API key

You can set these in a `.env` file in the root of your project:

```env
DG_API_KEY=your_deepgram_api_key
GROQ_API_KEY=your_groq_api_key
```

## How It Works

The voice assistant takes in audio input, transcribes it using the Deepgram API, and processes the transcript into a vector store using HuggingFace BgeEmbeddings and FAISS. It then uses a conversational retrieval chain to handle user input and generate responses.

The assistant is personalized to the user by training on the user's voice and style. It can access the user's tasks and interactions, and provide reminders in the user's own voice. For example, it can remind the user to complete tasks or to speak with a contact if it has been a while since the last interaction.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
