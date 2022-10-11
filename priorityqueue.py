class PriorityRank(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return "\n".join(["\n".join(["{0}: {1}".format(key, pair[key]) for key in pair]) for pair in self.queue])
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    # for inserting an element in the queue
    def insert(self, data):
        if (type(data) == dict) and (len(data) == 1):
            new_key = list(data.keys())[0]
            if (type(new_key) == str) and (type(data[new_key]) == int):
                self.queue.append(data)
    # for popping an element based on Priority
    def delete(self):
        if self.isEmpty():
            return [None, None]
        max_index = None
        max_int = None
        max_key = None
        for i in range(len(self.queue)):
            pair_key = list(self.queue[i].keys())[0]
            pair_int = self.queue[i][pair_key]
            if (max_index == None) or (pair_int < max_int):
                max_index = i
                max_int = pair_int
                max_key = pair_key
        del self.queue[max_index]
        return [max_key, max_int]

if __name__ == '__main__':
    myQueue = PriorityRank()
    print("add Priority ranklist")
    rank_no=int(input("No. of ranks :"))
    while(rank_no>0):
        rank_name=input("name of rank:")
        rank_position=input("position of rank(0-10) :")
        myQueue.insert({rank_name:int(rank_position)})
        rank_no-=1
    while(True):
        print(myQueue)
        print("Menu")
        print("Add New Rank to List-1")
        print("Change Existing rank-2")
        print("Delete the priority-3")
        x=int(input("Your Choice :"))
        if(x==3):
            while not myQueue.isEmpty():
                key, value = myQueue.delete()
                if key:
                    print("Delete {1}".format(value, key))
        if(x==1):
            rank_name=input("name of rank:")
            rank_position=input("position of rank(0-10) :")
            myQueue.insert({rank_name:int(rank_position)})
        if(x==2):
            myQueue2 = PriorityRank()
            select_rank=input("Choose the Rank want to change(rank name):") 
            while not myQueue.isEmpty():
                key, value = myQueue.delete()
                if key==select_rank:
                    new_rp=int(input("New Rank Position:"))
                    value=new_rp
                myQueue2.insert({key:value})
            while not myQueue2.isEmpty():
                key, value = myQueue2.delete()
                myQueue.insert({key:value})