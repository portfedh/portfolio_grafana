#!/bin/bash

# Bash script to run Docker file for slected user

# Cleanup of previous files
###########################
echo
echo -e "Cleaning outputs directory:"
rm -v outputs/*
echo


# Select computer
#################
read -p 'Enter computer used ( linux / mac ): ' COMPUTER

if [[ "${COMPUTER}" == "linux" ]]
then
  echo "You are running the script from Linux."
  VENV="./venv_linux/bin/python3"
  #echo "${VENV}"
  echo
elif [[ "${COMPUTER}" == "mac" ]]
then
  echo "You are running the script from a Mac."
  VENV="./venv/bin/python3"
  #echo "${VENV}"
  echo
else
  echo "Error in computer name."
  echo
  exit 1
fi


# Select user
#############
echo "Run Docker for which user?"
echo
echo "Current available users are:"
echo "- clg"
echo "- pcl"
echo

read -p 'Enter user: ' USER_NAME

if [[ "${USER_NAME}" == "clg" ]]
then
  echo "You are CLG."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:clg_grafana"
  DOCKER_COMPOSE="./usr/clg/docker-compose.yml"
  FILE_PATH="usr/clg/"
  #echo "${DOCKER_IMAGE}"
  echo
elif [[ "${USER_NAME}" == "pcl" ]]
then
  echo "You are PCL."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:pcl_grafana"
  DOCKER_COMPOSE="./usr/pcl/docker-compose.yml"
  FILE_PATH="usr/pcl/"
  #echo "${DOCKER_IMAGE}"
  echo
else
  echo "Error in username"
  exit 1
  echo
fi


# Run Docker
############
echo "Setting Up Docker files:"
# Pull latest image
docker pull "${DOCKER_IMAGE}"
# Run docker compose
docker-compose -f "${DOCKER_COMPOSE}" up -d
sleep 5
echo
echo "Docker setup."


# # Temp file: ERASE SOON
# ########################
# #VENV="./venv/bin/python3"
# VENV="./venv_linux/bin/python3"
# FILE_PATH="usr/clg/"
# #FILE_PATH="usr/pcl/"
# #########################

# Running python files
######################
echo "Executing Portfolio Scripts:"

echo "    - Executing set_mysql_setup."
${VENV} ${FILE_PATH}set_mysql_setup.py

echo "    - Executing get_daily_balance."
${VENV} ${FILE_PATH}get_daily_balance.py

echo "    - Executing get_daily_contributions."
${VENV} ${FILE_PATH}get_daily_contributions.py

echo "    - Executing get_irr."
${VENV} ${FILE_PATH}get_irr.py

echo "    - Executing get_returns."
${VENV} ${FILE_PATH}get_returns.py

echo "    - Executing get_daily_shares."
${VENV} ${FILE_PATH}get_daily_shares.py

echo "    - Executing get_daily_prices."
${VENV} ${FILE_PATH}get_daily_prices.py

echo "    - Executing get_daily_subtotals_single_account."
${VENV} ${FILE_PATH}get_daily_subtotals_single_account.py

echo "    - Executing get_daily_subtotals_all_accounts."
${VENV} ${FILE_PATH}get_daily_subtotals_all_accounts.py