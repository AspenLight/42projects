/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 11:00:50 by aspthiba          #+#    #+#             */
/*   Updated: 2026/04/21 18:26:18 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	new->next = *lst;
	*lst = new;
}
/*
void ft_lstadd_front(t_list **lst, t_list *new)
This function uses the custom data structure t_list, found in libft.h
This function takes an existing list and a new node,
and adds the new node to the beginning of the existing list.
Returns nothing.
*/
