/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/12 20:20:36 by asthibau          #+#    #+#             */
/*   Updated: 2025/08/27 20:32:31 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include <stdio.h>
# include "libft/libft.h"

int	ft_printf(const char *format, ...);
int	check_percent(char c, int count, va_list args);

int	ft_print_char(char c);
int	ft_print_str(char *str);
int	ft_print_ptr(unsigned long int ptr);
int	ft_print_dec(int i);
int	ft_print_int(int i);
int	ft_print_uns(unsigned int i);
int	ft_print_hex(unsigned int i);
int	ft_print_hexup(unsigned int i);

#endif
