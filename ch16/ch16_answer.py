# Ch 16 Couroutines
# THE PESTERING BUTLER
# Q. With the knowledge of coroutines, we now know that you can have 'conversations' with a function
# i.e. you can send and receive information. Use this principle to create a butler 'chatbot' that
# cyclically offers you 3 beverage choices (latte, espresso, capuccino), and accepts your input.
# When your input is 1, the butler brings you the beverage; when your input is 99, the butler leaves. 
# For all other inputs, the butler keeps pestering you about which beverage you'd like.

## Sample Conversation (The numbers are inputs by the user)
# You want latte?
# 0
# You want espresso?
# 3
# You want capuccino?
# 05
# You want latte?
# 2
# You want espresso?
# 1
# Fine, I will get you espresso

## Sample Conversation 2 (The numbers are inputs by the user)
# You want latte?
# 5
# You want espresso?
# 99
# Okay I will leave. But please don't fire me, Sir.


from itertools import cycle  
def beverage():
    bev_list = cycle(['latte', 'espresso', 'capuccino'])
    while True:
        bev = next(bev_list)
        print("You want " + bev + '?')
        choice = yield bev
        if choice == 1:
           break
    return bev

def serve():
    b = beverage()
    next(b)
    take_input = -1
    while True:
        take_input = int(input())
        if take_input == 99:
            print("Okay I will leave. But please don't fire me, Sir.")
            break
        try:
            b.send(take_input) 
        except StopIteration as bev:
            print("Fine, I will get you " + bev.value)
            break
        
        
if __name__ == "__main__":
    serve()

