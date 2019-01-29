import abc
class Order(object):
    def __init__(self):
        self.__status = Order.State.INITIAL

    class State(object):
        INITIAL = 1  # Initial state.
        SUBMITTED = 2  # Order has been submitted.
        ACCEPTED = 3  # Order has been acknowledged by the broker.
        CANCELED = 4  # Order has been canceled.
        PARTIALLY_FILLED = 5  # Order has been partially filled.
        FILLED = 6  # Order has been completely filled.

        def __init__(cls, init_ste):
            if(__valid(init_ste)):
                cls.__state = init_ste

        @staticmethod
        def __valid(state):
            return state > 0 and state < 6

        @classmethod
        def toString(cls, state):
            if state == cls.INITIAL:
                return "INITIAL"
            elif state == cls.SUBMITTED:
                return "SUBMITTED"
            elif state == cls.ACCEPTED:
                return "ACCEPTED"
            elif state == cls.CANCELED:
                return "CANCELED"
            elif state == cls.PARTIALLY_FILLED:
                return "PARTIALLY_FILLED"
            elif state == cls.FILLED:
                return "FILLED"
            else:
                return "INVALID"


print(Order.State.CANCELED)
s = Order.State(1)
print(s.toString('ACCEPTED'))
print(s.toString(2))
# staticmethod
print('isvalid',Order.State.__valid(2))
# classmethod
print('str',Order.State.toString(2))

