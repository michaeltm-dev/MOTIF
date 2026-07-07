from pydantic import BaseModel, Field, field_validator

class CompetitiveResponse(BaseModel):
    """
    Response format for competitive operators.
    Contains code and concise summary.
    """
    reasoning: str = Field(
        ...,
        title="Reasoning",
        description="Concise reasoning for the implementation (maximum 50 words)"
    )
    code: str = Field(
        ..., 
        title="Implementation Code", 
        description="Complete function implementation"
    )
    summary: str = Field(
        ..., 
        title="Change Summary", 
        description="One-line summary of changes made (max 100 characters)"
    )

    @field_validator("reasoning")
    @classmethod
    def limit_reasoning_words(cls, value: str) -> str:
        if len(value.split()) > 50:
            raise ValueError("reasoning must be at most 50 words")
        return value
