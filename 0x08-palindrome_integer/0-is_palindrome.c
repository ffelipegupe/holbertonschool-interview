#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "palindrome.h"

/**
 * reversed - function that reverse a number
 *
 * @n: number to be reversed
 *
 * Return: the reversed number
 */
int reversed(int n)
{
	int digit = (int)log10(n);
	if (n == 0)
		return 0;
       return ((n%10 * pow(10, digit)) + reversed(n/10));
}


/**
 * is_palindrome - checks if a given unsigned integer is a palindrome.
 *
 * @n: number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise.
 */
int is_palindrome(unsigned long n)
{
	if (n == (unsigned long)reversed(n))
	{
		return 1;
	}
	return 0;
}
