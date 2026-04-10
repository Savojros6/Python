a simple logical way for J to intelligently move around obstacles
Your current method is “greedy + random fallback.”
A smarter (but still simple) method that actually solves mazes is Breadth-First Search (BFS),
which can be explained in plain English like this:

Pretend you are standing at J’s current position and you can only move to the four adjacent
cells (no diagonals, no trees, no flag).

Make a mental “map” of the whole grid, but only the open cells (the ., ,, and @ cells).
Trees and the flag are walls you cannot step on.

Start from J’s position and flood outward in rings:
Ring 0 = J’s current square.
Ring 1 = all open squares directly next to J.
Ring 2 = all open squares next to Ring 1 that haven’t been visited yet.
Keep going ring by ring until you reach the ring that contains the player @.

Once you have found the ring that holds @, walk backwards from @ to J using the rings you just made.
The first step of that backward path is exactly the single move J should make right now.

Why this works:

It always finds the shortest possible path around any number of trees.
It never gets stuck in dead-ends
(because it explores every possible route at the same “distance” before going farther).
It automatically handles the flag and board edges correctly if you simply mark them as “not walkable.”
On a tiny 9×19 grid it is extremely fast — you can do the whole flood-fill in a fraction of a second.

This is the standard way almost every simple grid-based enemy finds its target when there are obstacles.
It is the same idea used in classic games like Pac-Man ghosts (when they are chasing) or in roguelikes.
You do not need any fancy math — just a list of positions to explore and a way to remember “which ring
each cell belongs to.” Once you have that ring map, J can always pick the single best next step even
when trees are in the way.



How BFS actually works (the rings + backtracking part)
I’ll explain it without any code, just the pure logical idea, because that’s what you asked for.
Imagine the grid is a big empty field with some trees as walls. You are standing at J’s position. BFS does this:

Create the rings (distance layers)
Start at J’s square → call this Ring 0.
Look at the four cells directly touching it (north, east, south, west) that are not trees or the flag.
All those cells become Ring 1 (they are distance 1 away from J).
Now look at every cell that touches any Ring-1 cell (but hasn’t been visited yet) → those become Ring 2.
Repeat: Ring 3, Ring 4, etc., until you finally add the cell that contains “@” to some ring.You now have
a complete “distance map” where every open cell knows exactly how many steps away it is from J. The rings
are just the sets of cells that share the same distance.

Why the rings make backtracking easy
The magic is that each ring only connects to the ring immediately before it and the ring immediately after it.
So once you have found which ring contains “@”, you can start at the player’s cell and walk backwards one ring at a time:
From @ (say it’s in Ring 5), look at its four neighbors.
Exactly one of them will be in Ring 4 (the previous ring).
That neighbor is the cell you “came from” to reach @.
Now move to that Ring-4 cell and repeat: look at its neighbors — exactly one will be in Ring 3.
Keep doing this until you reach Ring 0 (J’s starting position).
The very first step you take when walking backwards (i.e., the cell that is in Ring 1 and touches J in Ring 0)
is exactly the single best move J should make right now.

That’s the whole trick. The rings give you a perfect “breadcrumb trail” of increasing distance. Because
you built the rings outward from J, walking back along decreasing ring numbers automatically gives you the
shortest path without ever getting stuck or going the long way around trees.
It’s the same idea as dropping numbered markers on the floor while you explore every possible route at the
same “speed.” When you finally reach the player, you just follow the numbers in reverse order to get home.
That reverse walk is trivial to code once you have the ring (distance) information for every cell.
So in summary:

Your current code style is perfectly conventional for where you are in learning.
BFS is just “flood fill the map with distance rings from J” → then “walk backwards down the rings from @ to J”
to decide the next move. The rings make the backtracking step almost automatic.