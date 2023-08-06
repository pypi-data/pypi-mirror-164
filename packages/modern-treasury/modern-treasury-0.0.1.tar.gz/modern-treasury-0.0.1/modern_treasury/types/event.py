# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    created_at: Optional[str]

    data: Optional[object]
    """The body of the event."""

    entity_id: Optional[str]
    """The ID of the entity for the event."""

    event_name: Optional[str]
    """The name of the event."""

    event_time: Optional[str]
    """The time of the event."""

    id: Optional[str]

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    resource: Optional[str]
    """The type of resource for the event."""

    updated_at: Optional[str]
