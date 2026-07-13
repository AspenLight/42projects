/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/08 13:59:10 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/09 15:59:08 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	diff;
	int	i;
	int	*range;

	diff = 0;
	i = 0;
	if (min >= max)
		return ((void *)0);
	diff = max - min;
	range = malloc(sizeof(int) * (diff));
	while (min < max)
	{
		range[i] = min;
		i++;
		min++;
	}
	return (range);
}
/*
#include <stdio.h>
int	main(void)
{
	int	min;
	int	max;
	int	i;

	min = 2;
	max = 17;
	i = 0;
	int	*result = ft_range(min, max);
	while (result[i])
	{
		printf("%d: %d\n", i, result[i]);
		i++;
	}
	return (0);
}
*/
