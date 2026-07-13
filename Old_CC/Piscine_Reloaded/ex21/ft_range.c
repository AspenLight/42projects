/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/24 14:09:58 by asthibau          #+#    #+#             */
/*   Updated: 2025/04/24 14:20:45 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	diff;
	int	i;
	int	*result;

	i = 0;
	diff = max - min;
	if (diff <= 0)
		return (0);
	result = malloc(sizeof(int) * (diff));
	while (min < max)
	{
		result[i] = min;
		min++;
		i++;
	}
	return (result);
}
