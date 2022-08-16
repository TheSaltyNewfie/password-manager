import requests


def create(username, password_hash):
    response = requests.get(
        f"https://keyin.thesaltynewfie.ca/create?username={username}&password_hash={password_hash}"
    )
    return respone.json()


def login(username, password_hash):
    response = requests.get(
        f"https://keyin.thesaltynewfie.ca/auth?username={username}&password_hash={password_hash}"
    )
    return response.json()


def delete_user(username, password_hash):
    response = requests.get(
        f"http://127.0.0.1:18080/delete?username={username}&password_hash={password_hash}"
    )
    return response.json()


def new_password(username, password_hash, token, account_username, account_password):
    response = requests.get(
        f"http://127.0.0.1:18080/new-password?username={username}&password_hash={password_hash}&token={token}&pass_user={account_username}&pass_pass={account_password}"
    )
    return response.json()


def get_passwords(username, password_hash, token):
    response = requests.get(
        f"http://127.0.0.1:18080/get-passwords?username={username}&password_hash={password_hash}&token={token}"
    )
    return response.json()


def delete_password(username, password_hash, token, account_username, account_password):
    response = requests.get(
        f"http://127.0.0.1:18080/new-password?username={username}&password_hash={password_hash}&token={token}&pass_user={account_username}&pass_pass={account_password}"
    )
    return response.json()
