from functools import reduce, lru_cache
import socket

@lru_cache(maxsize=20)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
func = [fib]
for i in range(40):
    values = list(map(lambda x: x(i), func))

print(values)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Jealousy and the suffering it inflicts on lovers is at the heart of Shakespeare's later romances, Cymbeline and The Winter's Tale. Few moments in Shakespeare's plays are as intense as that in which Posthumus comes to believe that Imogen has slept with Iachimo (Cymbeline, 2.4). Although they bring us to the brink of tragedy, Cymbeline and The Winter's Tale end with the defeat of jealousy, and so they are considered comedies. This is not the case with Shakespeare's best-known exploration of the green-eyed monster", "utf-8"))
    clientsocket.close()

