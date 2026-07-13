/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/24 11:12:09 by asthibau          #+#    #+#             */
/*   Updated: 2025/04/24 12:22:55 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);

void	ft_print_data(char **argv)
{
	int	i;
	int	k;

	i = 1;
	k = 0;
	while (argv[i])
	{
		while (argv[i][k])
		{
			ft_putchar(argv[i][k]);
			k++;
		}
		write(1, "\n", 1);
		k = 0;
		i++;
	}
}

void	ft_strcmp(char **argv, int j, int k)
{
	char	*temp;

	while (argv[j][k] == argv[j + 1][k]
		&& argv[j][k] != '\0' && argv[j + 1][k] != '\0')
	{
		k++;
	}
	if ((argv[j][k] - argv[j + 1][k]) < 0)
		k = 0;
	else
	{
		k = 0;
		temp = argv[j + 1];
		argv[j + 1] = argv[j];
		argv[j] = temp;
	}
}

int	main(int argc, char **argv)
{
	int		i;
	int		j;
	int		k;

	i = 1;
	j = 1;
	k = 0;
	if (argc == 1)
		return (0);
	while (argv[i] && i < argc)
	{
		while (argv[j] && j < (argc - 1))
		{
			ft_strcmp(argv, j, k);
			j++;
		}
		j = 1;
		i++;
	}
	ft_print_data(argv);
	return (0);
}
