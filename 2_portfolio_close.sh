#!/bin/bash
# Bash script to:
#   - Delete MySQL database, 
#   - Delete all csv files
#   - Encrypt user files
#   - Close down docker.

# Check computer
################
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
  VENV="./venv_mac/bin/python3"
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
echo "- user1"
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
elif [[ "${USER_NAME}" == "user1" ]]
then
  echo "You are user1."
  echo
  DOCKER_COMPOSE="./usr/user1/docker-compose.yml"
  FILE_PATH="usr/user1/"
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

# Encrypt input files
######################
echo "Encrypting user input files:"
${VENV} file_encryption.py ${USER_NAME} encrypt
echo

# Remove Output Files
#####################
echo "Removing all CSV files:"
rm -v outputs/*
echo