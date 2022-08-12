#!/bin/bash

echo "Start server before using this"
printf "Run ./build/main&\n\n"

echo "Should work, creating user."
curl 'localhost:18080/create?username=joe&password_hash=blargblarg'

echo "Should error, duplicate key."
curl 'localhost:18080/create?username=joe&password_hash=blargblarg'

echo "Should work, token"
curl 'localhost:18080/auth?username=joe&password_hash=blargblarg'

echo "Should fail, user doesn't exist (wrong username)"
curl 'localhost:18080/auth?username=joey&password_hash=blargblarg'

echo "Should fail, user doesn't exist (wrong password)"
curl 'localhost:18080/auth?username=joe&password_hash=blargblar'
