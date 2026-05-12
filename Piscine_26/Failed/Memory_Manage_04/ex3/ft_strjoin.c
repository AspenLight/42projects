/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 19:07:39 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/26 17:18:17 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		i++;
	}
	return (i);
}

char	*ft_alloc_result(char *result, char *str)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (result[i])
		i++;
	while (str[j])
	{
		result[i + j] = str[j];
		j++;
	}
	result[i + j] = '\0';
	return (result);
}

int	ft_memsize(int size, char **strs, char *sep)
{
	int	i;
	int	memsize;

	i = 0;
	memsize = 0;
	while (i < size)
	{
		memsize = memsize + ft_strlen(strs[i]);
		if (i < (size - 1))
			memsize = memsize + ft_strlen(sep);
		i++;
	}
	return (memsize);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*result;
	int		i;
	int		mem;

	i = 0;
	if (size == 0)
	{
		result = malloc(1);
		if (result)
			result[0] = '\0';
		return (result);
	}
	mem = ft_memsize(size, strs, sep);
	result = malloc((mem + 1) * sizeof(char));
	if (!result)
		return (NULL);
	result[0] = '\0';
	while (i < size)
	{
		ft_alloc_result(result, strs[i]);
		if (i < (size - 1))
			ft_alloc_result(result, sep);
		i++;
	}
	return (result);
}
/*
#include <stdio.h>
int	main(void)
{
		char	*strs[] = {"xyimTcfi"};
		char	*sep = "ZGnzPbDF";
		int		size = 1;
		char	*result = ft_strjoin(size, strs, sep);
		printf("%s\n", result);
		return (0);
}
*/
