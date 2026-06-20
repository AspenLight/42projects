/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_push.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 20:27:09 by nmak              #+#    #+#             */
/*   Updated: 2026/06/07 10:12:50 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Print "pa" followed by a newline
//	Take the first element at the top of b and put it at the top of a
//	Do nothing if b is empty
void	pa(t_stack **stack_a, t_stack **stack_b, int **actions)
{
	t_stack	*temp;

	ft_printf("pa\n");
	if (!*stack_b)
		return ;
	temp = *stack_b;
	*stack_b = (*stack_b)->next;
	stackaddfront(stack_a, temp);
	(*actions)[3]++;
}

//	Print "pb" followed by a newline
//	Take the first element at the top of a and put it at the top of b
//	Do nothing if a is empty
void	pb(t_stack **stack_b, t_stack **stack_a, int **actions)
{
	t_stack	*temp;

	ft_printf("pb\n");
	if (!*stack_a)
		return ;
	temp = *stack_a;
	*stack_a = (*stack_a)->next;
	stackaddfront(stack_b, temp);
	(*actions)[4]++;
}

//	Interchange the first element at the top of a and b
void	pp(t_stack **stack_b, t_stack **stack_a, int **actions)
{
	pa(stack_a, stack_b, actions);
	ra(stack_a, actions);
	pb(stack_b, stack_a, actions);
}
