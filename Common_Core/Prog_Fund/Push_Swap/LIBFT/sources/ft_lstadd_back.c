/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/04 17:31:33 by nmak              #+#    #+#             */
/*   Updated: 2026/05/04 18:33:05 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*lst_end;

	if (!*lst)
	{
		*lst = new;
		return ;
	}
	lst_end = ft_lstlast(*lst);
	lst_end->next = new;
}

// int	main(void)
// {
// 	t_list *current = ft_lstnew((void *)"aaa");
// 	ft_lstadd_front(&current, ft_lstnew((void *)"42"));
// 	ft_lstadd_back(&current, ft_lstnew((void *)"endd"));
// 	while (current)
// 	{
// 		printf("%s\n", current->content);
// 		current = current->next;
// 	}
// }