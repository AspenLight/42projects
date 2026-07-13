/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/27 16:09:00 by asthibau          #+#    #+#             */
/*   Updated: 2025/02/27 16:13:00 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_numeric(char *str)
{
	int	i;

	i = 0;
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
		{
			return (0);
		}
		i++;
	}
	return (1);
}
/*
#include <stdio.h>
int     main(void)
{
        char    str[] = "19011A9";
        int     a;

        a = ft_str_is_numeric( str);
        ft_str_is_numeric( str);

        printf("%d", a);
        return (0);
}
*/
