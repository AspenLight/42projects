/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 21:00:09 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:01:40 by asthibau         ###   ########.fr       */
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
		{
			result = (char *)&s[i];
		}
		i++;
	}
	if (s[i] == (char)c)
	{
		result = (char *)&s[i];
	}
	return (result);
}
