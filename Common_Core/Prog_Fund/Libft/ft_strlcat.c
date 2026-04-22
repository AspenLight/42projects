/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:50 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:57:55 by aspthiba         ###   ########.fr       */
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
/*
size_t ft_strlcat(char *dst, const char *src, size_t n)
This function concatenates given string 'src' onto
given string 'dst' until the total length of 'dst' is equal to 'n'.
Returns the combined length of dst and src. 
*/
