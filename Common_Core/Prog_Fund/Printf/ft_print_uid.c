/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_uid.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/12 18:30:40 by aspthiba          #+#    #+#             */
/*   Updated: 2026/05/12 18:31:53 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_count_uns(unsigned int i)
{
	int	count;

	count = 0;
	while (i != 0)
	{
		count++;
		i = i / 10;
	}
	return (count);
}

int	ft_print_uns(unsigned int i)
{
	char			c;
	unsigned long	nb;

	nb = i;
	if (nb > 9)
	{
		ft_print_uns((nb / 10));
	}
	c = (nb % 10) + '0';
	write(1, &c, 1);
	return (ft_count_uns(i));
}

int	ft_print_int(int i)
{
	char	c;
	long	nb;
	int		count;

	count = 0;
	nb = i;
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
		count++;
	}
	if (nb > 9)
	{
		count += ft_print_int((nb / 10));
	}
	c = (nb % 10) + '0';
	write(1, &c, 1);
	count++;
	return (count);
}