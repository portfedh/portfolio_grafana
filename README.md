# Investment Portfolio Visualizer

**ToDo: Create GIF example here.**

## What it does

The project creates a custom portfolio visualizer to help you analyze an investment portfolio.

Its main features are:

- Its open source.

- You can consolidate several bank account and track the consolidated portfolio.

- You can have several portfolios for different users.

- You can customize all of the dashboards.

- You can aggregate the data in a way that makes sense to you.

- Graphs are dynamic so you can analyze different time periods.

## How to Install

To use the portfolio visualizer you will need to previously install:

- [Python 3](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)

Using a virtual environment is recommended.
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

This is the image that has the demo user portfolio data visualized.

Its meant as an example and as a starting point for you to create your own customized dashboards.

![ToDo: Image of dashboard here](https://google.com)

## How to Use

To give the script a try, run the setup, select 'user1' and look at the output visualization.

If you decide you would like to use it for your portfolio, follow the instructions to customize the scripts for your.

### First time setup

- Make sure you have installed python & docker with all their dependencies.

- Make sure docker is up and running.

- Delete the file named:

```bash
rm 0_check_computer.sh
```

- Open the following file in your code editor:

```bash
# File to edit:
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

Thats it. You are ready to run the script for the first time.

### First time run

To run the program, execute the following bash script from your terminal:

```bash
# Starting the application
./01_portfolio_run.sh
```

- The script will ask how long you want to wait for MySQL Volume to set up.
Since this is the first time, select 40 seconds. On future runs you can select 1 second.

- When asked to chose a username select:

> user1

All scripts will start to execute.

- After all files have finished running, open you browser and go to [localhost:3000/](localhost:3000/)

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

### Adding your own files

To Do
#### Adding your input data

To Do

#### Encrypting your data

To Do

#### Configuring your portfolio scripts

To Do
### Customizing your grafana dashboard

To Do
## Use cases

To Do

## Contributing

To Do