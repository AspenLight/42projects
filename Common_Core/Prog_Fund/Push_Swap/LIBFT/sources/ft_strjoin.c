/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 17:05:08 by nmak              #+#    #+#             */
/*   Updated: 2026/05/04 03:39:13 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	reslen;
	char	*res;

	if (!s1 || !s2)
		return (NULL);
	reslen = ft_strlen(s1) + ft_strlen(s2);
	res = malloc(reslen + 1);
	if (!res)
		return (NULL);
	ft_strlcpy(res, s1, ft_strlen(s1) + 1);
	ft_strlcat(res, s2, reslen + 1);
	return (res);
}
