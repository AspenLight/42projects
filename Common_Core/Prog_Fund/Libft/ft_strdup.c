/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:43 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 19:44:17 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t	i;
	size_t	srclen;
	char	*dest;

	i = 0;
	srclen = ft_strlen(s);
	dest = malloc((srclen + 1) * sizeof(char));
	if (!dest)
		return (NULL);
	while (s[i])
	{
		dest[i] = s[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}
/*
char *ft_strdup(const char *s)
This function copies given string 's' into
a new string which is created and allocated within
the function.
Returns the new string 'dest'.
*/
