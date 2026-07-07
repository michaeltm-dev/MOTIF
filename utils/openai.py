from typing import Dict, List, Optional, Tuple

from openai import OpenAI

from utils.format.response import CompetitiveResponse

class LLMClient:
    """
    OpenAI Responses API client for competitive MCTS.
    """
    def __init__(
        self,
        model: str = "gpt-4o-mini",
        temperature: float = 1.0
    ) -> None:
        """
        Initialize the LLM client.
        
        Args:
            model: The model to use for generation
            temperature: The temperature to use for generation
        """
        self.model = model
        self.temperature = temperature

        self.client = OpenAI()

    def _require_responses_api(self):
        if not hasattr(self.client, "responses"):
            raise RuntimeError(
                "Installed openai package does not support the Responses API. "
                "Install the version from requirements.txt."
            )
    
    def get_response(self, messages: List[Dict[str, str]], function_id: Optional[str] = None, temperature: Optional[float] = None) -> str:
        """
        Generate text response from the model.
        
        Args:
            messages: List of message dictionaries
            function_id: Optional function ID for logging
            temperature: Optional temperature override
            
        Returns:
            Text response from the model
        """
        temp = temperature if temperature is not None else self.temperature
        
        self._require_responses_api()

        response = self.client.responses.create(
            model=self.model,
            input=messages,
            temperature=temp,
        )
        
        return response.output_text

    def get_code(self, messages: List[Dict[str, str]], function_id: Optional[str] = None, temperature: Optional[float] = None) -> Tuple[str, str, str]:
        """
        Generate code response using structured format.
        
        Args:
            messages: List of message dictionaries
            function_id: Optional function ID for logging
            temperature: Optional temperature override
            
        Returns:
            Tuple of (reasoning, code, summary)
        """
        temp = temperature if temperature is not None else self.temperature

        self._require_responses_api()

        response = self.client.responses.parse(
            model=self.model,
            input=messages,
            temperature=temp,
            text_format=CompetitiveResponse,
        )

        # Return in expected format (code, explanation, summary)
        parsed = response.output_parsed
        return parsed.reasoning, parsed.code, parsed.summary
