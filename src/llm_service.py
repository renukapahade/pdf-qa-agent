from openai import OpenAI
from typing import List, Dict

class LLMService:
    def __init__(self, api_key: str, model_name: str):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        
    def get_answer(self, question: str, context: List[str]) -> str:
        """Get answer from OpenAI API"""
        prompt = f"""
        Based on the following context, answer the question.
        If the answer cannot be found in the context or you're not confident, 
        reply with "Data Not Available".
        
        Context:
        {' '.join(context)}
        
        Question: {question}
        """
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.0
        )
        
        return response.choices[0].message.content.strip()

    def process_questions(self, questions: List[str], contexts: Dict[str, List[str]]) -> Dict[str, str]:
        """Process multiple questions and return JSON response"""
        results = {}
        for question in questions:
            answer = self.get_answer(question, contexts[question])
            results[question] = answer
            
        return results