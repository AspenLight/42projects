/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_bucket_utils.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/12 06:10:07 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 06:28:25 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return the approximate square root of nb
int	ft_sqrt(int nb)
{
	int	sqrt;

	sqrt = 0;
	while ((sqrt + 1) * (sqrt + 1) <= nb)
		sqrt++;
	return (sqrt);
}

//	Return the sorted_pos number at index position
int	get_index_nb(t_stack **stack, int index)
{
	t_stack	*current;

	current = *stack;
	while (current && index--)
		current = current->next;
	return (current->sorted_pos);
}

//	Put the given index nb to the top of b
void	opt_rotates_b(t_stack **b, int **actions, int index)
{
	int	size;

	size = stacksize(*b);
	if (index < size / 2)
	{
		while (index--)
			rb(b, actions);
	}
	else if (index >= size / 2)
	{
		while (index++ < size)
			rrb(b, actions);
	}
}
