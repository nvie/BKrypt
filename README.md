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

    >>> for i in range(0, 3):
    ...     p = Password.create('my secret password')
    ...     print(p)
    ...
    $2a$04$eddbs9i/v3xuVei.d0CPaOL7g3spzxJ/z0.naES1jjI77kFpinvfK
    $2a$04$E0hc67qJ8A1xOf4IdkKpteM5o1A7sQE7PvgaC1j1HgDAXkJUagQhS
    $2a$04$AYPR70TyYUXN5A9Cl6wYn.ScDSGQYPwYgi.ZkBPvkI8SOQSrF.d.u


### Generating stronger hashes

To generate stronger hashes, use increased strength (12 is default).  Both
generating and checking then takes significantly longer, by the very design of
the BCrypt algorithm, that is.

    >>> p = Password.create('my secret password', strength=15)
    $2a$15$3LyRjuAzvX7i8uvFbwOk4ueZ0YrS4jAj3RiRsqBX5XTJlIRJrqDZ2


## Installation

The usual stuff.

    $ pip install bkrypt

