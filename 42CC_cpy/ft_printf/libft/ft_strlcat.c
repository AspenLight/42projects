/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 20:56:33 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:01:17 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t n)
{
	size_t	srclen;
	size_t	dstlen;

	srclen = ft_strlen(src);
	dstlen = ft_strlen(dst);
	if (dstlen >= n)
		dstlen = n;
	if (dstlen == n)
		return (n + srclen);
	if (srclen < (n - dstlen))
		ft_memcpy((dst + dstlen), src, (srclen + 1));
	else
	{
		ft_memcpy((dst + dstlen), src, (n - dstlen - 1));
		dst[n - 1] = '\0';
	}
	return (dstlen + srclen);
}
