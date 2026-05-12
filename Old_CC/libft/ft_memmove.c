/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 20:54:52 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 16:00:45 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*ptrdest;
	const unsigned char	*ptrsrc;
	size_t				i;

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
