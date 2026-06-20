/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   op_swap.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 02:36:40 by nmak              #+#    #+#             */
/*   Updated: 2026/06/04 02:16:18 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Swap the first two elements at the top of the stack
//	Do nothing if there is only one or no elements
void	swap(t_stack *stack)
{
	int	temp;

	if (!stack || !stack->next)
		return ;
	temp = stack->nb;
	stack->nb = stack->next->nb;
	stack->next->nb = temp;
}

//	Print "sa" followed by a newline and swap the stack
void	sa(t_stack *stack_a, int **actions)
{
	ft_printf("sa\n");
	swap(stack_a);
	(*actions)[0]++;
}

//	Print "sb" followed by a newline and swap the stack
void	sb(t_stack *stack_b, int **actions)
{
	ft_printf("sb\n");
	swap(stack_b);
	(*actions)[1]++;
}

//	Print "ss" followed by a newline and swap the stacks
void	ss(t_stack *stack_a, t_stack *stack_b, int **actions)
{
	ft_printf("ss\n");
	swap(stack_a);
	swap(stack_b);
	(*actions)[2]++;
}
