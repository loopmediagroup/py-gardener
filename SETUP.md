## Test Requirements
* Python 3.6
* Ubuntu 16.04

## Python Config

### Create Virtual Env
Install `virtualenv`

    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv
    $ sudo apt-get install python-dev

##### CREATE ENVIRONMENT
    $ virtualenv -p /usr/bin/python3.6 env
    
    # activate the new environment
    $ source env/bin/activate
    
    # install requirements
    $ pip install -r requirements.txt
    
##### DEACTIVATE ENVIRONMENT
To deactivate environment for session, enter:

    $ deactivate

## Running the tests

Ensure your env is activated and run:

    $ python run_tests.py
