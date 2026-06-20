/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_radix.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 17:53:55 by nmak              #+#    #+#             */
/*   Updated: 2026/06/14 20:41:08 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	get_bits_len(int bits)
{
	int	len;

	len = 0;
	while (bits > 0)
	{
		bits = bits >> 1;
		len++;
	}
	return (len);
}

int	get_max_bits(t_stack **a)
{
	int		max;
	t_stack	*current;

	current = *a;
	max = current->sorted_pos;
	while (current)
	{
		if (current->sorted_pos > max)
			max = current->sorted_pos;
		current = current->next;
	}
	return (max);
}

void	radix_sort(t_stack **a, t_stack **b, int **actions)
{
	int	bits;
	int	max_bits;
	int	stack_size;
	int	max_bits_len;

	bits = 0;
	max_bits = get_max_bits(a);
	max_bits_len = get_bits_len(max_bits);
	while (!is_sorted(*a) && bits < max_bits_len)
	{
		stack_size = (stacksize(*a));
		while (stack_size--)
		{
			if ((((*a)->sorted_pos >> bits) & 1) == 0)
				pb(b, a, actions);
			else
				ra(a, actions);
		}
		while (*b)
			pa(a, b, actions);
		bits++;
	}
}
