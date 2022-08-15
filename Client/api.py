import requests


def create(username, password_hash):
    response = requests.get("https")


def login(username, password_hash):
    pass


def delete_user(username, password_hash):
    response = requests.get(f"http://127.0.0.1:18080/delete?username={username}&password_hash={password_hash}").content
    print(f"SERVER -> {response}") # WIll be properly done later


def new_password(username, password_hash, token, account_username, account_password):
    pass


def get_passwords(username, password_hash, token):
    pass


def delete_password(username, password_hash, token, account_username, account_password):
    pass
