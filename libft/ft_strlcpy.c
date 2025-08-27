/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 20:56:39 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:01:20 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t n)
{
	size_t	srclen;

	srclen = ft_strlen(src);
	if (n > (srclen + 1))
		ft_memcpy(dst, src, (srclen + 1));
	else if (n != 0)
	{
		ft_memcpy(dst, src, (n - 1));
		dst[n - 1] = '\0';
	}
	return (srclen);
}
