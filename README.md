#hireme

Solution to the ZON backend developer code ninja program.

##automatic install

For new debian based machines, this script will do the trick.    
No warranties! When in doubt, please follow the manual install method.

    \curl -sL cutoffthetop.github.io/hireme | bash

##manual install

Make sure the following dependencies are installed on your system.

    apache2 mod_wsgi git python

Then clone the repository and change to the directory.

    git clone https://github.com/cutoffthetop/hireme.git
    cd hireme

Now run the bootstrap and buildout process.

    python buildout.py
    bin/buildout

To run the server locally, use this command.

    bin/hireme
