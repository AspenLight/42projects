/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 13:45:52 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 14:54:28 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	hold;
	int	minimum;

	i = 0;
	hold = 0;
	while (i < (size - 1))
	{
		minimum = i;
		j = i + 1;
		while (j < size)
		{
			if (tab[j] < tab[minimum])
				minimum = j;
			j++;
		}
		if (minimum != i)
		{
			hold = tab[minimum];
			tab[minimum] = tab[i];
			tab[i] = hold;
		}
		i++;
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int	tab[] = {5, 3, 4, 1};
	int	size = 4;
	int	i = 0;
	while (i < size)
	{
		printf("%i\n", tab[i]);
		i++;
	}
	i = 0;
	printf("------\n");
	ft_sort_int_tab(tab, size);
	while (i < size)
	{
		printf("%i\n", tab[i]);
		i++;
	}
	return (0);
}
*/
