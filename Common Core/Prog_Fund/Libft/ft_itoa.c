/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:44 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:16:08 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	int_len(long nb)
{
	int	count;

	count = 0;
	if (nb < 0)
	{
		count++;
		nb = -nb;
	}
	if (nb == 0)
		count++;
	while (nb != 0)
	{
		nb = nb / 10;
		count++;
	}
	return (count);
}

static char	*result_alloc(int len)
{
	char	*temp;

	temp = malloc((len + 1) * sizeof(char));
	if (!temp)
		return (NULL);
	temp[0] = '0';
	return (temp);
}

char	*ft_itoa(int n)
{
	int		len;
	int		i;
	char	*result;
	long	nb;

	nb = n;
	len = int_len(nb);
	result = result_alloc(len);
	if (!result)
		return (NULL);
	if (nb < 0)
		nb = -nb;
	i = len - 1;
	while (nb != 0)
	{
		result[i] = ((nb % 10) + '0');
		nb = nb / 10;
		i--;
	}
	if (n < 0)
		result[0] = '-';
	result[len] = 0;
	return (result);
}
/*
char *ft_itoa(int n)
This function takes an integer n, and converts it to a string.
Returns the resulting string.
*/
