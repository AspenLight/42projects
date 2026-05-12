/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   file_parsing_utils.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: julhuang <julhuang@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/21 23:33:49 by julhuang          #+#    #+#             */
/*   Updated: 2026/03/22 19:12:04 by julhuang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>

int	is_space(char c)
{
	if (c != ' ' && c != '\f' && c != '\r'
		&& c != '\t' && c != '\v')
		return (0);
	return (1);
}

void	go_next_line(int src_fd)
{
	char	c[1];

	while (read(src_fd, c, 1) > 0 && *c != '\n')
	{
	}
}

int	get_nb_line(char *path)
{
	char	c[1];
	int		src_fd;
	int		count;

	count = 1;
	src_fd = open(path, O_RDONLY);
	while (read(src_fd, c, 1) > 0)
	{
		if (*c == '\n')
			count++;
	}
	return (count);
}

int	write_spaces(unsigned long long nb_space)
{
	int	dst_fd;

	dst_fd = open(".index.dict", O_APPEND | O_WRONLY);
	if (dst_fd == -1)
		return (-((write(1, "Error\n", 6)) != 0));
	while (nb_space > 0)
	{
		write(dst_fd, " ", 1);
		nb_space--;
	}
	close(dst_fd);
	return (0);
}

unsigned long long	get_write_nb_space(int src_fd)
{
	unsigned long long	nb_space;
	char				c[1];
	int					dst_fd;

	nb_space = 1;
	while (read(src_fd, c, 1) > 0 && *c == ' ')
		nb_space++;
	if (*c == '\n')
		return (-1);
	write_spaces(nb_space);
	dst_fd = open(".index.dict", O_APPEND | O_WRONLY);
	if (dst_fd == -1)
		return (-((write(1, "Error\n", 6)) != 0));
	write(dst_fd, c, 1);
	close(dst_fd);
	return (nb_space);
}
