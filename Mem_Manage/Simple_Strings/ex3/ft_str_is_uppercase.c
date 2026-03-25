/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 17:07:08 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 17:07:33 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_uppercase(char *str)
{
	int	i;
	int	result;

	i = 0;
	result = 1;
	while (str[i])
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
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
	int	result = ft_str_is_uppercase(str);
	printf("%i\n", result);
	return (0);
}
*/
