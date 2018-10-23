from queue import *

class TabuList():
    def __init__(self, max_num_vals):
        self.que = Queue(max_num_vals)
        self.dict = dict()

    def check_in(self, key):
        return ''.join(key) in self.dict

    def check_and_add(self, key):
        if self.check_in(key):
            return True
        
        if self.que.full():
            r_key = self.que.get()
            del self.dict[r_key]

        parsed_key = ''.join(key)

        self.que.put(parsed_key)
        self.dict[parsed_key] = 0

        return False

if __name__ == "__main__":
    tabu = TabuList(5)
    tabu.check_and_add(["A"])
    tabu.check_and_add(["B"])
    tabu.check_and_add(["C"])
    tabu.check_and_add(["D"])
    tabu.check_and_add(["E"])

    print(tabu.check_in(["T"]) == False)
    print(tabu.check_in(["A"]) == True)

    print(tabu.check_and_add(["A"]) == True)
    print(tabu.check_and_add(["T"]) == False)

    print(tabu.check_in(["T"]) == True)
    print(tabu.check_in(["A"]) == False)