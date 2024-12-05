from unittest import TestCase
from main.maze import MazeGame

# class for the test suite
class TestMazeIsWalkable(TestCase):

    # testing walkable path
    def test_walkable_path(self):
        # instantiating the MazeGame
        maze = MazeGame()

        # creating a mock maze, and storing it the variable that would have the maze created by the recursive function
        # 1s are walls, and 0(zeroes) are paths
        maze.maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]
        ]
        # coordinates for the end of the maze
        maze.endpoint_position = [4, 4]

        # passing coordinates for a path that should return True
        self.assertTrue(maze.is_walkable(1, 2))
        self.assertTrue(maze.is_walkable(3, 3))


    def test_walkable_wall(self):
        # same as above, but passing coordintes for a wall, and should return false as it should not be walkable for the hero sprite
        maze = MazeGame()

        maze.maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]
        ]
        maze.endpoint_position = [4, 4]

        self.assertFalse(maze.is_walkable(0, 0))
        self.assertFalse(maze.is_walkable(2, 2))


    # testing the endpoint with a ZERO
    def test_end_point_with_0(self):

        maze = MazeGame()

        maze.maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]
        ]

        maze.endpoint_position = [4, 4]

        self.assertTrue(maze.is_walkable(4, 4))

    # testng the endpoint with a 1 at the coordinate which would normally be a wall
    def test_end_point_with_1(self):

        maze = MazeGame()

        maze.maze = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1]
        ]

        # the reason a endpoint position is needed is because we want to make sure the exit to the maze is always in the
        # same place, and at the opposite end to the start. So the endpoint will always be walkable regardless of whether
        # it lands on a 0 or a 1. We are testing with a 1 in the end position to test that it still accepts it as walkable
        # As the maze is being randomly generated using a recursive function, you could not garantee that there would always
        # be a zero in the same position. By passing the endpoint_position varibale to the is_walkable function, that will
        # always be walkable
        maze.endpoint_position = [4, 4]

        self.assertTrue(maze.is_walkable(4, 4))
