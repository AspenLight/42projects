/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:53 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 19:42:01 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*temp;

	while (*lst)
	{
		temp = (*lst)->next;
		ft_lstdelone(*lst, del);
		*lst = temp;
	}
	free(*lst);
	*lst = NULL;
}
/*
void ft_lstclear(t_list *lst, void (*del)(void *))
This function uses the custom data structure t_list, found in libft.h
This function deletes and frees the
given node 'lst' and all its successors.
This function calls the provided function 'del' to delete the content.
Returns nothing.
*/
