/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/25 17:24:41 by aspthiba          #+#    #+#             */
/*   Updated: 2026/05/12 18:52:55 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int	ft_printf(const char *format, ...);
int	check_percent(char c, int count, va_list args);

int	ft_print_char(char c);
int	ft_print_str(char *str);
int	ft_print_ptr(unsigned long int ptr);
int	ft_print_int(int i);
int	ft_print_uns(unsigned int i);
int	ft_count_uns(unsigned int i);
int	ft_print_hex(unsigned long int i);
int	ft_print_hexup(unsigned long int i);

#endif
