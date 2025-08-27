/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_dec.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:01:37 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:29:30 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_dec(int i)
{
	char	c;
	long	nb;
	int		count;

	nb = i;
	count = 0;
	if (nb < 0)
	{
		write(0, "-", 1);
		nb = -nb;
		count++;
	}
	if (nb > 9)
	{
		count += ft_print_dec((nb / 10));
	}
	c = (nb % 10) + '0';
	write(0, &c, 1);
	count++;
	return (count);
}
