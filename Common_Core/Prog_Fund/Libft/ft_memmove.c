/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:21 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:43:36 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	size_t				i;
	unsigned char		*ptrdest;
	const unsigned char	*ptrsrc;

	if (dest == NULL && src == NULL)
		return (NULL);
	i = 0;
	ptrdest = (unsigned char *)dest;
	ptrsrc = (const unsigned char *)src;
	if (ptrdest > ptrsrc)
		while (n-- > 0)
			ptrdest[n] = ptrsrc[n];
	else
	{
		while (i < n)
		{
			ptrdest[i] = ptrsrc[i];
			i++;
		}
	}
	return (dest);
}
/*
void *ft_memmove(void *dest, const void *src, size_t n)
This function copies 'n' bytes of given string 'src'
into given destination 'dest' using an intermediate buffer.
Returns a pointer to 'dest'.
*/
