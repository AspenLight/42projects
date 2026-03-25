/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 16:54:46 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/11 16:23:31 by aspthiba         ###   ########.fr       */
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

void	ft_print_comb2(void)
{
	int	a;
	int	b;

	a = 0;
	while (a <= 98)
	{
		b = a + 1;
		while (b <= 99)
		{
			if (a < 10)
				ft_putnbr(0);
			ft_putnbr(a);
			write(1, " ", 1);
			if (b < 10)
				ft_putnbr(0);
			ft_putnbr(b);
			if (!(a == 98 && b == 99))
				write(1, ", ", 2);
			b++;
		}
		a++;
	}
}
/*
int main(void)
{
    ft_print_comb2();
    return (0);
}
*/
