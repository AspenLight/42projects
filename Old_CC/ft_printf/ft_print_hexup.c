/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hexup.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 18:10:25 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:30:34 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_hexup(unsigned int i)
{
	int	count;

	count = 0;
	if (i > 16)
		count += ft_print_hexup(i / 16);
	count += ft_print_char("0123456789ABCDEF"[i % 16]);
	return (count);
}
