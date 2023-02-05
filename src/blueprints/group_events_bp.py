from vkbottle.bot import Blueprint, Message
from vkbottle import GroupEventType, GroupTypes
from database.db_requests import DBRequests
from src.helpers.message_generator import MessageGenerator

bp = Blueprint()
db_requests = DBRequests()
msg_generator = MessageGenerator()


@bp.on.raw_event(GroupEventType.PHOTO_COMMENT_NEW, dataclass=GroupTypes.PhotoCommentNew)
async def photo_comment_new(event: GroupTypes.PhotoCommentNew):
    pass
