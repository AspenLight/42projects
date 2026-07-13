/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/05 17:02:45 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/06 12:58:40 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_factorial(int nb)
{
	if (nb == 1 || nb == 0)
		return (1);
	else if (nb > 0)
		return (nb * ft_recursive_factorial(nb - 1));
	else
		return (0);
}
/*
#include <stdio.h>
int	main(void)
{
	int	i;

	i = 0;
	while (i < 10)
	{
		printf("%d\n", ft_recursive_factorial(i));
		i++;
	}
	return (0);
}
*/
