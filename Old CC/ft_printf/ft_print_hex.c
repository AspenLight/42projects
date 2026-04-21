/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hex.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:10:12 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:29:46 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_hex(unsigned int i)
{
	int	count;

	count = 0;
	if (i > 16)
		count += ft_print_hex(i / 16);
	count += ft_print_char("0123456789abcdef"[i % 16]);
	return (count);
}
