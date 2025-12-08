from pydantic import BaseModel, Field

class CompetitiveResponse(BaseModel):
    """
    Response format for competitive operators.
    Contains code and concise summary.
    """
    reasoning: str = Field(
        ...,
        title="Reasoning",
        description="Step-by-step reasoning for your implementation (max 5 steps)"
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