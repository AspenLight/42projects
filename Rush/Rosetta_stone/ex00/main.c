/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: julhuang <julhuang@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/22 17:57:02 by julhuang          #+#    #+#             */
/*   Updated: 2026/03/22 19:06:26 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include "rush_header.h"

int	process(char *path, char *nb)
{
	int	out;

	out = file_parsing(path);
	if (out != 0)
		return (1);
	out = sort_file();
	if (out != 0)
		return (1);
	out = write_number(nb);
	if (out != 0)
		return (1);
	return (0);
}

int	main(int argc, char **argv)
{
	if (argc != 2 && argc != 3)
		return (write(1, "Error\n", 6) != 0);
	if (argc == 2)
		return (process("numbers.dict", argv[1]));
	return (process(argv[1], argv[2]));
}
