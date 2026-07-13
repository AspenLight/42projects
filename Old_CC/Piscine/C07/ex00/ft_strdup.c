/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/06 13:32:07 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/08 13:58:30 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>

char	*ft_strdup(char *src)
{
	char	*copy;
	int		i;

	i = 0;
	while (src[i])
	{
		i++;
	}
	copy = malloc(sizeof(*copy) * (i + 1));
	i = 0;
	while (src[i])
	{
		copy[i] = src[i];
		i++;
	}
	copy[i] = '\0';
	return (copy);
}
/*
#include <stdio.h>
int	main(void)
{
	char	*src = "TestString123";
	printf("%s\n%s\n", src, ft_strdup(src));
	return (0);
}
*/
