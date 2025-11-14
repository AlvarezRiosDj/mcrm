import strawberry
from typing import Optional

@strawberry.type
class OperationResult:
    success: bool
    message: Optional[str]