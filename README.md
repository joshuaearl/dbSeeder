## What does it do

It submits a HTTP POST request using random user information. Randomly selects a first and last name from a top 1000 list, chooses an email address style and random phone number

## What was the inspiration for the project

To have a script that can create a diverse, random test data set for use in development projects

## Install

1) Install Python
2) Install dependencies, open terminal and run: pip install requests

## Setup

1) Open and edit 'dbSeeder.py'
2) Change the config at the top to include your target protocol, host and path to the form action
3) Change the 'headers' dictionary at the top. Change host, origin and referer
4) Change the 'data' dictionary at the bottom. This is where the name of the input fields from the form go 

## Run

Open Open terminal and run: python dbSeeder.py

## Note

It only submits the form once per execution currently. Easily modifiable to run in a loop or until certain parameter is met.

## LICENSE

GNU GPLv3