/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   file_parsing_write.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: julhuang <julhuang@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/22 17:27:47 by julhuang          #+#    #+#             */
/*   Updated: 2026/03/22 19:26:21 by julhuang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>
#include "rush_header.h"

int	go_to_semi_colon(int src_fd, char *c)
{
	if (*c != ':')
	{
		while (read(src_fd, c, 1) > 0 && *c != ':' && *c != '\n')
		{
		}
	}
	if (*c != ':')
		return (2);
	return (0);
}

int	write_key(int src_fd)
{
	char	c[1];
	int		dst_fd;

	while (read(src_fd, c, 1) > 0 && is_space(*c) == 1)
	{
	}
	if (*c == '+')
		read(src_fd, c, 1);
	else if (!(*c >= '0' && *c <= '9'))
	{
		if (*c != '\n')
			go_next_line(src_fd);
		return (2);
	}
	dst_fd = open(".index.dict", O_WRONLY | O_APPEND);
	if (dst_fd == -1)
		return ((write(1, "Error\n", 6)) != 0);
	write(dst_fd, c, 1);
	while ((read(src_fd, c, 1) > 0)
		&& (*c >= '0' && *c <= '9'))
		write(dst_fd, c, 1);
	close(dst_fd);
	return (go_to_semi_colon(src_fd, c));
}

int	write_value(int src_fd)
{
	char	c[1];
	int		dst_fd;

	while (read(src_fd, c, 1) > 0 && *c == ' ')
	{
	}
	dst_fd = open(".index.dict", O_WRONLY | O_APPEND);
	if (dst_fd == -1)
		return ((write(1, "Error\n", 6)) != 0);
	if (*c >= ' ' && *c <= '~')
		write(dst_fd, c, 1);
	while (read(src_fd, c, 1) > 0 && *c != '\n')
	{
		if (*c == ' ' && get_write_nb_space(src_fd) == -1ull)
			break ;
		else if (*c >= ' ' && *c <= '~')
			write(dst_fd, c, 1);
	}
	write(dst_fd, "\n", 1);
	close(dst_fd);
	return (0);
}
