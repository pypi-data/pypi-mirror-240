import logging
from typing import TYPE_CHECKING, List, Optional

from swibots.api.chat.models import (
    Message,
)

if TYPE_CHECKING:
    from swibots.api.chat import ChatClient

log = logging.getLogger(__name__)

BASE_PATH = "/v1/organization"


class OrganizationController:
    """Organization controller"""

    def __init__(self, client: "ChatClient"):
        self.client = client

