/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 19:52:05 by nmak              #+#    #+#             */
/*   Updated: 2026/05/04 18:58:14 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_intlen(int n)
{
	int			i;
	long long	nb;

	i = 0;
	nb = n;
	if (nb <= 0)
	{
		nb = -nb;
		i++;
	}
	while (nb > 0)
	{
		nb /= 10;
		i++;
	}
	return (i);
}

char	*ft_itoa(int n)
{
	int			nlen;
	long long	nb;
	char		*res;

	nb = n;
	nlen = ft_intlen(nb);
	res = malloc(nlen + 1);
	if (!res)
		return (NULL);
	if (nb < 0)
	{
		nb = -nb;
		res[0] = '-';
	}
	while (nb > 0)
	{
		res[--nlen] = (nb % 10) + '0';
		nb /= 10;
	}
	if (n == 0)
		res[0] = '0';
	res[ft_intlen(n)] = '\0';
	return (res);
}

// int	main()
// {
// 	printf("%d\n", ft_intlen(0));
// 	printf("%s\n", ft_itoa(0));
// }