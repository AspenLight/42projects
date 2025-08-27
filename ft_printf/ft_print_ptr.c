/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/19 17:53:03 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 21:45:18 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_print_ptr(unsigned long int ptr)
{
	int	count;

	count = 0;
	if (ptr > 16)
		count += ft_print_ptr(ptr / 16);
	count += ft_print_char("0123456789abcdef"[ptr % 16]);
	return (count);
}
