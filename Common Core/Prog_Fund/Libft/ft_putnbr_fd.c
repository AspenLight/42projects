/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:01:32 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:48:16 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	c;
	long	nb;

	nb = n;
	if (nb < 0)
	{
		write(fd, '-', 1);
		nb = -nb;
	}
	if (nb > 9)
	{
		ft_putnbr_fd((nb / 10), fd);
	}
	c = (nb % 10) + '0';
	write(fd, &c, 1);
	return ;
}
/*
void ft_putnbr_fd(int c, int fd)
This function writes integer 'n' to the
terminal or file pointed to by file descriptor 'fd'
Returns nothing.
*/
