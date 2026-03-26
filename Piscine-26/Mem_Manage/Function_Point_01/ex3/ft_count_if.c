/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_if.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 16:47:30 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/23 19:02:27 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_count_if(char **tab, int length, int (*f)(char *))
{
	int	i;
	int	check;

	i = 0;
	check = 0;
	while (i < length)
	{
		if ((*f)(tab[i]) != 0)
			check++;
		i++;
	}
	return (check);
}
