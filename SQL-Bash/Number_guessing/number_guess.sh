#!/bin/bash
# Connect to the database
PSQL="psql --username=freecodecamp --dbname=number_guess --tuples-only -c"

# Prompt for username
echo "Enter your username:"
read USERNAME

USER_INFO=$($PSQL "SELECT username, games_played, best_game FROM users WHERE username='$USERNAME';")

if [[ -z $USER_INFO ]]; then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  INSERT_USER=$($PSQL "INSERT INTO users(username) VALUES('$USERNAME');")
else
  echo "$USER_INFO" | while read USERNAME BAR GAMES_PLAYED BAR BEST_GAME; do
    echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
  done
fi

SECRET_NUMBER=$((RANDOM % 1000 + 1))
NUMBER_OF_GUESSES=0
GUESSED=false

echo "Guess the secret number between 1 and 1000:"

while [[ $GUESSED == false ]]; do
  read GUESS

  if [[ ! $GUESS =~ ^[0-9]+$ ]]; then
    echo "That is not an integer, guess again:"
    continue
  fi

  ((NUMBER_OF_GUESSES++))

  if [[ $GUESS -eq $SECRET_NUMBER ]]; then
    echo "You guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"
    GUESSED=true

    USER_INFO=$($PSQL "SELECT games_played, best_game FROM users WHERE username='$USERNAME';")
    echo "$USER_INFO" | while read GAMES_PLAYED BAR BEST_GAME; do
      NEW_GAMES_PLAYED=$((GAMES_PLAYED + 1))
      if [[ -z $BEST_GAME || $NUMBER_OF_GUESSES -lt $BEST_GAME ]]; then
        UPDATE_USER=$($PSQL "UPDATE users SET games_played=$NEW_GAMES_PLAYED, best_game=$NUMBER_OF_GUESSES WHERE username='$USERNAME';")
      else
        UPDATE_USER=$($PSQL "UPDATE users SET games_played=$NEW_GAMES_PLAYED WHERE username='$USERNAME';")
      fi
    done
  elif [[ $GUESS -lt $SECRET_NUMBER ]]; then
    echo "It's higher than that, guess again:"
  else
    echo "It's lower than that, guess again:"
  fi
done