#include <stdlib.h>
#include <stdio.h>
#include "palindrome.h"

/**
 * is_palindrome - checks if a given unsigned integer is a palindrome.
 *
 * @n: number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise.
 */
int is_palindrome(unsigned long n)
{
	unsigned long master = 0;
	unsigned long reversed = 0;
	unsigned long remainder = 0;

	master = n;
	while (n != 0)
	{
		remainder = n % 10;
		reversed = reversed * 10 + remainder;
		n = n / 10;
	}
	if (master == reversed)
		return (1);
	return (0);
}
