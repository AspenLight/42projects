/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 19:55:44 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/04 20:06:04 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(int nb)
{
	char	n;

	if (nb == -2147483648)
	{
		write(1, "-2147483648", 11);
		return ;
	}
	else if (nb < 0)
	{
		write(1, "-", 1);
		ft_putnbr(-nb);
	}
	else if (nb < 10)
	{
		n = nb + '0';
		write(1, &n, 1);
	}
	else if (nb > 9 && nb <= 2147483647)
	{
		ft_putnbr(nb / 10);
		n = (nb % 10) + '0';
		write(1, &n, 1);
	}
}
/*
int	main(void)
{
	int	nb;

	nb = -137;
	ft_putnbr(nb);
	return (0);
}
*/
