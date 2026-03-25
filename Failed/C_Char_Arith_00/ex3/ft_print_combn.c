/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_combn.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/08 17:11:25 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/11 16:23:45 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_logic(char i, char *list, int position, int size)
{
	while (i <= '9' - position)
	{
		list[size - position] = i;
		if (position == 0)
		{
			write(1, list, size + 1);
			if (list[0] != '9' - size)
				write (1, ", ", 2);
		}
		else
			ft_logic((i + 1), list, (position - 1), size);
		i++;
	}
}

void	ft_print_combn(int n)
{
	char	list[10];

	if (n > 0 && n < 10)
	{
		ft_logic('0', list, (n - 1), (n - 1));
	}
}
/*
int	main(void)
{
	ft_print_combn(3);
}
*/
