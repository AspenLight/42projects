/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/25 17:21:12 by aspthiba          #+#    #+#             */
/*   Updated: 2026/05/12 18:52:56 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *str, ...)
{
	int		i;
	int		count;
	va_list	args;

	i = 0;
	count = 0;
	va_start(args, str);
	if (str == NULL)
		return (-1);
	while (str[i])
	{
		if (str[i] == '%')
		{
			count = check_percent(str[i + 1], count, args);
			i += 2;
		}
		else
		{
			write(1, &str[i], 1);
			count++;
			i++;
		}
	}
	va_end(args);
	return (count);
}

int	check_percent(char c, int count, va_list args)
{
	if (c == '%')
	{
		write(1, "%", 1);
		count++;
	}
	if (c == 'c')
		count += ft_print_char(va_arg(args, int));
	if (c == 's')
		count += ft_print_str(va_arg(args, char *));
	if (c == 'p')
	{
		count += ft_print_ptr((unsigned long int)va_arg(args, void *));
	}
	if (c == 'd')
		count += ft_print_int(va_arg(args, int));
	if (c == 'i')
		count += ft_print_int(va_arg(args, int));
	if (c == 'u')
		count += ft_print_uns(va_arg(args, unsigned int));
	if (c == 'x')
		count += ft_print_hex(va_arg(args, unsigned long int));
	if (c == 'X')
		count += ft_print_hexup(va_arg(args, unsigned long int));
	return (count);
}
