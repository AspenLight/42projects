/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   file_parsing.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: julhuang <julhuang@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 22:16:51 by julhuang          #+#    #+#             */
/*   Updated: 2026/03/22 19:21:17 by julhuang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>
#include "rush_header.h"

int	get_to_value(int src_fd)
{
	char	c[1];
	int		dst_fd;

	dst_fd = open(".index.dict", O_WRONLY | O_APPEND);
	if (dst_fd == -1)
		return ((write(1, "Error\n", 6)) != 0);
	write(dst_fd, c, 1);
	close(dst_fd);
	if (*c == ' ')
	{
		while (read(src_fd, c, 1) > 0 && *c != ' ')
		{
		}
	}
	return (0);
}

int	file_parsing_loop(char *path, int src_fd)
{
	int	nb_line;
	int	out;

	nb_line = get_nb_line(path);
	while (nb_line > 0)
	{
		out = write_key(src_fd);
		if (out == 1)
			return (1);
		if (out == 2)
		{
			nb_line--;
			continue ;
		}
		if (get_to_value(src_fd) == 1 || write_value(src_fd) == 1)
			return (1);
		nb_line--;
	}
	return (0);
}

int	file_parsing(char *path)
{
	int	src_fd;
	int	dst_fd;

	src_fd = open(path, O_RDONLY);
	dst_fd = open(".index.dict", O_CREAT | O_TRUNC | O_WRONLY, S_IRWXU);
	if (src_fd == -1 || dst_fd == -1)
		return ((write(1, "Error\n", 6)) != 0);
	close(dst_fd);
	if (file_parsing_loop(path, src_fd) == 1)
	{
		close(src_fd);
		return (1);
	}
	close(src_fd);
	return (0);
}
