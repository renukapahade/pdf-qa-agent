from typing import Dict
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

class SlackService:
    def __init__(self, token: str):
        self.client = WebClient(token=token)
        
    def post_results(self, channel: str, results: Dict[str, str]) -> None:
        """Post results to Slack channel"""
        try:
            formatted_results = json.dumps(results, indent=2)
            self.client.chat_postMessage(
                channel=channel,
                text=f"Question-Answer Results:\n```{formatted_results}```"
            )
        except SlackApiError as e:
            print(f"Error posting message: {e.response['error']}")
