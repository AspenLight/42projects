/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/04 17:24:22 by nmak              #+#    #+#             */
/*   Updated: 2026/05/04 18:31:45 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (lst);
	while (lst->next)
		lst = lst->next;
	return (lst);
}

// int	main(void)
// {
// 	t_list *current = ft_lstnew((void *)"aaa");
// 	ft_lstadd_front(&current, ft_lstnew((void *)"42"));
// 	ft_lstadd_front(&current, ft_lstnew((void *)"bb"));
// 	ft_lstadd_front(&current, ft_lstnew((void *)"56"));
// 	printf("%s\n", ft_lstlast(current)->content);

// 	while (current)
// 	{
// 		printf("%s\n", current->content);
// 		current = current->next;
// 	}
// }