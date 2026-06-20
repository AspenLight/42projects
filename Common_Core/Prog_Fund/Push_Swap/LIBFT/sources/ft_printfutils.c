/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printfutils.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/07 18:35:16 by nmak              #+#    #+#             */
/*   Updated: 2026/05/17 06:25:48 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putchar(char c, int *ptr_count)
{
	write (1, &c, 1);
	*ptr_count += 1;
}

void	ft_putstr(const char *str, int *ptr_count)
{
	if (!str)
	{
		ft_putstr("(null)", ptr_count);
		return ;
	}
	while (*str)
	{
		ft_putchar(*str, ptr_count);
		str++;
	}
}

void	ft_putnbr(long int nb, int *ptr_count)
{
	if (nb < 0)
	{
		nb = -nb;
		ft_putchar('-', ptr_count);
	}
	if (nb > 9)
		ft_putnbr(nb / 10, ptr_count);
	nb = nb % 10 + '0';
	ft_putchar((char)nb, ptr_count);
}

void	ft_u_putnbr(unsigned long nb, int *ptr_count)
{
	if (nb > 9)
		ft_u_putnbr(nb / 10, ptr_count);
	ft_putchar(nb % 10 + '0', ptr_count);
}

void	ft_puthex(unsigned long nb, int *ptr_count, int isupper)
{
	char	*lower_hex;
	char	*upper_hex;

	lower_hex = "0123456789abcdef";
	upper_hex = "0123456789ABCDEF";
	if (isupper == 1)
	{
		if (nb / 16)
			ft_puthex(nb / 16, ptr_count, 1);
		ft_putchar(upper_hex[nb % 16], ptr_count);
	}
	if (isupper == 0)
	{
		if (nb / 16)
			ft_puthex(nb / 16, ptr_count, 0);
		ft_putchar(lower_hex[nb % 16], ptr_count);
	}
}
