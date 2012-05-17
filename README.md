# Setup
## Clone & cd into git repo

## Set up virtualenv & activate virtualenv
1. `curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py`
2. `python virtualenv.py groovy_env`
3. `. groovy_env/bin/activate`

## Install requirements
1. `pip install -e .`

# Testing
Run google chrome with remote debugging enabled. Note that this won't work if you already have chrome running!
`google-chrome --remote-debugging-port=4242`

# Running
If you're in the virtualenv, then:
`groovy/groovy.py`
otherwise:
`/path/to/groovy_env/bin/python /path/to/groovy.py`
