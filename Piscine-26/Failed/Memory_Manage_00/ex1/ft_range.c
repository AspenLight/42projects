/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 19:07:08 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/23 20:26:05 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	size;
	int	*range;
	int	i;

	size = max - min;
	if (size <= 0)
		return (NULL);
	range = malloc(size * sizeof(int));
	i = 0;
	while (i < size)
	{
		range[i] = min;
		min++;
		i++;
	}
	return (range);
}
/*
#include <stdio.h>
int	main(void)
{
	int	min = -3;
	int	max = 9;
	int	*range = ft_range(min, max);
	int	size = max - min;
	int	i = 0;
	while (i < size)
	{
		printf("%i\n", range[i]);
		i++;
	}
	return (0);
}
*/
