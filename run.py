from src.main import main

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python run.py <pdf_path> <slack_channel> question1 [question2 ...]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    slack_channel = sys.argv[2]
    questions = sys.argv[3:]
    
    results = main(pdf_path, questions, slack_channel)
    print("Results:", results)