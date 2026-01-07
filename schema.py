from typing import Optional

from pydantic import BaseModel, Field


class InvoiceInfo(BaseModel):
    invoice_number: str = Field(..., description="Unique invoice number")
    total_amount: float = Field(..., description="Total amount of the invoice")
    tax_amount: Optional[float] = Field(
        None, description="Tax included in the total amount"
    )
    company_name: Optional[str] = Field(None, description="Name of the issuing company")
    company_address: Optional[str] = Field(
        None, description="Address of the issuing company"
    )
