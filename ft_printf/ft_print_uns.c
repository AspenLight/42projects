/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_uns.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:09:57 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/28 00:10:49 by asthibau         ###   ########.fr       */
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
	write(0, &c, 1);
	return (ft_count_uns(i));
}
