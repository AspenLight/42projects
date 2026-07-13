/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/05 17:10:30 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/07 13:34:39 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	temp;

	temp = nb;
	if (power == 0)
		return (1);
	if (power < 0)
		return (0);
	while (power > 1)
	{
		nb *= temp;
		power--;
	}
	return (nb);
}
/*
#include <stdio.h>
int	main(void)
{
	printf("%d\n", ft_iterative_power(9, 2));
	return (0);
}
*/
