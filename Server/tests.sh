#!/bin/bash

echo "Start server before using this"
printf "Run ./build/main&\n\n"

printf "Should work, creating user."
curl 'localhost:18080/create?username=joe&password_hash=blargblarg'

printf "\n\nShould error, duplicate key."
curl 'localhost:18080/create?username=joe&password_hash=blargblarg'

printf "\n\nShould work, token"
curl 'localhost:18080/auth?username=joe&password_hash=blargblarg'

printf "\n\nShould fail, user doesn't exist (wrong username)"
curl 'localhost:18080/auth?username=joey&password_hash=blargblarg'

printf "\n\nShould fail, user doesn't exist (wrong password)"
curl 'localhost:18080/auth?username=joe&password_hash=blargblar'
