# Investment Portfolio Visualizer

**ToDo: Create GIF example here.**

## What it does

The scripts create a custom portfolio visualizer to help you analyze an investment portfolio.

Its main features are:

- Its open source.

- You can consolidate several bank accounts into one portfolio.

- You can have several portfolios for different users.

- You can customize all of the dashboards.

- You can aggregate the data in a way that makes sense to you.

- Graphs are dynamic so you can analyze different time periods.

## How to Install

To use the portfolio visualizer you will need to previously install:

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)

I would recommend using  a virtual environment.
You can find documentation on setting one up [here.](https://docs.python.org/3/library/venv.html)

Once python 3 is installed, you will need to add the following libraries from [pip.](https://pypi.org/):

- [Pandas](https://pypi.org/project/pandas/)
- [Cryptography](https://pypi.org/project/cryptography/)
- [yfinance](https://pypi.org/project/yfinance/)
- [Pyxirr](https://pypi.org/project/pyxirr/)
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
- [mysql-connector](https://pypi.org/project/mysql-connector-python/)

All the docker images will automatically be downloaded from Docker Hub when you run the docker-compose.yml file.

The images that docker uses are:

- [MySQL](https://hub.docker.com/_/mysql)
- [Grafana](https://hub.docker.com/r/grafana/grafana)

The customized portfolio image that will be downloaded will be:

- [Custom Grafana Image](https://hub.docker.com/r/portfedh/portfolio_dashboard/tags)

This is the docker image that has the demo user portfolio.

Its meant as a starting point for you to create your own customized dashboards.

![ToDo: Image of dashboard here](https://google.com)

## How to Use

To give the script a try, follow the instructions below, select 'user1' and look at the output dashboard.

If you decide to use it for your portfolio, then follow the instructions to customize the scripts and add your data.

## First time setup

- Make sure you have installed python & docker with all their dependencies.

- Make sure docker is up and running.

- Delete the file named:

```bash
0_check_computer.sh
```

- Open the following file in your code editor:

```bash
01_portfolio_run.sh
```

- Uncomment the following lines in the 'check computer' section:

```bash
# VENV="<Path_to_your_python_file_here>"
# echo "${VENV}"
```

- Modify the 'VENV' variable and add the path to your python virtual environment or python executable.

- Now delete the line with the following text:

```bash
source 0_check_computer.sh
```

Thats it!

You are ready to run the script for the first time.

## First time run

Navigate to your project folder.

Make sure your virtual environment is activated.

To run all the python scripts, execute the following bash script from your terminal:

```bash
./01_portfolio_run.sh
```

The script will ask how long to wait for MySQL Volume to set up.

Since this is the first time, select 40 seconds. On future runs select 1 second.

When asked to chose a username select:

> user1

You will then be asked for a password to decrypt the files. Select:

> 1234abc

Wait for all scripts to execute.

Open you browser and go to [localhost:3000/](localhost:3000/)

- The default credentials for the demo user are:

> username: admin
>
> password: admin1

Browse through the Portfolio dashboard. You should see something like this:

![Image of the portfolio](localhost:3000/)

When you are ready to close everything up, head back to the terminal and execute the closing bash script:

```bash
# Closing the application
./02_portfolio_close.sh
```

## Adding your input data

Navigate to the 'inputs' directory.

Create a new directory.

Name your directory with the username for that portfolio.

You will need to add 3 files for every investment account you add.

- contributions_username_account.csv
- monthly_account_balance_username_account.csv
- trade_history_username_account.csv.

The contributions file will have the date and amount of every deposit or withdrawal you've made to that account.

The account balance, will have the date and balance for the account for every month.

The trade history file will have all the trading transactions you have made in that account (buy or sell, not dividends).

You can take a look at the input files for the demo user 'user1' as examples to fill in your own.

If you add more than one account, the dates in the monthly account balance file must match, even if the balance is $0.

## Adding your scripts

Once your input files are set up.

You must now modify the scripts to make the calculations and save the outputs to MySQL.

Navigate to the usr directory.

Create a new directory with your username

Copy all the files in usr/user1 into the new folder you just created.

Modify each file so it uses your input files and creates your desired output data.

All scripts have comments explaining what they do.

If you need more help, go to the /system_design_charts directory.

You will find a more detailed explanation of how everything works there.

## Encrypting your data

Right now all your input data is unencrypted at rest.

To encrypt you files:

- Go to the project root directory

- Execute the following command:

```bash
python3 file_encryption.py <username> encrypt
```

- Set a password to encrypt your files. 

After this, all the files under /input/<username>/' will be encrypted.

Make sure to save your encryption password, as there is no recovery option if you forget it.

## Customizing your grafana dashboard

Once you


## Adding your files to portfolio run

```bash
elif [[ "${USER_NAME}" == "user1" ]]
then
  echo "You are user1."
  echo
  DOCKER_IMAGE="portfedh/portfolio_dashboard:user1_grafana"
  DOCKER_COMPOSE="./usr/user1/docker-compose.yml"
  FILE_PATH="usr/user1/"
  #echo "${DOCKER_IMAGE}"
  echo
```

## Use cases

To Do

## Contributing

To Do