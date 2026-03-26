/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_sort.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 16:47:44 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/23 19:42:22 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_is_sort(int *tab, int length, int (*f)(int, int))
{
	int	i;
	int	is_sorted_asc;
	int	is_sorted_desc;

	i = 1;
	is_sorted_asc = 1;
	is_sorted_desc = 1;
	while (i < length)
	{
		if ((*f)(tab[i - 1], tab[i]) > 0)
			is_sorted_asc = 0;
		i++;
	}
	i = length - 2;
	while (i >= 0)
	{
		if ((*f)(tab[i + 1], tab[i]) > 0)
			is_sorted_desc = 0;
		i--;
	}
	if (is_sorted_asc == 1 || is_sorted_desc == 1)
		return (1);
	else
		return (0);
}
