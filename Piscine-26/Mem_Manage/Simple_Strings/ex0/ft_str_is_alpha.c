/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 16:57:38 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/18 17:02:56 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_alpha(char *str)
{
	int	i;
	int	result;

	i = 0;
	result = 1;
	while (str[i])
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			i++;
		else if (str[i] >= 'a' && str[i] <= 'z')
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
	int	result = ft_str_is_alpha(str);
	printf("%i\n", result);
	return (0);
}
*/
