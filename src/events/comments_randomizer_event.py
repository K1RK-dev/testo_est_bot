from database.db_requests import DBRequests
from datetime import datetime
import time


class CommentsRandomizerEvent:
    def __init__(self):
        self.db_requests = DBRequests()

    async def check_event_registration(self, user_id):
        try:
            is_registered = await self.db_requests.check_event_registration(user_id)
            return is_registered
        except Exception as e:
            print(str(e))
            return False

    async def register_event_member(self, user_id):
        try:
            await self.db_requests.register_event_member(user_id, 15)
        except Exception as e:
            print('Не удалось зарегистрировать пользователя в конкурсе. Error : (' + str(e) + ')')

    async def is_user_can_do_attempt(self, user_id, attempt_pause_mins=10):
        attempts_count = await self.db_requests.get_event_attempts_count(user_id)
        if not attempts_count['attempt_count'] is None:
            if int(attempts_count['attempt_count']) > 0:
                current_timestamp = datetime.now().timestamp()
                pause_timestamp = datetime.strptime(str(attempt_pause_mins), "%M").timestamp()
                last_attempt_timestamp = await self.db_requests.get_last_event_attempt_timestamp(user_id)

                if not last_attempt_timestamp['last_attempt_timestamp'] is None:
                    last_attempt_timestamp = datetime.strptime(str(last_attempt_timestamp['last_attempt_timestamp']), "%Y-%m-%d %H:%M:%S").timestamp()
                    if (current_timestamp - last_attempt_timestamp) >= pause_timestamp:
                        return True
        return False
