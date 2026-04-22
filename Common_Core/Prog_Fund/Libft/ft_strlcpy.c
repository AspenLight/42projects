/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:52 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:59:24 by aspthiba         ###   ########.fr       */
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
/*
size_t ft_strlcpy(char *dst, const char *src, size_t n)
This function copies given string 'src' into given string 'dst'
up to 'n' bytes.
Returns the length of src.
*/
