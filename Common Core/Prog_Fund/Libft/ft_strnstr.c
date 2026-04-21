/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:02:02 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 19:06:30 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *str, const char *sub, size_t n)
{
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	if (sub[0] == '\0')
		return ((char *)str);
	while (str[i] && (i < n))
	{
		while ((str[i + j] == sub[j]) && str[i + j] && (i + j < n))
		{
			j++;
			if (sub[j] == '\0')
				return ((char *)(str + i));
		}
		i++;
		j = 0;
	}
	return (0);
}
/*
char *ft_strnstr(const char *str, const char *sub, size_t n)
This function finds the first instance of given string 'sub'
within given string 'str'.
Returns a pointer to the first character of 'sub' within 'str',
or 0 if no instance is found.
*/
