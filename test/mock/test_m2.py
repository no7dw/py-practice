from mock import MagicMock
mock = Mock(side=KeyError('foo'))
mock()
