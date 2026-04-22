/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:02:08 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 19:47:09 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	set_test(const char *set, char c)
{
	int	i;

	i = 0;
	while (set[i])
	{
		if (c == set[i])
			return (1);
		i++;
	}
	return (0);
}

static char	*result_str(const char *s, size_t start, size_t len)
{
	char	*str;
	size_t	i;

	if (len <= 0 || start >= ft_strlen(s))
		return (ft_strdup(""));
	str = ft_calloc((len + 1), sizeof(char));
	if (!str)
		return (NULL);
	i = 0;
	while (i < len)
	{
		str[i] = s[start + i];
		i++;
	}
	return (str);
}

char	*ft_strtrim(const char *s, const char *set)
{
	int	i;
	int	j;

	i = 0;
	j = ft_strlen(s) - 1;
	if (ft_strlen(s) == 0)
		return (ft_strdup(""));
	while (set_test(set, s[i]))
		i++;
	while (set_test(set, s[j]))
		j--;
	return (result_str(s, i, (j - (i - 1))));
}
/*
char *ft_strtrim(const char *s, char const *set))
This function creates a new string containing the contents
of given string 's' with the characters specified in charset 'set'
removed from the beginning and end of 's'.
Returns the newly created string, or NULL in case of error.
*/
