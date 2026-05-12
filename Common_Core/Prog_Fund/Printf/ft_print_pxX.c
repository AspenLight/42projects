/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_pxX.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/12 18:32:40 by aspthiba          #+#    #+#             */
/*   Updated: 2026/05/12 18:52:57 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_hex(unsigned long int i)
{
	int	count;

	count = 0;
	if (i > 16)
		count += ft_print_hex(i / 16);
	count += ft_print_char("0123456789abcdef"[i % 16]);
	return (count);
}

int	ft_print_hexup(unsigned long int i)
{
	int	count;

	count = 0;
	if (i > 16)
		count += ft_print_hexup(i / 16);
	count += ft_print_char("0123456789ABCDEF"[i % 16]);
	return (count);
}

int	ft_print_ptr(unsigned long int ptr)
{
	int	count;

	count = 0;
	if (!ptr)
	{
		count += ft_print_str("(nil)");
		return (count);
	}
	else
	{
		count += ft_print_str("0x");
		count += ft_print_hex(ptr);
	}
	return (count);
}
