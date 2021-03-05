#include "menger.h"
/**
 * menger - function that draws a 2D Menger Sponge
 * @level: level of the Menger Sponge to draw
 * Return: Nothing.
 */
void menger(int level)
{
	int r;
	int c;
	int n_level;

	if (level < 0)
		return;
	n_level = pow(3, level);
	for (r = 0; r < n_level; r++)
	{
		for (c = 0; c < n_level; c++)
			putchar(helper(r, c));
		putchar('\n');
	}
}
/**
 * helper - helper function to draw
 * @col: columns
 * @row: rows
 * Return: "#" or " "
 */
char helper(int col, int row)
{
	while (row || col)
	{
		if (col % 3 == 1 && row % 3 == 1)
			return (' ');
		row = row / 3;
		col = col / 3;
	}
	return ('#');
}
