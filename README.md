# Investment Portfolio Visualizer

**ToDo: Create GIF example here.**

## What it does

The project creates a custom portfolio visualizer to help you analyze an investment portfolio.

Its main features are:

- Its open source.

- You can consolidate several bank account and track the consolidated portfolio.

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

To give the script a try, run the first time setup and look at the output visualization.

If you decide you would like to use it with your portfolio, follow the instructions of the rest of the sections.

### First time setup

- Make sure you have installed python & docker with all their dependencies.

- Execute the bash script from your terminal:

```bash
# Starting the application
./01_portfolio_run.sh
```

- When asked to chose a username select:

> user1

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

## Use cases

To Do

## Contributing
