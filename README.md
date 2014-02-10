#hireme

[![Build Status](https://travis-ci.org/cutoffthetop/hireme.png?branch=master)](https://travis-ci.org/cutoffthetop/hireme)

Solution to the zon-backend developer code ninja program.

##automatic install

For new debian based machines, this script will do the install automatically.    
Make sure you understand what it is doing, before executing as root.

    wget -q cutoffthetop.github.io/hireme && bash hireme

##manual install

Make sure the following dependencies are installed on your system.

    apache2 mod_wsgi git python python-dev

Then clone the repository and change to the directory.

    git clone https://github.com/cutoffthetop/hireme.git /usr/local/
    cd /usr/local/hireme

Now run the bootstrap and buildout process.

    python buildout.py
    bin/buildout

##testing

To run the server locally, use this command.

    bin/hireme

To run the test suite with verbose output, use this command.

    bin/tests -v

##deployment

Copy the virtualhost file, enable it and activate mod_wsgi.

    cp /usr/local/hireme/hireme /etc/apache2/sites-available
    a2dissite default 
    a2ensite hireme
    service apache2 restart
