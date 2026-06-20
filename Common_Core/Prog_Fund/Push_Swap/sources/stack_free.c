/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_free.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/05 03:58:47 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 06:33:13 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Free the stack
void	freestack(t_stack *stack)
{
	t_stack	*temp;

	while (stack)
	{
		temp = stack;
		stack = stack->next;
		free (temp);
	}
}

void	free_all(t_stack **a, t_stack **b, int **actions)
{
	if (*a)
		freestack(*a);
	if (*b)
		freestack(*b);
	if (*actions)
		free (*actions);
}
