# Setup
## Clone git repo
1. `git clone git://github.com/jfly/groovy.git`
2. `cd groovy`

## Set up virtualenv & activate virtualenv
1. `curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py`
2. `python virtualenv.py groovy_env`
3. `. groovy_env/bin/activate`

## Install requirements
`pip install -r requirements.txt`

# Testing
Run google chrome with remote debugging enabled. Note that this won't work if you already have chrome running!
`google-chrome --remote-debugging-port=4242`

# Running
If you're in the virtualenv, then:
`./groovy.py`
otherwise:
`/path/to/groovy_env/bin/python /path/to/groovy.py`
