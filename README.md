# Investment Portfolio Visualizer

**ToDo: Create GIF example here.**

## What it does

The project is a custom portfolio visualizer to display information about investments in the stock market.

It's similar to dashboards in online banking portals, but with a few key differences:

- Its open source.

- Graphs are dynamic (not static).

- You can consolidate more than one bank account.

- You can customize all of the dashboards.

- You can aggregate the data in a way that makes sense to you.

## How to Install

You must install the python modules in the **requirements.txt** file.

You will also need to install docker in your computer.

Using a vrtual enviroment is recommended.

## How to Use

Setup will take a little time.

**ToDo: Create setup instructions file and link here.**

Updating after setup is a breeze. It should not take more than 5 minutes per month.

To use the scripts, you will need to have a basic understanding of the following:

- Docker
- MySQL
- Grafana
- Python (Padas)

To run the scripts, simply execute the script from your terminal:

```bash
# Starting the application
./01_portfolio_run.sh

# Closing th e application
./02_portfolio_close.sh
```

Currently, both of the files above use a virtual enviroment. You will need to change that bit of code to reflect where your python files are located.
For example:

```bash
# Before (01_portfolio_run.sh  Line 17)
./venv/bin/python3 set_mysql_setup.py

# After (same line)

./python3 set_mysql_setup.py
```

When run, the scripts will read your input files, process the data, download the stock prices, save them to MySQL and create the Docker Containers with all the graphs.

To access graphana go to:

localhost:3000/

## Use cases

To Do

## Contributing

To Do