/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/03 14:26:57 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/03 14:38:31 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcat(char *dest, char *str)
{
	int	i;
	int	n;

	i = 0;
	n = 0;
	while (dest[i])
	{
		i++;
	}
	while (str[n])
	{
		dest[i] = str[n];
		n++;
		i++;
	}
	dest[i] = '\0';
	return (dest);
}
/*
#include <stdio.h>
int	main(void)
{
	char	s1[] = "bat";
	char	s2[] = "cat";

	printf("%s\n", ft_strcat(s1, s2));
	return (0);
}
*/
