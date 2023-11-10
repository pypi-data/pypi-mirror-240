from pydantic import BaseModel, Field
from typing import List, Any, Optional


class FeedbackItem(BaseModel):
    id: str
    nm_id: int = Field(..., validation_alias='nmId')
    text: str
    product_valuation: int = Field(..., validation_alias='productValuation')


class Feedback(BaseModel):
    count: int = Field(..., validation_alias='feedbackCount')
    count_with_photo: int = Field(..., validation_alias='feedbackCountWithPhoto')
    count_with_text: int = Field(..., validation_alias='feedbackCountWithText')
    items: Optional[List[FeedbackItem]] = Field(..., validation_alias='feedbacks')

    @classmethod
    def from_resp(cls, response: dict) -> 'Feedback':
        return cls(**response)

    def is_empty(self) -> bool:
        return not bool(self.items)

    def get_comments(self) -> List[str]:
        return [item.text.lower() for item in self.items]


class ProductItem(BaseModel):
    id: int
    root: int
    name: str
    rating: float
    review_rating: float = Field(..., validation_alias='reviewRating')


class Products(BaseModel):
    products: List[ProductItem]


class Card(BaseModel):
    state: int
    params: Any
    data: Products

    @classmethod
    def from_resp(cls, response: dict) -> 'Card':
        return cls(**response)
