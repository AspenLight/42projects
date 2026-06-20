/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   input_checker.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 21:26:46 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 07:36:20 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return 1, 2, 3 or 4 for each matching option, plus 10 if bench
//	0 if none
int	valid_option(char **argv)
{
	int	i;
	int	option;

	i = 1;
	option = 0;
	while (argv[i] && i <= 2)
	{
		if (!ft_strncmp(argv[i], "--bench", ft_strlen("--bench")))
			option += 10;
		else if (!ft_strncmp(argv[i], "--simple", ft_strlen("--simple")))
			option += 1;
		else if (!ft_strncmp(argv[i], "--medium", ft_strlen("--medium")))
			option += 2;
		else if (!ft_strncmp(argv[i], "--complex", ft_strlen("--complex")))
			option += 3;
		else if (!ft_strncmp(argv[i], "--adaptive", ft_strlen("--adaptive")))
			option += 4;
		i++;
	}
	return (option);
}

//	Return 1 if the arguments are numbers, 0 otherwise
int	valid_nb(char **argv)
{
	int	i;
	int	j;

	if (!argv || !argv[0])
		return (0);
	i = 1;
	while (argv[i])
	{
		j = 0;
		if (argv[i][j] && ft_isdigit(argv[i][j + 1]) &&
		(argv[i][j] == '+' || argv[i][j] == '-'))
			j++;
		while (argv[i][j])
		{
			if (!ft_isdigit(argv[i][j]))
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

//	Return 1 if the arguments are integers, 0 otherwise
int	valid_int(char **argv)
{
	int		i;
	int		error;

	if (!argv || !argv[0])
		return (0);
	i = 1;
	error = 0;
	while (argv[i])
	{
		atoi_error(argv[i], &error);
		if (error)
			return (0);
		i++;
	}
	return (1);
}

//	Return 1 if the arguments contains duplicates, 0 otherwise
int	valid_dup(char **argv)
{
	int	i;
	int	j;

	if (!argv || !argv[1] || !argv[1][0])
		return (0);
	i = 1;
	while (argv[i])
	{
		j = 1;
		while (argv[i + j])
		{
			if (ft_atoi(argv[i]) == ft_atoi(argv[i + j]))
				return (1);
			j++;
		}
		i++;
	}
	return (0);
}

//	Return 1 if the arguments are valid, 0 otherwise
int	valid_input(char **argv)
{
	int	option;

	option = valid_option(++argv);
	if (option)
		argv++;
	if (option >= 10 && option <= 14)
		argv++;
	if (!valid_nb(argv))
		return (0);
	if (!valid_int(argv))
		return (0);
	if (valid_dup(argv))
		return (0);
	return (1);
}
