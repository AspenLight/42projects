/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/05 17:16:32 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/07 13:36:16 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_power(int nb, int power)
{
	if (power == 0)
		return (1);
	if (power < 0)
		return (0);
	if (power == 1)
		return (nb);
	else if (power > 1)
		return (nb * ft_recursive_power(nb, power - 1));
	else
		return (0);
}
/*
#include <stdio.h>
int	main(void)
{
	printf("%d\n", ft_recursive_power(4, 2));
	return (0);
}
*/
