/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base2.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/25 16:21:26 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/25 16:43:40 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		i++;
	}
	return (i);
}

int	ft_nblen(long nb, int base)
{
	int	len;

	len = 0;
	if (nb <= 0)
	{
		len++;
		if (nb < 0)
			nb = -nb;
	}
	while (nb > 0)
	{
		nb = nb / base;
		len++;
	}
	return (len);
}

int	ft_basecheck(char *base)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	if (!base[0] || !base[1])
		return (0);
	while (base[i])
	{
		if (base[i] == '+' || base[i] == '-'
			|| (base[i] >= 9 && base[i] <= 13) || base[i] == 32)
			return (0);
		j = i + 1;
		while (base[j])
		{
			if (base[i] == base[j])
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}
