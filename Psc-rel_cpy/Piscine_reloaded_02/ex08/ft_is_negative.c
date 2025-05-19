/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/23 14:56:11 by asthibau          #+#    #+#             */
/*   Updated: 2025/04/25 17:55:07 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char sign);

void	ft_is_negative(int n)
{
	char	sign;

	sign = '0';
	if (n >= 0)
	{
		sign = 'P';
	}
	else
	{
		sign = 'N';
	}
	ft_putchar(sign);
}
