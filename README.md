# Twitico #

## Description ##

Twitico is a simple, minimalist Python twitter client. It supports notifications via PyNotify.

## Installation ##

Just copy the executable to a location that will be seen by the $PATH variable. Examples:

### ZSH ###

    mkdir -p ${HOME}/.local/bin
    cd ${HOME}/.local/bin
    wget https://raw.github.com/kmwhite/twitico/master/twitico
    cat >>${HOME}/.zshrc<<EOF
    if [ -d ${HOME}/.local/bin ]; then
      export PATH=${HOME}/.local/bin:$PATH
    fi
    EOF

## Usage ##

After installation, simply execute the command:

    % twitico

* NOTE: For the first run of the command, you'll want to execute it from a terminal

## Contributing ##

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it
* Fork the project
* Start a feature/bugfix branch
* Commit and push until you are happy with your contribution
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the Fabfile, version, or history. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so I can cherry-pick around it.

## License ##
Twitico is covered by the 3-clause BSD license. For more information, please see either http://www.opensource.org/licenses/BSD-3-Clause or the 'twitico' executable's source
