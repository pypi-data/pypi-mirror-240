from typing import TYPE_CHECKING, BinaryIO, Callable, List, Optional, Union
import swibots
from io import BytesIO
from swibots.base import SwitchObject
from swibots.api.common import User, Media, EmbeddedMedia
from swibots.utils.types import JSONDict
from swibots.types import MediaType
from .inline_markup import InlineMarkup, InlineMarkupRemove


class Organization(
    SwitchObject,
):
    def __init__(self, app: "swibots.App" = None,
                 community_ids: List[str] = None,
                 thumbnail: str = None,
                 created_at: str = None,
                 created_by: int = None,
                 description: str = None,
                 email: str = None,
                 followers: int = 0,
                 id: str = None,
                 instagram: str = None,
                 twitter: str = None,
                 profile_pic: str = None,
                 name: str = None,
                 telegram: str = None,
                 ):
            super().__init__(app)
            self.community_ids = community_ids
            self.thumbnail = thumbnail
            self.created_at = created_at