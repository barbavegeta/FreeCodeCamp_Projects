#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=salon -t --no-align -c"

display_services() {
  echo -e "\nWelcome to My Salon, how can I help you?"
  SERVICES=$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")
  echo "$SERVICES" | while IFS="|" read SERVICE_ID NAME; do
    echo "$SERVICE_ID) $NAME"
  done
}

display_services

while true; do
  echo -e "\nPlease enter the service number:"
  read SERVICE_ID_SELECTED
  SERVICE_NAME=$($PSQL "SELECT name FROM services WHERE service_id = $SERVICE_ID_SELECTED")

  if [[ -z $SERVICE_NAME ]]; then
    echo -e "\nThat service doesn't exist. Please choose again."
    display_services
  else
    break
  fi
done

echo -e "\nEnter your phone number:"
read CUSTOMER_PHONE

CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")

if [[ -z $CUSTOMER_ID ]]; then
  echo -e "\nWhat's your name?"
  read CUSTOMER_NAME
  INSERT_CUSTOMER_RESULT=$($PSQL "INSERT INTO customers (name, phone) VALUES ('$CUSTOMER_NAME', '$CUSTOMER_PHONE')")
  CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone = '$CUSTOMER_PHONE'")
else
  CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE customer_id = $CUSTOMER_ID")
fi

echo -e "\nWhat time would you like the $SERVICE_NAME appointment?"
read SERVICE_TIME

INSERT_APPOINTMENT_RESULT=$($PSQL "INSERT INTO appointments (customer_id, service_id, time) VALUES ($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")

if [[ $INSERT_APPOINTMENT_RESULT == "INSERT 0 1" ]]; then
  echo -e "\nI have put you down for a $SERVICE_NAME at $SERVICE_TIME, $CUSTOMER_NAME."
else
  echo -e "\nThere was an error scheduling your appointment. Please try again."
fi
