/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   write_number.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tlusson <tlusson@learner.42.tech>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 12:27:59 by tlusson           #+#    #+#             */
/*   Updated: 2026/03/22 18:40:17 by tlusson          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h> 
#include <fcntl.h>
#include "rush_header.h"

int	write_trio2(char *trio)
{
	if (trio[1] == '1')
	{
		if (write_dict_n(trio[2] - '0' + 10) == 1)
			return (1);
		return (0);
	}
	if (trio[1] != '0')
		if (write_dict_n(trio[1] - '0' + 18) == 1)
			return (1);
	if ((trio[0] != '0' || trio[1] != '0') && (trio[2] != '0'))
		write(1, " ", 1);
	if (trio[2] != '0')
		if (write_dict_n(trio[2] - '0') == 1)
			return (1);
	return (0);
}

int	write_trio(char *trio)
{
	if (trio[0] == '0' && trio[1] == '0' && trio[2] == '0')
		return (2);
	if (trio[0] != '0')
	{
		if (write_dict_n(trio[0] - '0') == 1)
			return (1);
		write(1, " ", 1);
		if (write_dict_n(28) == 1)
			return (1);
	}
	if (trio[0] != '0' && trio[1] != '0')
		write(1, " ", 1);
	return (write_trio2(trio));
}

int	populate_trio(char *trio, int i, char *number)
{
	int	j;

	j = 0;
	while (j < 3)
	{
		if (i >= 0)
			trio[j] = number[i];
		else
			trio[j] = '0';
		i++;
		j++;
	}
	return (i);
}

int	write_number2(int section, char *trio)
{
	int	out;

	out = write_trio(trio);
	if (out == 1)
		return (1);
	if (out == 0 && section > 1)
	{
		write(1, " ", 1);
		if (write_dict_n(section + 27) == 1)
			return (1);
	}
	return (0);
}

int	write_number(char *number)
{
	char	trio[3];
	int		i;
	int		section;

	number = true_pointer(number);
	if (!number)
		return (write(1, "Error\n", 6) != 0);
	section = number_len(number);
	i = ((3 - (section % 3)) % 3) * -1;
	section = (section - i) / 3;
	while (section > 0)
	{
		i = populate_trio(trio, i, number);
		if (write_number2(section, trio) == 1)
			return (write(1, "Error\n", 6) != 0);
		if ((section > 1) && (number[i] != '0'
				|| number[i + 1] != '0' || number[i + 2] != '0'))
			write(1, " ", 1);
		section--;
	}
	write(1, "\n", 1);
	return (0);
}
