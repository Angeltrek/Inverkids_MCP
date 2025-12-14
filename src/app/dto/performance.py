from dataclasses import dataclass
from typing import Optional, Literal

Scope = Literal["module", "topic", "global"]
Metric = Literal["average", "latest", "trend"]
Order = Literal["lowest", "highest"]

@dataclass(frozen=True)
class StudentGradeSummaryInput:
    scope: Literal["module", "topic"]
    scope_id: str
    metric: Metric = "average"


@dataclass(frozen=True)
class StudentsByPerformanceInput:
    scope: Scope
    scope_id: Optional[str]
    order: Order
    limit: int = 5
