import pytest

def square(i):
    return i*i

class TestClass:
    def setup_class(self):
        # print("setup_class")
        pass
        
    def teardown_class(self):
        # print("teardown_class")
        pass

    @pytest.mark.parametrize("data, result", [
        (6, 36),
        (3, 9),
    ])        
    def test_square(self, data, result):
        assert result == square(data)

            