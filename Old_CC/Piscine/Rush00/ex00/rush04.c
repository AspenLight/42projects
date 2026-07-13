/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tdupin <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/23 10:04:20 by tdupin            #+#    #+#             */
/*   Updated: 2025/02/23 19:13:50 by mfreger          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c);

void	countcolumns(int x, char a, char b, char c)
{
	int	i;

	i = 0;
	while (i < x)
	{
		if (i == 0)
			ft_putchar(a);
		else
		{
			if (i == x - 1)
				ft_putchar(c);
			else
				ft_putchar(b);
		}
		i++;
	}
	ft_putchar('\n');
}

void	rush(int x, int y)
{
	int	l;

	l = 0;
	if (!(x <= 2147483647) || !(y <= 2147483647))
	{
		return ;
	}
	{
		if (!(x <= 0) && !(y <= 0))
		{
			while (l < y)
			{
				if (l == 0)
					countcolumns(x, 65, 66, 67);
				else
				{
					if (l == y -1)
						countcolumns(x, 67, 66, 65);
					else
						countcolumns(x, 66, 32, 66);
				}
				l++;
			}
		}
	}
}
