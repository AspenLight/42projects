/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_bucket.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/10 00:47:00 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 07:28:46 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return the index of the first number above or equals to isqrt in stack
//	-1 if no correspondance
int	get_first_isqrt(t_stack **stack, int isqrt)
{
	int		i;
	t_stack	*curr;

	i = 0;
	curr = *stack;
	while (curr)
	{
		if (curr->sorted_pos >= isqrt)
			return (i);
		i++;
		curr = curr->next;
	}
	return (-1);
}

//	Return the index of the last number above or equals to isqrt in stack
//	-1 if no correspondance
int	get_last_isqrt(t_stack **stack, int isqrt)
{
	int		i;
	int		last;
	t_stack	*curr;

	i = 0;
	last = i;
	curr = *stack;
	while (curr)
	{
		if (curr->sorted_pos >= isqrt)
			last = i;
		i++;
		curr = curr->next;
	}
	if (get_index_nb(stack, last) >= isqrt)
		return (last);
	return (-1);
}

//	Return the index of the closest number above or equals to isqrt in stack
//	-1 if no correspondance
int	get_closest_isqrt(t_stack **stack, int isqrt)
{
	int	first;
	int	last;
	int	size;

	first = get_first_isqrt(stack, isqrt);
	last = get_last_isqrt(stack, isqrt);
	size = stacksize(*stack);
	if (first <= (size / 2))
		return (first);
	return (last);
}

//	Push every sorted pos numbers over or equal isqrt to a
//	with the best rotations possibles
//	Return the numbers of pushed elements
int	push_over_isqrt(t_stack **a, t_stack **b, int **actions, int isqrt)
{
	int	count;
	int	in_range;

	count = 0;
	in_range = get_closest_isqrt(b, isqrt);
	while (*b && in_range > -1)
	{
		if ((*b)->sorted_pos >= isqrt)
		{
			pa(a, b, actions);
			count++;
		}
		else
		{
			opt_rotates_b(b, actions, in_range);
			in_range = get_closest_isqrt(b, isqrt);
		}
	}
	return (count);
}

//	Bucket sort !
void	bucketsort(t_stack **a, t_stack **b, int **actions)
{
	int	i;
	int	nb;
	int	sqrt;

	sqrt = ft_sqrt(stacksize(*a));
	i = stacksize(*a) / sqrt;
	while (*a)
		pb(b, a, actions);
	while (i >= 0)
	{
		nb = push_over_isqrt(a, b, actions, (i * sqrt));
		insertionsort(a, actions, nb);
		i--;
	}
}
