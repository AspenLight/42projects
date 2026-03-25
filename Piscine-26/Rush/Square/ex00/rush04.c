/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jvalma <jvalma@learner.42.tech>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/07 10:39:48 by jvalma            #+#    #+#             */
/*   Updated: 2026/03/07 17:23:21 by jvalma           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char c);

int	createlib(char *lib)
{
	lib[0] = 'A';
	lib[1] = 'C';
	lib[2] = 'B';
	lib[3] = ' ';
	return (*lib);
}

void	first(char *lib, int x)
{
	int	j;

	j = 0;
	while (j <= x - 1)
	{
		if (j == 0)
		{
			ft_putchar(lib[0]);
		}
		else if (j == x - 1)
		{
			ft_putchar(lib[1]);
		}
		else
		{
			ft_putchar(lib[2]);
		}
		j++;
	}
}

void	last(char *lib, int x)
{
	int	j;

	j = 0;
	while (j <= x - 1)
	{
		if (j == 0)
		{
			ft_putchar(lib[1]);
		}
		else if (j == x - 1)
		{
			ft_putchar(lib[0]);
		}
		else
		{
			ft_putchar(lib[2]);
		}
		j++;
	}
}

void	middle(char *lib, int x)
{
	int	j;

	j = 0;
	while (j <= x - 1)
	{
		if (j == 0 || j == x - 1)
		{
			ft_putchar(lib[2]);
		}
		else
		{
			ft_putchar(lib[3]);
		}
		j++;
	}
}

void	rush(int x, int y)
{
	int		i;
	char	lib[4];

	createlib(lib);
	if (x > 0 && y > 0)
	{
		i = 1;
		while (i <= y)
		{
			if (i == 1)
			{
				first(lib, x);
			}
			else if (i == y)
			{
				last(lib, x);
			}
			else
			{
				middle(lib, x);
			}
			ft_putchar('\n');
			i++;
		}
	}
}
