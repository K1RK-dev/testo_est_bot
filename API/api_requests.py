from vkbottle.api import API
from config import TOKEN, APP_TOKEN


class APIRequests:
    def __init__(self):
        self.api_group = API(TOKEN)
        self.api_service = API(APP_TOKEN)

    async def get_wall_post_comments(self, owner_id, post_id):
        response = await self.api_service.request("wall.getComments", {'owner_id': owner_id, 'post_id': post_id})
        return response

    async def reply_to_comment(self, owner_id, post_id, message, comment_to_reply_id):
        response = await self.api_group.request("wall.createComment", {'owner_id': owner_id,
                                                                       'post_id': post_id,
                                                                       'message': message,
                                                                       'reply_to_comment': comment_to_reply_id})
        return response
