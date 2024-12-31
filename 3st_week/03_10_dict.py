dict = {"fast": "빠른"}

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index =hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("333", 3)
my_dict.put("77", 7)