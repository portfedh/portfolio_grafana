#!/bin/bash

# Script to delete MySQL database, 
# all csv files and close down docker.

# Select computer
#################
UNAME_STR=$(uname)
if [[ ${UNAME_STR} == 'Linux' ]]; then
   PLATFORM='linux'
   echo 'Linux'
elif [[ ${UNAME_STR} == 'Darwin' ]]; then
   PLATFORM='darwin'
   echo 'Mac'
else
  echo "Error in computer name."
  echo
  exit 1
fi

if [[ "${PLATFORM}" == "linux" ]]
then
  echo "You are running the script from Linux."
  VENV="./venv_linux/bin/python3"
  echo "${VENV}"
  echo
elif [[ "${PLATFORM}" == "darwin" ]]
then
  echo "You are running the script from a Mac."
  VENV="./venv/bin/python3"
  echo "${VENV}"
  echo
else
  echo "Error in computer name."
  echo
  exit 1
fi


# Select user
#############
echo "Close Docker for which user?"
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
  DOCKER_COMPOSE="./usr/clg/docker-compose.yml"
  FILE_PATH="usr/clg/"
  #echo "${DOCKER_IMAGE}"
  echo
elif [[ "${USER_NAME}" == "pcl" ]]
then
  echo "You are PCL."
  echo
  DOCKER_COMPOSE="./usr/pcl/docker-compose.yml"
  FILE_PATH="usr/pcl/"
  #echo "${DOCKER_IMAGE}"
  echo
else
  echo "Error in username"
  exit 1
  echo
fi


# Close MySQL
#############
echo "Removing MySQL Database:"
${VENV} ${FILE_PATH}set_mysql_close.py
echo


# Close Docker
##############
echo "Removing Docker files:"
docker-compose -f "${DOCKER_COMPOSE}" down
sleep 5
echo
echo "Docker closed."


# Remove Output Files
#####################
echo "Removing all CSV files:"
rm -v outputs/*

echo "All files removed succesfully."