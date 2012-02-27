import bcrypt
from version import VERSION

__author__ = 'Vincent Driessen <me@nvie.com>'
__version__ = VERSION


class Password(object):
    @classmethod
    def create(self, passwd, strength=None):
        hash = bcrypt.hashpw(passwd, bcrypt.gensalt(strength))
        return Password(hash)

    def __init__(self, hash):
        self._hash = hash

    @property
    def hash(self):
        return self._hash

    def __str__(self):
        return self._hash

    def __eq__(self, passwd):
        if not isinstance(passwd, basestring):
            raise ValueError('Can only compare Password to strings.')
        given_hash = self.hash
        try:
            real_hash = bcrypt.hashpw(passwd, given_hash)
        except ValueError:
            # In case of an invalid (non-BCrypt) hash, return False
            return False
        return real_hash == given_hash


def hash_password(password, strengh=None):
    """Hashes the given password with the given BCrypt strenght and returns
    a string.
    """
    return Password.create(password, strengh).hash


if __name__ == '__main__':
    p = Password.create('foo', strength=14)
    print 'foo -> ', p
    hash = p.hash
    p2 = Password(hash)
    assert p2 != 'bar'
    assert p2 == 'foo'

    hash = unicode(Password.create('foo'))
    print hash

    print hash_password('foo')
    assert type(hash_password('foo')) == str
