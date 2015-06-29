__author__ = "jeffrey"
__date__ = "$2015/6/29 下午 05:20:50$"

import collections

ALIVE = '*'
EMPTY = '-'
Query = collections.namedtuple('Query', ('y', 'x'))
Transition = collections.namedtuple('Transition', ('y', 'x', 'state'))

def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast
    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # Southeast
    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # Southwest
    w_ = yield Query(y + 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # Northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY # Die: Too few
        elif neighbors > 3:
            return EMPTY # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE # Regenerate
    return state

TICK = object()

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK

def test_count_neighbors():
    it = count_neighbors(10, 5)
    q1 = next(it)                  # Get the first query
    print('First yield: ', q1)
    q2 = it.send(ALIVE)            # Send q1 state, get q2
    print('Second yield:', q2)
    q3 = it.send(ALIVE)            # Send q2 state, get q3
    print('...')
    q4 = it.send(EMPTY)
    q5 = it.send(EMPTY)
    q6 = it.send(EMPTY)
    q7 = it.send(EMPTY)
    q8 = it.send(EMPTY)
    try:
        count = it.send(EMPTY)     # Send q8 state, retrieve count
    except StopIteration as e:
        print('Count: ', e.value)  # Value from return statement    

def test_step_cell():
    it = step_cell(10, 5)
    q0 = next(it)           # Initial location query
    print('Me:      ', q0)
    q1 = it.send(ALIVE)     # Send my status, get neighbor query
    print('Q1:      ', q1)
    print('...')
    q2 = it.send(ALIVE)
    q3 = it.send(ALIVE)
    q4 = it.send(ALIVE)
    q5 = it.send(ALIVE)
    q6 = it.send(EMPTY)
    q7 = it.send(EMPTY)
    q8 = it.send(EMPTY)
    t1 = it.send(EMPTY)     # Send for q8, get game decision
    print('Outcome: ', t1)

if __name__ == "__main__":
    test_count_neighbors()
    test_step_cell()