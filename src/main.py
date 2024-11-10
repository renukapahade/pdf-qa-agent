from typing import List, Dict
import argparse
import logging
from .config import Config
from .document_processor import DocumentProcessor
from .llm_service import LLMService
from .slack_service import SlackService

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main(pdf_path: str, questions: List[str], slack_channel: str) -> Dict[str, str]:
    try:
        logger.info(f"Processing PDF: {pdf_path}")
        logger.info(f"Questions to answer: {questions}")
        
        # Initialize services
        doc_processor = DocumentProcessor(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
        
        llm_service = LLMService(
            api_key=Config.OPENAI_API_KEY,
            model_name=Config.MODEL_NAME
        )
        
        slack_service = SlackService(token=Config.SLACK_BOT_TOKEN)
        
        # Process document and get relevant chunks for each question
        logger.info("Processing document and finding relevant contexts...")
        contexts = doc_processor.process_document(pdf_path, questions)
        
        # Get answers using LLM
        logger.info("Generating answers using LLM...")
        results = llm_service.process_questions(questions, contexts)
        
        # Post to Slack
        logger.info(f"Posting results to Slack channel: {slack_channel}")
        slack_service.post_results(slack_channel, results)
        
        return results
        
    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF Question-Answering Agent")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--questions", required=True, nargs="+", help="List of questions")
    parser.add_argument("--slack-channel", required=True, help="Slack channel to post results")
    
    try:
        args = parser.parse_args()
        results = main(args.pdf, args.questions, args.slack_channel)
        print("Results:", results)
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise