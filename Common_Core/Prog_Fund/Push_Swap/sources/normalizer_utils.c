/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   normalizer_utils.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 16:48:26 by nmak              #+#    #+#             */
/*   Updated: 2026/06/08 17:51:35 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Swap a and b values
void	qs_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

//	Return the position of the index
//	Sort the array between low and high around a pivot
int	partition(int tab[], int low, int high)
{
	int	i;
	int	pivot;

	i = low - 1;
	pivot = tab[high];
	while (low < high)
	{
		if (tab[low] <= pivot)
		{
			i++;
			qs_swap(&tab[low], &tab[i]);
		}
		low++;
	}
	qs_swap(&tab[i + 1], &tab[high]);
	return (i + 1);
}

//	Recursively call partition to split and sort the array around a pivot
void	quicksort(int tab[], int low, int high)
{
	int	pi;

	if (low >= high)
		return ;
	pi = partition(tab, low, high);
	quicksort(tab, low, pi - 1);
	quicksort(tab, pi + 1, high);
}
