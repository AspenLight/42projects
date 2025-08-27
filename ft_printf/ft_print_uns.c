/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_uns.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:09:57 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:29:40 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_uns(unsigned int i)
{
	char			c;
	unsigned long	nb;
	int				count;

	nb = i;
	count = 0;
	if (nb > 9)
	{
		ft_print_uns((nb / 10));
	}
	c = (nb % 10) + '0';
	write(0, &c, 1);
	count++;
	return (count);
}
