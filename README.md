## BKrypt

Wrapper around [python-bcrypt](http://www.mindrot.org/projects/py-bcrypt) to
provide simple access to the future-proof BCrypt algorithms, for password
hashing.

### Generating a password hash

    >>> from bkrypt import Password
    >>> p = Password.create('my secret password')
    >>> print(p)
    $2a$04$I2KuvSCq4pF/xJeSieLcsO.xs204lqy1IuakktiI/PZxv7OwIAoWS

To get the hash string out, use `p.hash` or `str(p)`.


### Checking password correctness

    >>> from bkrypt import Password
    >>> p = Password('$2a$04$I2KuvSCq4pF/xJeSieLcsO.xs204lqy1IuakktiI/PZxv7OwIAoWS')
    >>> p == 'foo'
    False
    >>> p == 'my secret password'
    True


## About the hashes

### Generating stronger hashes

Note that generating a password hash for the same password will result in
different hashes every time:

    >>> p = Password.create('my secret password')
    >>> print(p)
    $2a$04$MPRwrINhaCvXVlQsB/DzLu9ZxhUY/xfTsxERDT8Q.sWl9LiC72pS2


### Generating stronger hashes

To generate stronger hashes, use increased strength (12 is default).  Both
generating and checking then takes significantly longer, by the very design of
the BCrypt algorithm, that is.

    >>> p = Password.create('my secret password', strength=15)
    $2a$15$3LyRjuAzvX7i8uvFbwOk4ueZ0YrS4jAj3RiRsqBX5XTJlIRJrqDZ2


## Installation

The usual stuff.

    $ pip install bkrypt

