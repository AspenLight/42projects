/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:02:05 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 19:09:08 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	unsigned int	i;
	char			*result;

	i = 0;
	result = NULL;
	while (s[i])
	{
		if (s[i] == (char)c)
			result = (char *)&s[i];
		i++;
	}
	if (s[i] == (char)c)
		result = (char *)&s[i];
	return (result);
}
/*
char *ft_strrchr(const char *s, int c)
This function finds and returns the LAST instance of
given character 'c' within given string 's'
Returns the address of the last instance of 'c' within 's',
or NULL if no instances are found.
*/
