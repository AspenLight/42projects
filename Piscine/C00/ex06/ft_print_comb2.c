/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/20 18:28:38 by asthibau          #+#    #+#             */
/*   Updated: 2025/02/21 12:12:19 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_print_comb_cont(int a, int b, int c, int d)
{
	while (d <= '9')
	{
		if (a != c || b != d)
		{
			if (!(a == '9' && b == '9'))
			{
				write (1, &a, 1);
				write (1, &b, 1);
				write (1, " ", 1);
				write (1, &c, 1);
				write (1, &d, 1);
				if (!(a == '9' && b == '8' && c == '9' && d == '9'))
					write(1, ", ", 2);
			}
		}
		d++;
	}
}

void	ft_print_comb2(void)
{
	int	a;
	int	b;
	int	c;
	int	d;

	a = '0';
	c = '0';
	while (a <= '9')
	{
		b = '0';
		while (b <= '9')
		{
			while (c <= '9')
			{
				d = '0';
				ft_print_comb_cont(a, b, c, d);
				c++;
			}
			c = '0';
			b++;
		}
		a++;
	}
}
