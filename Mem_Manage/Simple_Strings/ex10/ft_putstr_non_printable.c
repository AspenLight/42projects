/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_non_printable.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 14:51:30 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/19 16:56:45 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_puthex(char c)
{
	char	*tab;

	tab = "0123456789abcdef";
	if (c < 16)
	{
		write(1, &tab[(int)c], 1);
	}
	else if (c >= 16)
	{
		ft_puthex(c / 16);
		ft_puthex(c % 16);
	}
}

void	ft_putstr_non_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] >= 32 && str[i] < 127)
		{
			write(1, &str[i], 1);
			i++;
		}
		else
		{
			write(1, "\\", 1);
			if (str[i] < 16)
				write(1, "0", 1);
			ft_puthex(str[i]);
			i++;
		}
	}
}
/*
int	main(void)
{
	char	str[] = "Hello\tHow are you ?";
	ft_putstr_non_printable(str);
	return (0);
}
*/
