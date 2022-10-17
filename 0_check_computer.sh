#!/bin/bash
# Bash script to:
#   - Check if im working from my Mac or Linux computer.
#   - Select the appropriate virtual enviroment. 

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