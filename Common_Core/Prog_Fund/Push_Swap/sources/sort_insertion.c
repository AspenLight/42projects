/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_insertion.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/04 01:22:54 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 06:29:39 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return the lowest nb of the stack, 0 if empty
int	get_lowest(t_stack **stack)
{
	int		lowest;
	t_stack	*current;

	if (!*stack)
		return (0);
	current = *stack;
	lowest = current->nb;
	while (current)
	{
		if (lowest > current->nb)
			lowest = current->nb;
		current = current->next;
	}
	return (lowest);
}

//	Return the previous number of the current stack position
//	Which is simply the last one
int	get_previous_nb(t_stack **stack)
{
	t_stack	*current;

	current = *stack;
	while (current->next)
		current = current->next;
	return (current->nb);
}

//	Return the distance from nb to the top of the stack
int	get_dist_to_top(t_stack **stack, int nb)
{
	int		i;
	t_stack	*current;

	i = 0;
	current = *stack;
	while (current && nb != current->nb)
	{
		i++;
		current = current->next;
	}
	return (i);
}

//	Rotates optimaly until nb is at the top of the stack a
void	opt_rotates_a(t_stack **stack, int **actions, int nb)
{
	int		i;
	int		size;

	i = get_dist_to_top(stack, nb);
	size = stacksize(*stack);
	if (i < size / 2)
	{
		while (i--)
			ra(stack, actions);
	}
	else if (i >= size / 2)
	{
		while (i++ < size)
			rra(stack, actions);
	}
}

//	Insertion sort !
void	insertionsort(t_stack **stack_a, int **actions, int index)
{
	int	i;
	int	size;

	i = 0;
	size = index - 1;
	while (!is_sorted(*stack_a) && i < size)
	{
		while (i < size && (*stack_a)->nb < (*stack_a)->next->nb)
		{
			ra(stack_a, actions);
			i++;
		}
		if (i < size && (*stack_a)->nb > (*stack_a)->next->nb)
			sa(*stack_a, actions);
		if (i > 0 && i < size && get_previous_nb(stack_a) > (*stack_a)->nb)
		{
			rra(stack_a, actions);
			i--;
		}
	}
	opt_rotates_a(stack_a, actions, get_lowest(stack_a));
}
