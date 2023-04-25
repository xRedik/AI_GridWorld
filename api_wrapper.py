import requests


class APIWrapper:
    def __init__(self):
        self.gw_url = "https://www.notexponential.com/aip2pgaming/api/rl/gw.php"
        self.score_url = "https://www.notexponential.com/aip2pgaming/api/rl/score.php"

        self.headers = {
            'User-Agent': 'Sikkim',
            'userId': '1175',
            'x-api-key': '84c9055aacf9160871ff',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.teamId = 1378

    def get_runs(self, count):
        payload = {}

        queryParam = {'type': 'runs', 'teamId': self.teamId, 'count': count}

        response = requests.request(
            "GET", self.score_url, headers=self.headers, data=payload, params=queryParam)
        # print(response.text)
        parsed_res = eval(response.text)
        if parsed_res['code'] == 'OK':
            return parsed_res['runs']
        else:
            return parsed_res

    def get_location(self):
        payload = {}

        queryParam = {'type': 'location', 'teamId': self.teamId}

        response = requests.request(
            "GET", self.gw_url, headers=self.headers, data=payload, params=queryParam)
        # print(response.text)
        parsed_res = eval(response.text)
        if parsed_res['code'] == 'OK':
            return parsed_res['world'], parsed_res['state']
        else:
            return parsed_res

    def enter_world(self, worldID):
        payload = {
            'type': 'enter',
            'teamId': self.teamId,
            'worldId': worldID,
        }

        response = requests.request(
            "POST", self.gw_url, headers=self.headers, data=payload)

        # print(response.text)
        parsed_res = eval(response.text)
        if parsed_res['code'] == 'OK':
            return parsed_res['worldId']
        else:
            return parsed_res

    def make_move(self, worldID, move):
        payload = {
            'type': 'move',
            'teamId': self.teamId,
            'worldId': worldID,
            'move': move
        }

        response = requests.request(
            "POST", self.gw_url, headers=self.headers, data=payload)

        # print(response.text)
        parsed_res = eval(response.text)
        if parsed_res['code'] == 'OK':
            return parsed_res['reward'], parsed_res['worldId'], parsed_res['newState']
        else:
            return parsed_res

    def get_score(self):
        payload = {}

        queryParam = {'type': 'score', 'teamId': self.teamId}

        response = requests.request(
            "GET", self.score_url, headers=self.headers, data=payload, params=queryParam)
        # print(response.text)
        parsed_res = eval(response.text)
        if parsed_res['code'] == 'OK':
            return parsed_res['score']
        else:
            return parsed_res

    # !DONT RESET
    # def reset_team(self):
    #     payload = {}

    #     queryParam = {'teamId': self.teamId, 'otp': '5712768807'}

    #     response = requests.request(
    #         "GET", 'https://www.notexponential.com/aip2pgaming/api/rl/reset.php', headers=self.headers, data=payload, params=queryParam)
    #     print(response.text)


api = APIWrapper()
# runs = api.get_runs(1)
# print(runs)

# world, res = api.get_location()
# print(world)

# worldId = api.enter_world(0)

# api.make_move(worldId, 0)
score = api.get_score()
print(score)
