#!/bin/bash

# Bash script to run Docker file for slected user

# # Cleanup of any previous files
# ##############################################################################
# echo
# echo -e "Cleaning outputs directory:"
# rm -v outputs/*
# echo


# # Selcect computer
# ##############################################################################
# read -p 'Enter computer used ( linux / mac ): ' COMPUTER

# if [[ "${COMPUTER}" == "linux" ]]
# then
#   echo "You are Linux."
#   VENV="./venv_linux/bin/python3"
#   #echo "${VENV}"
#   echo
# elif [[ "${COMPUTER}" == "mac" ]]
# then
#   echo "You are Mac."
#   VENV="./venv/bin/python3"
#   #echo "${VENV}"
#   echo
# else
#   echo "Error in computer name."
#   echo
#   exit 1
# fi


# # Select user
# ##############################################################################
# echo "Run Docker for which user?"
# echo
# echo "Current available users are:"
# echo "- clg"
# echo "- pcl"
# echo

# read -p 'Enter user: ' USER_NAME

# if [[ "${USER_NAME}" == "clg" ]]
# then
#   echo "You are CLG."
#   DOCKER_IMAGE="portfedh/portfolio_dashboard:clg_grafana"
#   DOCKER_COMPOSE="./usr/clg/docker-compose.yml"
#   echo "${DOCKER_IMAGE}"
#   echo
# elif [[ "${USER_NAME}" == "pcl" ]]
# then
#   echo "You are PCL."
#   DOCKER_IMAGE="portfedh/portfolio_dashboard:pcl_grafana"
#   OCKER_COMPOSE="./usr/pcl/docker-compose.yml"
#   echo "${DOCKER_IMAGE}"
#   echo
# else
#   echo "Error in username"
#   exit 1
#   echo
# fi


# # Run Docker
# ##############################################################################
# echo "Setting Up Docker files:"
# # Pull latest image
# docker pull "${DOCKER_IMAGE}"
# # Run docker compose
# docker-compose -f "${DOCKER_COMPOSE}" up -d
# sleep 5
# echo
# echo "Docker setup."


# Temp file: ERASE SOON
########################
VENV="./venv/bin/python3"
#########################


# Running indivdual files
##############################################################################
echo "Executing Portfolio Scripts:"

echo "    - Executing set_mysql_setup."
"${VENV}" usr/clg/set_mysql_setup.py

echo "    - Executing get_daily_balance."
"${VENV}" usr/clg/get_daily_balance.py