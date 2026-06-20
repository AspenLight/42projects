/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/05 18:26:54 by nmak              #+#    #+#             */
/*   Updated: 2026/06/01 04:46:34 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdio.h>
# include <stdarg.h>

int		ft_printf(const char *str, ...);
void	ft_percent(const char *str, va_list list, int *ptr_count);
void	ft_putchar(char c, int *ptr_count);
void	ft_putstr(const char *str, int *ptr_count);
void	ft_putnbr(long int nb, int *ptr_count);
void	ft_u_putnbr(unsigned long nb, int *ptr_count);
void	ft_puthex(unsigned long nb, int *ptr_count, int isupper);

#endif