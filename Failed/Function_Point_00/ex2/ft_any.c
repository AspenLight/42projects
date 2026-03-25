/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_any.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 16:47:09 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/23 17:35:46 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_any(char **tab, int (*f)(char *))
{
	int	i;
	int	check;

	i = 0;
	check = 0;
	while (tab[i])
	{
		check = (*f)(tab[i]);
		if (check != 0)
			return (1);
		i++;
	}
	if (check != 0)
		return (1);
	else
		return (0);
}
