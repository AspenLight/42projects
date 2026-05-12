/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 18:49:35 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/11 18:56:45 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	hold;

	hold = 1;
	if (nb < 0)
		return (0);
	else if (nb == 0 || nb == 1)
		return (1);
	else
	{
		while (nb > 0)
		{
			hold = nb * hold;
			nb--;
		}
		return (hold);
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int	result = ft_iterative_factorial(12);
	printf("%i\n", result);
	return (0);
}
*/
