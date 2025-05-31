This project was created for fun.
The program is written in Python 3 and uses common libraries.
I aimed to simulate evolution as realistically as possible.

Plants:
Each plant has a "DNA" made of pre-written, randomly mixed conditions with logical statements. This DNA determines how the plant grows. It dictates both where to grow and what type of cell to use:

    "n" = normal

    "e" = energy

    "s" = seed (only seed cells can plant)

When a plant with a seed cell dies, it copies its DNA to the new plant with ~5% chance of mutation per statement. This allows for complex evolution. If the mutation rate is too high, evolution may stall at simple forms like "grass".

World:
The world is ~50 cells high and ~1000 cells wide. The left and right edges are connected (toroidal world), so plants growing past one side appear on the opposite.

Sun:
The sun gives energy only to topmost cells. It encourages vertical growth, as cells below are blocked from sunlight. Plants need this energy not only to grow but also to stay alive. Covered plants die due to energy starvation.

Lifespan:
Each plant has a random lifespan. This prevents a single dominant plant from taking over the entire world and stalling evolution.

Display:
The simulation is displayed using simple print() statements. Adjust your terminal size to fit the output.

Triple Display:
To make the world as wide as possible and fit 16:9 screens, the world is split into three horizontal lines in the terminal. These lines are connected, forming one continuous world.

Note:
Having many plants at once is important. Otherwise, random events might wipe out all plants and reset the simulation.
