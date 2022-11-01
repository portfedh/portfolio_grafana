#!/bin/bash
# Bash script to:
#   - Provide available users
# Imported and used in 1_portfolio_run.sh

AVAILABLE_USERS=("name1" "name2")

# Check selected user
#####################
function check_users {
if [[ "${USER_NAME}" == "user1" ]]
then
  echo "You are user1."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:user1_grafana"
  DOCKER_COMPOSE="./usr/user1/docker-compose.yml"
  FILE_PATH="usr/user1/"
  echo
elif [[ "${USER_NAME}" == "name1" ]]
then
  echo "You are name1."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:name1_grafana"
  DOCKER_COMPOSE="./usr/name1/docker-compose.yml"
  FILE_PATH="usr/name1/"
  echo
elif [[ "${USER_NAME}" == "name2" ]]
then
  echo "You are name2."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:name2_grafana"
  DOCKER_COMPOSE="./usr/name2/docker-compose.yml"
  FILE_PATH="usr/name2/"
  echo
else
  echo "Error in username"
  exit 1
  echo
fi
}