/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 13:21:25 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 13:24:24 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	int	swap;

	swap = *a;
	*a = *b;
	*b = swap;
}
/*
#include <stdio.h>
int	main(void)
{
	int	a = 4;
	int	b = 2;
	printf("%i%i\n", a, b);
	ft_swap(&a, &b);
	printf("%i%i\n", a, b);
	return (0);
}
*/
