/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush01.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nben-ama <nben-ama@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 10:57:24 by nben-ama          #+#    #+#             */
/*   Updated: 2026/03/15 19:15:29 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

int	check_input(char *str)
{
	int	views[16];
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (str[i] && count < 16)
	{
		if (str[i] < '1' || str[i] > '4')
			return (0);
		views[count++] = str[i] - '0';
		i++;
		if (count < 16 && str[i] != ' ')
			return (0);
		if (count < 16)
			i++;
	}
	return (count == 16 && str[i] == '\0');
}

void	print_solution(int **grid)
{
	int		row;
	int		col;
	char	c;

	row = 0;
	while (row < 4)
	{
		col = 0;
		while (col < 4)
		{
			c = '0' + grid[row][col];
			write(1, &c, 1);
			if (col < 3)
				write(1, " ", 1);
			col++;
		}
		write(1, "\n", 1);
		row++;
	}
}

int	is_valid_placement(int **grid, int pos, int num)
{
	int	i;
	int	row;
	int	col;

	row = pos / 4;
	col = pos % 4;
	i = 0;
	while (i < col)
	{
		if (grid[row][i] == num)
			return (0);
		i++;
	}
	i = 0;
	while (i < row)
	{
		if (grid[i][col] == num)
			return (0);
		i++;
	}
	return (1);
}

int	fill(int **grid, int pos)
{
	int	row;
	int	col;
	int	num;

	if (pos == 16)
		return (1);
	row = pos / 4;
	col = pos % 4;
	num = 1;
	while (num < 5)
	{
		if (is_valid_placement(grid, pos, num) == 1)
		{
			grid[row][col] = num;
			if (fill(grid, pos + 1) == 1)
				return (1);
			grid[row][col] = 0;
		}
		num++;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	int	**grid;
	int	i;
	int	j;

	if (argc != 2 || !check_input(argv[1]))
	{
		write(2, "Error\n", 6);
		return (1);
	}
	grid = malloc(4 * sizeof(int *));
	i = 0;
	while (i < 4)
	{
		grid[i++] = malloc(4 * sizeof(int));
	}
	fill(grid, 0);
	print_solution(grid);
	return (0);
}
