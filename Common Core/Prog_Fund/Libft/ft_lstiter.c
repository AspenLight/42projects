/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:59 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:26:15 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list	*temp;

	temp = lst;
	while (temp)
	{
		f(temp->content);
		temp = temp->next;
	}
}
/*
void ft_lstiter(t_list *lst, void (*f)(void *))
This function uses the custom data structure t_list, found in libft.h
This function iterates through the given list 'lst'
and applies the given function 'f' to the content of each node.
Returns nothing.
*/
