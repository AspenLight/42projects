/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 21:00:01 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:01:36 by asthibau         ###   ########.fr       */
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
	while (str[i] && i < n)
	{
		while (str[i + j] == sub[j] && str[i + j] && (i + j < n))
		{
			j++;
			if (sub[j] == '\0')
				return ((char *) str + i);
		}
		i++;
		j = 0;
	}
	return (0);
}
