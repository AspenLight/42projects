/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/03 14:26:57 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/04 14:42:52 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncat(char *dest, char *str, unsigned int nb)
{
	unsigned int	i;
	unsigned int	n;

	i = 0;
	n = 0;
	while (dest[n])
		n++;
	while (str[i] && i < nb)
	{
		dest[n] = str[i];
		i++;
		n++;
	}
	dest[n] = '\0';
	return (dest);
}
/*
#include <stdio.h>
int	main(void)
{
	char	s1[] = "bat";
	char	s2[] = "cat";
	unsigned int	nb = 2;

	printf("%s\n", ft_strncat(s1, s2, nb));
	return (0);
}
*/
