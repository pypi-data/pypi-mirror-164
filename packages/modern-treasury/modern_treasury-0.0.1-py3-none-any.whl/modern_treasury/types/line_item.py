# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LineItem"]


class LineItem(BaseModel):
    accounting_category_id: Optional[Optional[str]]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[Optional[str]]
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """

    amount: Optional[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    created_at: Optional[str]

    description: Optional[Optional[str]]
    """A free-form description of the line item."""

    id: Optional[str]

    itemizable_id: Optional[str]
    """The ID of the payment order or expected payment."""

    itemizable_type: Optional[Literal["ExpectedPayment", "PaymentOrder"]]
    """One of `payment_orders` or `expected_payments`."""

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Optional[Dict[str, str]]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    object: Optional[str]

    updated_at: Optional[str]
