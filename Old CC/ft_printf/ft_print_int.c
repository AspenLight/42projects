/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_int.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:08:43 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:29:35 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_int(int i)
{
	char	c;
	long	nb;
	int		count;

	count = 0;
	nb = i;
	if (nb < 0)
	{
		write(0, "-", 1);
		nb = -nb;
		count++;
	}
	if (nb > 9)
	{
		count += ft_print_int((nb / 10));
	}
	c = (nb % 10) + '0';
	write(0, &c, 1);
	count++;
	return (count);
}
