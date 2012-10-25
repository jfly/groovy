#!/usr/bin/env python

from distutils.core import setup

setup(name='groovy',
        version='0.1',
        author='Jeremy Fleischman',
        author_email='jeremyfleischman@gmail.com',
        url='https://github.com/jfly/groovy',
        packages=['groovy'],

        install_requires=["webkit_remote_debugger"],
        dependency_links=["https://github.com/jfly/webkit_remote_debugger/tarball/master#egg=webkit-remote-debugger-1.0"]
     )
