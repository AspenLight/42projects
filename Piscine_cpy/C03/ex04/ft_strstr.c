/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/03 14:39:17 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/10 17:55:47 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(char *str, char *to_find)
{
	int	i;
	int	n;

	i = 0;
	n = 0;
	if (to_find[i] == '\0')
		return (str);
	while (str[i])
	{
		n = 0;
		while ((str[i + n] == to_find[n]) && (str[i + n] != '\0'))
		{
				n++;
		}
		if (to_find[n] == '\0')
		{
			return (str + i);
		}
		i++;
	}
	return (0);
}
/*
#include <stdio.h>
int	main(void)
{
	char	str[] = "chocolate";
	char	to_find[] = "late";

	printf("str: %s\nft_strstr: %s\n", str, ft_strstr(str, to_find));
	return (0);
}
*/
