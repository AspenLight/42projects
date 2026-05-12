/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/30 01:34:33 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/30 01:39:41 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include "ft_printf.h"

int	main(void)
{
	int i = 3;
	int i2 = 42;
	unsigned int u = 176473;
	char *str = "hello";
	char c = 'c';
	int ptr_cont = 42;
	int *ptr = &ptr_cont;
	int testsize1 = ft_printf("char: %c, dec: %d, hex: %x, hexup: %X, int: %i, ptr: %p, string: %s, unsigned: %u\n", c, i, i2, i2, i2, ptr, str, u);
	int testsize2 = printf("char: %c, dec: %d, hex: %x, hexup: %X, int: %i, ptr: %p, string: %s, unsigned: %u\n", c, i, i2, i2, i2, ptr, str, u);

	printf("size of ft_printf: %d\nsize of printf: %d\n", testsize1, testsize2);
	return (0);
}