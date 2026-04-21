/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:56 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:26:15 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	del(lst->content);
	free(lst);
}
/*
void ft_lstdelone(t_list *lst, void (*del)(void *))
This function uses the custom data structure t_list, found in libft.h
This function deletes and frees the given node 'lst'
This function calls the provided function 'del' to delete the content.
Returns nothing.
*/
