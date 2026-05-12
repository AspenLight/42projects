/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 17:08:10 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/19 14:50:32 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_printable(char *str)
{
	int	i;
	int	result;

	i = 0;
	result = 1;
	while (str[i])
	{
		if (str[i] >= 32 && str[i] < 127)
			i++;
		else
		{
			result = 0;
			i++;
		}
	}
	return (result);
}
/*
#include <stdio.h>
int	main(void)
{
	char	str[] = "Testing theCode";
	int	result = ft_str_is_printable(str);
	printf("%i\n", result);
	return (0);
}
*/
