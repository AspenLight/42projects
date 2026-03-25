/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: julhuang <julhuang@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/22 14:27:29 by julhuang          #+#    #+#             */
/*   Updated: 2026/03/22 19:14:23 by julhuang         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <fcntl.h>
#include "rush_header.h"

void	write_key_value(int src_fd, int id_key)
{
	char	c[1];
	char	dst_fd;

	dst_fd = open(".sort.dict", O_RDWR);
	while (id_key > 0)
	{
		while (read(dst_fd, c, 1) && *c != '\n')
		{
		}
		id_key--;
	}
	while (read(src_fd, c, 1) && *c != '\n')
		write(dst_fd, c, 1);
	write(dst_fd, "\n", 1);
	close(dst_fd);
}

int	test_current_line(int src_fd, char *key, int id_key)
{
	int		i;
	int		len_key;
	char	c[1];

	i = 0;
	len_key = str_key_len(key);
	while (read(src_fd, c, 1) > 0 && *c != ':')
	{
		if (*c != key[i])
		{
			if (*c != '\n')
				go_to_next_line(src_fd);
			return (-1);
		}
		i++;
	}
	if (*c == ':' && i == len_key)
	{
		write_key_value(src_fd, id_key);
		return (i);
	}
	else if (*c != '\n')
		go_to_next_line(src_fd);
	return (-1);
}

int	get_values(int src_fd, char *key, int id_key)
{
	int	i;
	int	nb_line;
	int	dst_fd;

	dst_fd = open(".sort.dict", O_CREAT | O_WRONLY, S_IRWXU);
	if (dst_fd == -1)
		return (-(write(1, "Error\n", 6) != 0));
	close(dst_fd);
	nb_line = get_nb_line(".index.dict");
	while (nb_line > 0)
	{
		i = test_current_line(src_fd, key, id_key);
		if (i != -1)
			return (i);
		nb_line--;
	}
	return (-(write(1, "Dict Error\n", 11) != 0));
}

int	sort_file(void)
{
	char	*keys;
	int		i;
	int		src_fd;
	int		id_key;
	int		res;

	keys = get_keys();
	i = 0;
	id_key = 0;
	while (keys[i])
	{
		src_fd = open(".index.dict", O_RDONLY);
		res = get_values(src_fd, &keys[i], id_key);
		if (res == -1)
			return (1);
		i += res;
		i++;
		id_key++;
		close(src_fd);
	}
	return (0);
}
