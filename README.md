# PDF Question-Answering Agent

An AI agent that leverages OpenAI's language model to extract answers from PDF documents and post results to Slack. The agent uses custom document processing and semantic search to provide accurate answers based on document content.

## Features

- **PDF Processing**: Extract and process text from PDF documents
- **Chunking**: Splits documents into semantically meaningful chunks with overlap
- **Search**: Uses TF-IDF and cosine similarity for relevant context retrieval
- **OpenAI Integration**: Leverages GPT models for accurate answer generation
- **Slack Integration**: Automatically posts results to specified Slack channels
- **Additional**: Includes logging, error handling

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Slack Bot Token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/renukapahade/pdf-qa-agent.git
cd pdf-qa-agent
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package and dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

4. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your-openai-api-key
SLACK_BOT_TOKEN=your-slack-bot-token
MODEL_NAME=gpt-4o-mini
CHUNK_SIZE=4000
CHUNK_OVERLAP=200
```

## Usage

```bash
python run.py handbook.pdf "#welcome"  "What is the name of the company?" "Who is the CEO of the company?" "What is their vacation policy?" "What is the termination policy?"
```


## Project Structure

```
pdf-qa-agent/
├── src/
│   ├── __init__.py
│   ├── config.py           # Configuration management
│   ├── document_processor.py # PDF processing and chunking
│   ├── llm_service.py      # OpenAI integration
│   ├── slack_service.py    # Slack integration
│   └── main.py            # Main application logic
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
└── run.py
```

## Future Improvements

1. Enhanced Accuracy:
   - Implement embedding-based search
   - Add answer validation
   - Implement confidence scoring
   - Use prompt engineering techniques

2. Scalability:
   - Add async processing for multiple documents
   - Implement caching
   - Add document preprocessing pipeline
   - Support for batch processing

3. Production Features:
   - Add monitoring and metrics
   - Implement rate limiting
   - Add API endpoint
   - Add result persistence
   - Implement user authentication

