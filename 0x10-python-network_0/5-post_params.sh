#!/usr/bin/env bash
# send a POST request to the URL then display the body of the reponse
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
