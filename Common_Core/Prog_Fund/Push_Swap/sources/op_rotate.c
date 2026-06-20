/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_rotate.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/04 03:18:00 by nmak              #+#    #+#             */
/*   Updated: 2026/06/07 10:22:06 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Shift up all elements of the stack by one
//	The first element becomes the last one
void	rotate(t_stack **stack)
{
	t_stack	*current;
	t_stack	*tail;

	current = *stack;
	while (current->next)
		current = current->next;
	tail = *stack;
	current->next = tail;
	*stack = (*stack)->next;
	tail->next = NULL;
}

//	Print "ra" followed by a newline
//	Rotate the stack a
void	ra(t_stack **stack_a, int **actions)
{
	ft_printf("ra\n");
	rotate(stack_a);
	(*actions)[5]++;
}

//	Print "rb" followed by a newline
//	Rotate the stack b
void	rb(t_stack **stack_b, int **actions)
{
	ft_printf("rb\n");
	rotate(stack_b);
	(*actions)[6]++;
}

//	Print "rr" followed by a newline
//	ra and rb at the same time
void	rr(t_stack **stack_a, t_stack **stack_b, int **actions)
{
	ft_printf("rr\n");
	rotate(stack_a);
	rotate(stack_b);
	(*actions)[7]++;
}
