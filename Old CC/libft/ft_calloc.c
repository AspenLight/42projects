/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/15 20:57:42 by asthibau          #+#    #+#             */
/*   Updated: 2025/05/24 15:59:36 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	char	*ptr;
	size_t	bytes;

	if (nmemb == 0 || size == 0)
	{
		bytes = 0;
	}
	if (size != 0 && nmemb > (INT_MAX / size))
	{
		return (NULL);
	}
	bytes = nmemb * size;
	ptr = malloc(bytes);
	if (ptr == NULL)
	{
		return (NULL);
	}
	ft_bzero(ptr, bytes);
	return (ptr);
}
