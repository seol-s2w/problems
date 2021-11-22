import random
import time

from linked_list import LinkedList


class Woodogi:
    def __init__(self, data):
        self.data = data

    def __hash__(self) -> int:
        return hash(self.data) % 500

    def __eq__(self, o: object) -> bool:
        return self.data == o.data


class MySet:
    def __init__(self, bucket_size: int = 1024):
        self.bucket: list[LinkedList] = []
        self.bucket_size = bucket_size
        for i in range(bucket_size):
            self.bucket.append(LinkedList())

    def __contains__(self, key):
        index = hash(key) % self.bucket_size
        ll = self.bucket[index]

        node = ll.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next

        return False

    def add(self, data):
        index = hash(data) % self.bucket_size
        ll = self.bucket[index]

        node = ll.head
        while node is not None:
            if node.data == data:
                return
            node = node.next

        ll.push_back(data)


def init_data(count):
    data = list(range(count))
    random.shuffle(data)

    return data


def test_set(data, step):
    print(f"- set (len {len(data)}, step {step})\n")
    set_ = set()
    for i in range(0, len(data), step):
        start = time.time()
        for j in range(i, i + step):
            set_.add(data[j])
        end = time.time()
        print(f"add to set      ({i:>7} ~ {i+step-1:>7}): {end - start:0.3f} sec")
    print()

    data_to_find = random.sample(data, len(data) // 2)
    start = time.time()
    for d in data_to_find:
        if d in set_:
            pass
    end = time.time()
    print(f"find in set     (data count: {len(data)//2:>5}): {end - start:0.3f} sec")
    print()


def test_list(data, step):
    print(f"- list (len {len(data)}, step {step})\n")
    list_ = []
    for i in range(0, len(data), step):
        start = time.time()
        for j in range(i, i + step):
            list_.append(data[j])
        end = time.time()
        print(f"add to list     ({i:>7} ~ {i+step-1:>7}): {end - start:0.3f} sec")
    print()

    data_to_find = random.sample(data, len(data) // 2)
    start = time.time()
    for d in data_to_find:
        if d in list_:
            pass
    end = time.time()
    print(f"find in list    (data count: {len(data)//2:>5}): {end - start:0.3f} sec")
    print()


def test_my_set(data, step, bucket_size):
    print(f"- my set (len {len(data)}, step {step})\n")
    my_set = MySet(bucket_size)
    for i in range(0, len(data), step):
        start = time.time()
        for j in range(i, i + step):
            my_set.add(data[j])
        end = time.time()
        print(f"add to my set   ({i:>7} ~ {i+step-1:>7}): {end - start:0.3f} sec")
    print()

    data_to_find = random.sample(data, len(data) // 2)
    start = time.time()
    for d in data_to_find:
        if d in my_set:
            pass
    end = time.time()
    print(f"find in my set  (data count: {len(data)//2:>5}): {end - start:0.3f} sec")
    print()


def problem1(data, step):
    print("=" * 50)
    print("test 1: normal data")
    print("=" * 50)

    test_set(data, step)
    # test_list(data, step)


def problem2(data, step):
    print("=" * 50)
    print("test 2: hash collision data")
    print("=" * 50)

    woo_data = [Woodogi(d) for d in data]
    test_set(woo_data, step)


def problem3(data, step, bucket_size=1024):
    print("=" * 50)
    print("test 3: myset")
    print("=" * 50)

    test_my_set(data, step, bucket_size)


if __name__ == "__main__":
    count = 1_000_000
    step = 100_000
    data = init_data(count)

    problem1(data, step)
    # problem2(data, step)
    problem3(data, step, 1024 * 128)
