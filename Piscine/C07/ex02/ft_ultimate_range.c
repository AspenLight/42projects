/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/08 13:59:10 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/09 16:31:00 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int	diff;
	int	i;

	diff = 0;
	i = 0;
	if (min >= max)
		return (0);
	diff = max - min;
	*range = malloc(sizeof(*range) * (diff + 1));
	while (min < max)
	{
		(*range)[i] = min;
		i++;
		min++;
		if (min == max)
			return (i);
	}
	return (-1);
}
/*
#include <stdio.h>
int	main(void)
{
	int	min;
	int	max;
	int	i;
	int	*range;
	int	**rangepoint;

	min = 2;
	max = 17;
	i = 0;
	range = 0;
	rangepoint = &range;
	int n = ft_ultimate_range(rangepoint, min, max);
	printf("%d\n", n);
	while (i < n)
        {
                printf("%d: %d\n", i, range[i]);
                i++;
        }
	free(range);
	return (0);
}
*/
