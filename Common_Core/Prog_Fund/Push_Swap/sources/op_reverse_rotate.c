/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_reverse_rotate.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/04 02:16:40 by nmak              #+#    #+#             */
/*   Updated: 2026/06/05 23:32:14 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Shift down all elements of the stack by one
//	The last element becomes the first one
void	reverse_rotate(t_stack **stack)
{
	t_stack	*head;
	t_stack	*tail;

	if (!*stack || !(*stack)->next)
		return ;
	head = *stack;
	while (head->next)
	{
		tail = head;
		head = head->next;
	}
	tail->next = NULL;
	head->next = *stack;
	*stack = head;
}

//	Print "rra" followed by a newline
//	Reverse rotate the stack a
void	rra(t_stack **stack_a, int **actions)
{
	ft_printf("rra\n");
	reverse_rotate(stack_a);
	(*actions)[8]++;
}

//	Print "rrb" followed by a newline
//	Reverse rotate the stack a
void	rrb(t_stack **stack_b, int **actions)
{
	ft_printf("rrb\n");
	reverse_rotate(stack_b);
	(*actions)[9]++;
}

//	Print "rrr" followed by a newline
//	rra and rrb at the same time
void	rrr(t_stack **stack_a, t_stack **stack_b, int **actions)
{
	ft_printf("rrr\n");
	reverse_rotate(stack_a);
	reverse_rotate(stack_b);
	(*actions)[10]++;
}
