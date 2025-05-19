/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/10 15:32:13 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/11 18:27:36 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strcat(char *dest, char *str)
{
	int	i;
	int	n;

	i = 0;
	n = 0;
	while (dest[i])
	{
		i++;
	}
	while (str[n])
	{
		dest[i] = str[n];
		n++;
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

char	*ft_strjoin_cont(int i, char *result, char **strs, char *sep)
{
	int	size;

	size = i;
	i = 0;
	while (i <= (size - 1))
	{
		if (i < size - 1)
		{
			ft_strcat(result, strs[i]);
			ft_strcat(result, sep);
		}
		else
			ft_strcat(result, strs[i]);
		i++;
	}
	return (result);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int		i;
	int		fullstrlen;
	char	*result;

	if (size == 0)
	{
		result = malloc(sizeof(char));
		if (result)
			result[0] = '\0';
		return (result);
	}
	i = 0;
	fullstrlen = 0;
	while (i < size)
	{
		fullstrlen += ft_strlen(strs[i]) + ft_strlen(sep);
		i++;
	}
	fullstrlen -= ft_strlen(sep);
	result = malloc(sizeof(char) * (fullstrlen + 1));
	i = size;
	result[0] = '\0';
	return (ft_strjoin_cont(i, result, strs, sep));
}
/*
#include <stdio.h>
int	main(int argc, char **argv)
{
	char	sep[] = ", ";

	printf("%s\n", ft_strjoin(argc, argv, sep));
	return (0);
}
*/
