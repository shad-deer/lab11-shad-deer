# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    #   a function that accepts the number
    # it them performs n*2
    # then loop thru the list 
    # we want this performed ALL at the same time
    async def double(n):
        await asyncio.sleep(0)
        return n * 2
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    return await asyncio.gather(*(double(n) for n in numbers))


async def fastest(jobs):
    # Outline:
    #  in words of chefs
    # we have a chef with three things on counter
    # We want the chef to get me the fastest cooking item
    # where to start
        # each job and its time
        # once each job has its time up, the label rings
        # the chef gives me as areturn, that specific food, and the function is complete
        # we can use no await value to start all of these at the same time.
    async def run_job (label, delay):
        await asyncio.sleep(delay)
        return label
    tasks = [run_job(label, delay) for label, delay in jobs]

    for completed_task in asyncio.as_completed(tasks):
        return await completed_task
             
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)



def echo_once(host, port, message):
    # Outline:
    #   I think i did this once in class...
    # connect to the host and port
    # send a message that is encoded in bytes
    # and then recieve that message decoded as a string
    DATA_SIZE = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port)) # blocking
        client.sendall(message.encode())
        reply = client.recv(DATA_SIZE) # blocking
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    return reply.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
