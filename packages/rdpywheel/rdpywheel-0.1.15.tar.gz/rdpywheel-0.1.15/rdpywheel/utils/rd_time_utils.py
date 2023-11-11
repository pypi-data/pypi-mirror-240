from datetime import datetime


class RdTimeUtils:

    @staticmethod
    def get_current_time_seconds(self):
        return int(datetime.now().timestamp())