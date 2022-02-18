import requests

page_size_12 = "?pagesize=12"
page_size_all = "?"

team_search_url = "https://cricheroes.in/api/v1/other/global-search/"
team_members_url = "https://cricheroes.in/api/v1/team/get-team-member/"
team_matches_url = "https://cricheroes.in/api/v1/team/get-team-match/"

player_info_url = "https://cricheroes.in/api/v1/player/get-player-profile-info/"
player_matches_url = "https://cricheroes.in/api/v1/player/get-player-match/"  # + player_id + page_size_all
player_stats_url = "https://cricheroes.in/api/v1/player/get-player-statistic/"

match_scorecard_url = "https://cricheroes.in/api/v1/scorecard/v2/get-scorecard/"
match_commentary_url = "https://cricheroes.in/api/v1/scorecard/v2/get-commentary/"  # + match_id + page_size_all

request_headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate",
    "accept-language": "en-US,en;q=0.8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "api-key": "cr!CkH3r0s",
    "device-type": "Chrome: 98.0.4758.102",
    "udid": "50100646453736980475810253736",
}


def get_player_info(player_id):
    response = requests.get(
        url=player_info_url + str(player_id), headers=request_headers
    ).json()
    print(response)
    return


def query_teams(team_name):
    team_name = team_name.replace(" ", "%20")
    response = requests.get(
        url=team_search_url + team_name + page_size_12, headers=request_headers
    ).json()
    print(response["data"]["teams"][0])
    return response["data"]["teams"][0]


def get_team_players(team_id):
    response = requests.get(
        url=team_members_url + str(team_id) + page_size_all, headers=request_headers
    ).json()
    return response["data"]["members"]


def get_player_matches(player_id):
    response = requests.get(
        url=player_matches_url + str(player_id) + page_size_all, headers=request_headers
    ).json()
    print(response)
    return


def get_team_matches(team_id):
    response = requests.get(
        url=team_members_url + str(team_id) + page_size_all, headers=request_headers
    ).json()
    return response["data"]


def main():
    teams = query_teams("Basavanagudi Challengers")
    players = get_team_players(teams["team_id"])
    matches = get_team_matches(teams["team_id"])
    get_player_info(players[0]["player_id"])
    get_player_matches(players[0]["player_id"])


if __name__ == "__main__":
    main()
