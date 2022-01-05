import random
import string


def get_random_str(num):
    data = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return "".join([random.choice(data) for i in range(num)])


if __name__ == "__main__":
    print(get_random_str(10))
    print(get_random_str(20))
    print(get_random_str(30))
