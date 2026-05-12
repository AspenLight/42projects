/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cedurget <cedurget@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/15 14:53:41 by cedurget          #+#    #+#             */
/*   Updated: 2026/03/15 19:17:29 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	check_row_l(int *row, int max, int visible)
{
	int	i;

	i = 0;
	while (i < 4)
	{
		if (row[i] > max)
		{
			max = row[i];
			visible++;
		}
		i++;
	}
	return (visible);
}

int	check_row_r(int *row, int max, int visible)
{
	int	i;

	i = 4;
	while (i > 0)
	{
		if (row[i] > max)
		{
			max = row[i];
			visible++;
		}
		i--;
	}
	return (visible);
}

int	check_col_u(int **grid, int col, int max, int visible)
{
	int	i;

	i = 0;
	while (i < 4)
	{
		if (grid[i][col] > max)
		{
			max = grid[i][col];
			visible++;
		}
		i++;
	}
	return (visible);
}

int	check_col_d(int **grid, int max, int visible)
{
	int	i;

	i = 4;
	while (i > 0)
	{
		if (grid[i][col] > max)
		{
			max = grid[i][col];
			visible++;
		}
		i--;
	}
	return (visible);
}

int	count_visible_buildings(int **grid, int *views)
{
	int	i;

	i = 0;
	while (i < 4)
	{
		if (check_col_u(grid, i, 0, 0) != views[i])
			swap_col_u();
		if (check_col_d(grid, i, 0, 0) != views[i + 4])
			swap_col_d();
		if (check_row_l(grid[i], 0, 0) != views[i + 8])
			swap_row_l();
		if (check_row_r(grid[i], 0, 0) != views[i + 12])
			swap_row_r();
		i++;
	}
	return (visible);
}
