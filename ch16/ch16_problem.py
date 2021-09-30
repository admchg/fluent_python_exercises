# Ch 16 Couroutines
# THE PESTERING BUTLER
# Q. With the knowledge of coroutines, we now know that you can have 'conversations' with a function
# i.e. you can send and receive information. Use this principle to create a butler 'chatbot' that
# cyclically offers you 3 beverage choices (latte, espresso, capuccino), and accepts your input.
# When your input is 1, the butler brings you the beverage; when your input is 99, the butler leaves.
# For all other inputs, the butler keeps pestering you about which beverage you'd like.

## Sample Conversation (The numbers are inputs by the user)
# <The program is launched>
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
# <The program exits here>


## Sample Conversation 2 (The numbers are inputs by the user)
# <The program is launched>
# You want latte?
# 5
# You want espresso?
# 99
# Okay I will leave. But please don't fire me, Sir.
# <The program exits here>


from itertools import cycle


def beverage():
    beverages = cycle(["espresso", "capuccino", "latte"])

    request = yield None
    while True:
        bev = next(beverages)
        request = yield f"You want {bev}"
        if request == "1":
            break

    # Initialize and yield a choice of beverages cyclically
    # Break away if coroutine is 'sent' a '1'
    return f"Fine, I will get you a {bev}"


def serve():
    # Initialize and prime the beverage couroutine
    # Start taking user inputs
    # You can set 99 as the escape (break) request and send other responses to the coroutine.
    # Finally, catch exception to accept the order.
    bev = beverage()
    next(bev)
    print(bev.send(0))
    while True:
        req = input()
        if req == "99":
            return "Okay I will leave. But please don't fire me, Sir."
        else:
            try:
                print(bev.send(req))
            except StopIteration as exc:
                print(exc.value)
                break


if __name__ == "__main__":
    serve()
