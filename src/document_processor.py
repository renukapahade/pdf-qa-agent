from PyPDF2 import PdfReader
from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self, chunk_size: int, chunk_overlap: int):
        """
        Initialize the DocumentProcessor.
        
        Args:
            chunk_size (int): Number of characters per chunk
            chunk_overlap (int): Number of characters to overlap between chunks
        """
        self.chunk_size = int(chunk_size)  # Ensure these are integers
        self.chunk_overlap = int(chunk_overlap)
        self.vectorizer = TfidfVectorizer()
        
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file"""
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + " "
            return text.strip()
        except Exception as e:
            logger.error(f"Failed to extract text from PDF: {e}")
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    def create_chunks(self, text: str) -> List[str]:
        """
        Split text into chunks of specified size with overlap.
        Uses character-based chunking instead of word-based.
        """
        try:
            chunks = []
            if not text:
                return chunks
                
            # Convert sizes from words to characters if needed
            chunk_size = self.chunk_size
            overlap = self.chunk_overlap
            
            # Calculate start indices for chunks
            start_indices = list(range(0, len(text), chunk_size - overlap))
            
            # Create chunks
            for start_idx in start_indices:
                end_idx = start_idx + chunk_size
                # Don't exceed text length
                if end_idx > len(text):
                    end_idx = len(text)
                # Add chunk if it has content
                chunk = text[start_idx:end_idx].strip()
                if chunk:
                    chunks.append(chunk)
                # Break if we've reached the end
                if end_idx == len(text):
                    break
                    
            logger.info(f"Created {len(chunks)} chunks from text")
            return chunks
            
        except Exception as e:
            logger.error(f"Failed to create chunks: {e}")
            raise Exception(f"Error creating chunks: {str(e)}")
    
    def find_relevant_chunks(self, question: str, chunks: List[str], top_k: int = 2) -> List[str]:
        """Find most relevant chunks for a question using TF-IDF and cosine similarity"""
        try:
            if not chunks:
                return []
            if not question.strip():
                return chunks[:top_k]
                
            # Create document matrix
            all_texts = chunks + [question]
            
            # Fit and transform the texts
            tfidf_matrix = self.vectorizer.fit_transform(all_texts)
            
            # Calculate similarities between question and chunks
            similarities = cosine_similarity(
                tfidf_matrix[-1:],  # Question vector (last element)
                tfidf_matrix[:-1]   # Chunk vectors (all except last)
            )[0]
            
            # Get indices of top_k similar chunks
            top_indices = np.argsort(similarities)[-top_k:][::-1]
            
            # Return the most relevant chunks
            return [chunks[i] for i in top_indices]
            
        except Exception as e:
            logger.error(f"Failed to find relevant chunks: {e}")
            raise Exception(f"Error finding relevant chunks: {str(e)}")

    def process_document(self, pdf_path: str, questions: List[str]) -> dict:
        """Process document and find relevant chunks for all questions"""
        try:
            # Extract text from PDF
            logger.info(f"Extracting text from {pdf_path}")
            text = self.extract_text(pdf_path)
            
            # Create chunks
            logger.info("Creating chunks from extracted text")
            chunks = self.create_chunks(text)
            
            if not chunks:
                raise ValueError("No chunks were created from the document")
            
            # Find relevant chunks for each question
            logger.info("Finding relevant chunks for each question")
            results = {}
            for question in questions:
                relevant_chunks = self.find_relevant_chunks(question, chunks)
                results[question] = relevant_chunks
                
            return results
            
        except Exception as e:
            logger.error(f"Failed to process document: {e}")
            raise Exception(f"Error processing document: {str(e)}")