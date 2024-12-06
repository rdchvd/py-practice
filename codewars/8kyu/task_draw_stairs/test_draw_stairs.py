import timeit
import tracemalloc
import unittest
from .solution import draw_stairs, draw_stairs_recursive


class TestDrawStairs(unittest.TestCase):
	test_cases = [
		(1, "I"),
		(2, "I\n I"),
		(3, "I\n I\n  I"),
		(4, "I\n I\n  I\n   I"),
		(10, "I\n I\n  I\n   I\n    I\n     I\n      I\n       I\n        I\n         I"),
	]

	def test_draw_stairs(self):
		for n, expected in self.test_cases:
			self.assertEqual(draw_stairs(n), expected)

	def test_draw_stairs_recursive(self):
		for n, expected in self.test_cases:
			self.assertEqual(draw_stairs_recursive(n), expected)

	@staticmethod
	def test_measure_time():
		join_time = timeit.timeit(lambda: draw_stairs(100), number=100)
		recursive_time = timeit.timeit(lambda: draw_stairs_recursive(100), number=100)

		print(f"[Draw Stairs] Join method: {join_time:.6f} seconds")
		print(f"[Draw Stairs] Recursive method: {recursive_time:.6f} seconds")

	@staticmethod
	def test_measure_memory():
		tracemalloc.start()

		draw_stairs(100)
		join_memory = tracemalloc.get_traced_memory()[1]

		tracemalloc.reset_peak()
		draw_stairs_recursive(100)
		recursive_memory = tracemalloc.get_traced_memory()[1]

		tracemalloc.stop()

		print(f"[Draw Stairs] Join method peak memory: {join_memory} bytes")
		print(f"[Draw Stairs] Recursive method peak memory: {recursive_memory} bytes")


if __name__ == "__main__":
	unittest.main()
	TestDrawStairs.test_measure_time()
	TestDrawStairs.test_measure_memory()

