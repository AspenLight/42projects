/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_err.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/05 18:06:59 by nmak              #+#    #+#             */
/*   Updated: 2026/06/05 23:58:36 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_putchar_err(char c, int *ptr_count)
{
	write (2, &c, 1);
	*ptr_count += 1;
}

void	ft_putstr_err(const char *str, int *ptr_count)
{
	if (!str)
	{
		ft_putstr_err("(null)", ptr_count);
		return ;
	}
	while (*str)
	{
		ft_putchar_err(*str, ptr_count);
		str++;
	}
}

void	ft_putnbr_err(long int nb, int *ptr_count)
{
	if (nb < 0)
	{
		nb = -nb;
		ft_putchar_err('-', ptr_count);
	}
	if (nb > 9)
		ft_putnbr_err(nb / 10, ptr_count);
	nb = nb % 10 + '0';
	ft_putchar_err((char)nb, ptr_count);
}

void	ft_percent_err(const char *str, va_list list, int *ptr_count)
{
	if (*str == 'c')
		ft_putchar_err((char)va_arg(list, int), ptr_count);
	else if (*str == 's')
		ft_putstr_err((char *)va_arg(list, char *), ptr_count);
	else if (*str == 'd' || *str == 'i')
		ft_putnbr_err((long int)va_arg(list, int), ptr_count);
	else if (*str == '%')
		ft_putchar_err(*str, ptr_count);
	str++;
}

int	ft_print_err(const char *str, ...)
{
	int		count;
	va_list	list;

	count = 0;
	va_start(list, str);
	if (!str)
		return (-1);
	while (*str)
	{
		if (str[1] && *str == '%')
			ft_percent_err(++str, list, &count);
		else
			ft_putchar_err(*str, &count);
		str++;
	}
	va_end(list);
	return (count);
}
