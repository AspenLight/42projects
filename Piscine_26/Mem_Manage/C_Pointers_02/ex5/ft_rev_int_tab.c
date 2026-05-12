/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 13:35:11 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 13:45:20 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int	i;
	int	rev;
	int	hold;

	i = 0;
	rev = size - 1;
	hold = 0;
	while (i < size / 2)
	{
		hold = tab[i];
		tab[i] = tab[rev];
		tab[rev] = hold;
		rev--;
		i++;
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int	tab[] = {1, 5, 3, 4};
	int	size = 4;
	int	i = 0;
	while (i < size)
	{
		printf("%i\n", tab[i]);
		i++;
	}
	i = 0;
	printf("------\n");
	ft_rev_int_tab(tab, size);
	while (i < size)
	{
		printf("%i\n", tab[i]);
		i++;
	}
	return (0);
}
*/
