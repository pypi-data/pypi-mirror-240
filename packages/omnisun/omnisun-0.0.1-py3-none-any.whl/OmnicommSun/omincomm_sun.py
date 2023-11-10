import json
import requests as r


class SUN:
    URL = "https://config.omnicomm.ru/api"

    def __init__(self):
        self.start()

    def start(self):
        params = f'{self.URL}?action=locale&lang=ru'
        r.post(params)

    def get_task_queue(self):
        data = {
            "action": "getTaskQueue"
        }
        response = r.post(url=self.URL, data=data)

    def get_registrator(self, terminal_id: int, password: str):
        data = {
            "action": "getRegistrator",
            "data": json.dumps({
                "ID": terminal_id,
                "password": password,
                "registratorid": []
            })
        }
        response = r.post(url=self.URL, params=data)
        print(response.json())


if __name__ == '__main__':
    sun = SUN()
    # sun.get_task_queue()
    sun.get_registrator(254002001, '56987')

