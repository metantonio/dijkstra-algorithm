# Install project

```sh
poetry install
```

# Run Algorithm

```sh
poetry run python ./dijkstra.py
```

To find the shortest path between Alice and David.

<img src="./Figure_1.png"></img>

# Exercise proposition:

- Imagine every person starts with a distance of 100 between them.
- Every time that a person have an interaction with another, the distance between them is reduced by:

```py
    distance = 100/(N+1)

#   Where N = number of times that the user has interacted with another user.
```

- If distance between 2 users that never shared directly, is less or equal than 40, that user should appears as suggestion.
- If distance between 2 users that never shared directly, is less or equal than 10, that user should appear as recommendation as friend.

Solution for the exercise:

```sh
poetry run python ./exercise.py
```

<img src="./Figure_2.png"></img>