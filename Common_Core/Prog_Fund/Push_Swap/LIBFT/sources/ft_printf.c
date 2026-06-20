/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/05 18:06:59 by nmak              #+#    #+#             */
/*   Updated: 2026/05/24 00:09:46 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putptr(void *ptr, int *ptr_count)
{
	if (!ptr)
	{
		ft_putstr("(nil)", ptr_count);
	}
	else
	{
		ft_putstr("0x", ptr_count);
		ft_puthex((unsigned long)ptr, ptr_count, 0);
	}
}

void	ft_percent(const char *str, va_list list, int *ptr_count)
{
	if (*str == 'c')
		ft_putchar((char)va_arg(list, int), ptr_count);
	else if (*str == 's')
		ft_putstr((char *)va_arg(list, char *), ptr_count);
	else if (*str == 'p')
		ft_putptr((void *)va_arg(list, void *), ptr_count);
	else if (*str == 'd' || *str == 'i')
		ft_putnbr((long int)va_arg(list, int), ptr_count);
	else if (*str == 'u')
		ft_u_putnbr((unsigned long)va_arg(list, unsigned int), ptr_count);
	else if (*str == 'x')
		ft_puthex((unsigned long)va_arg(list, unsigned int), ptr_count, 0);
	else if (*str == 'X')
		ft_puthex((unsigned long)va_arg(list, unsigned int), ptr_count, 1);
	else if (*str == '%')
		ft_putchar(*str, ptr_count);
	str++;
}

int	ft_printf(const char *str, ...)
{
	int		count;
	va_list	list;

	count = 0;
	va_start(list, str);
	if (!str)
		return (-1);
	while (*str)
	{
		if (str[1] && *str == '%')
			ft_percent(++str, list, &count);
		else
			ft_putchar(*str, &count);
		str++;
	}
	va_end(list);
	return (count);
}

// int	main(void)
// {
// 	char	str1[] = "Oui oui on printf ici\n%x";
// 	char	str2[] = "[Ceci est une string]";
// 	char	c = '7';
// 	int	nb = -1234567899;
// 	int	*ptr = NULL;
// 	size_t uni = 12345678912345678;

// 	printf("\n---\n");
// 	printf("\nprintf   %d\n", printf(str1, 9223372036854775807));
// 	printf("---\n");
// 	printf("\nft_printf %d\n", ft_printf(str1, 9223372036854775807));
// 	printf("---\n\n");
// 	return (0);
// }
