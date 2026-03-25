/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/18 17:20:27 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/19 16:10:41 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_isalphanum(char str)
{
	int	result;

	if (str >= 'A' && str <= 'Z')
		result = 1;
	else if (str >= 'a' && str <= 'z')
		result = 1;
	else if (str >= '0' && str <= '9')
		result = 1;
	else
		result = 0;
	return (result);
}

void	ft_charupcase(char *str, int i)
{
	if (str[i] >= 'a' && str[i] <= 'z')
		str[i] = str[i] - 32;
}

void	ft_charlowcase(char *str, int i)
{
	if (str[i] >= 'A' && str[i] <= 'Z')
		str[i] = str[i] + 32;
}

char	*ft_strcapitalize(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (i == 0 && ft_isalphanum(str[i]) == 1)
			ft_charupcase(str, i);
		else if (ft_isalphanum(str[i]) == 1 && ft_isalphanum(str[i - 1]) == 0)
			ft_charupcase(str, i);
		else
			ft_charlowcase(str, i);
		i++;
	}
	return (str);
}
/*
#include <stdio.h>
int	main(void)
{
	char	str1[] = "hello, how are you doing?";
	char	str2[] = "  42words forty-two; fifty+and+one";
	printf("%s%s\n", ft_strcapitalize(str1), ft_strcapitalize(str2));
	return (0);
}
*/
