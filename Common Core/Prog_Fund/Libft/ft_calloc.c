/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:22 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:26:33 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_calloc(size_t nitems, size_t size)
{
	char	*ptr;
	size_t	bytes;

	if (nitems == 0 || size == 0)
	{
		bytes = 0;
	}
	if (size != 0 && nitems > (INT_MAX / size))
	{
		return (NULL);
	}
	bytes = nitems * size;
	ptr = malloc(bytes);
	if (!ptr)
	{
		return (NULL);
	}
	ft_bzero(ptr, bytes);
	return (ptr);
}
/*
void ft_calloc(size_t nitems, size_t size)
This function returns a pointer to an allocated memory
created to hold 'nitems' items of 'size' size,
with all bytes in storage initialized as 0.
*/
