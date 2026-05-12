/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 17:04:01 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 17:04:03 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_numeric(char *str)
{
	int	i;
	int	result;

	i = 0;
	result = 1;
	while (str[i])
	{
		if (str[i] >= '0' && str[i] <= '9')
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
	int	result = ft_str_is_numeric(str);
	printf("%i\n", result);
	return (0);
}
*/
