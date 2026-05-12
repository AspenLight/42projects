/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 19:02:28 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/11 19:09:31 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	result;

	result = 1;
	if (power < 0)
		return (0);
	else if (power == 0)
		return (1);
	else if (power == 1)
		return (nb);
	else
	{
		while (power > 0)
		{
			result = result * nb;
			power--;
		}
		return (result);
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int	result = ft_iterative_power(6, 5);
	printf("%i\n", result);
	return (0);
}
*/
