/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:47 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:26:25 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*last;

	if (*lst == NULL)
	{
		*lst = new;
		return ;
	}
	if (lst == NULL || new == NULL)
		return ;
	last = ft_lstlast(*lst);
	if (!last)
		*lst = new;
	last->next = new;
}
/*
void ft_lstadd_back(t_list **lst, t_list *new)
This function uses the custom data structure t_list, found in libft.h
This function takes an existing list and a new node,
and adds the new node to the end of the existing list.
Returns nothing.
*/
