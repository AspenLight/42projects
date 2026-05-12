/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 19:07:39 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/23 21:07:21 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_superlen(int i, char *str)
{
	int	j;

	j = 0;
	while (str[j])
	{
		i++;
		j++;
	}
	return (i);
}

int	ft_alloc_result(int j, char *result, char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		result[j] = str[i];
		j++;
		i++;
	}
	return (j);
}

int	ft_memsize(int size, char **strs, char *sep)
{
	int	i;
	int	memsize;

	i = 0;
	memsize = 0;
	while (i < size)
	{
		memsize = ft_superlen(memsize, strs[i]);
		if (i != (size - 1))
			memsize = ft_superlen(memsize, sep);
		i++;
	}
	memsize = memsize + 1;
	return (memsize);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*result;
	int		i;
	int		j;

	i = 0;
	j = 0;
	result = malloc(ft_memsize(size, strs, sep) * sizeof(char));
	if (size == 0)
		return (result);
	while (i < size)
	{
		j = ft_alloc_result(j, result, strs[i]);
		if (i != (size - 1))
			j = ft_alloc_result(j, result, sep);
		i++;
	}
	return (result);
}
/*
#include <stdio.h>
int	main(void)
{
		char	*strs[] = {"Hello", "this", "is", "a", "test"};
		char	*sep = " ";
		int		size = 5;
		char	*result = ft_strjoin(size, strs, sep);
		printf("%s\n", result);
		return (0);
}
*/
