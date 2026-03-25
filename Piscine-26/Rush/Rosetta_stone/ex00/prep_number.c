/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   prep_number.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tlusson <tlusson@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 18:29:37 by tlusson           #+#    #+#             */
/*   Updated: 2026/03/22 00:45:17 by julhuang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>
#include "rush_header.h"

int	number_len(char *str)
{
	int	count;

	count = 0;
	while (*str)
	{
		count++;
		str++;
	}
	return (count);
}

int	valid_number(char *number)
{
	int	count;

	count = 0;
	while (*number)
	{
		if (*number < '0' || *number > '9')
			return (0);
		if (count || *number > '0')
			count++;
		if (count > 39)
			return (0);
		number++;
	}
	return (1);
}

int	write_dict_n(int n)
{
	int		dict;
	char	c[1];
	int		out;
	int		i;

	dict = open(".sort.dict", O_RDONLY);
	if (dict == -1)
		return (1);
	i = 0;
	out = 1;
	while (i <= n && out)
	{
		out = read(dict, c, 1);
		if (out == -1)
			return (1);
		if (out == 0 || *c == '\n')
			i++;
		else if (i == n)
			write(1, c, 1);
	}
	if (close(dict) == -1)
		return (1);
	return (0);
}

char	*true_pointer(char *number)
{
	if (!valid_number(number) || *number == '\0')
		return (0);
	while (*number == '0')
		number++;
	if (!*number)
		write_dict_n(0);
	return (number);
}
