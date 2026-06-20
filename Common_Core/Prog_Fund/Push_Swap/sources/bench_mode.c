/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench_mode.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/04 20:06:02 by aspthiba          #+#    #+#             */
/*   Updated: 2026/06/14 20:38:51 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return disorder of the stack
//	0 being the right order and 1 the worst possible order
float	compute_disorder(t_stack *stack)
{
	int	mistakes;
	int	total_pairs;

	if (!stack || !stack->next)
		return (0);
	mistakes = 0;
	total_pairs = 0;
	while (stack && stack->next)
	{
		total_pairs += 1;
		if (stack->nb > stack->next->nb)
			mistakes += 1;
		stack = stack->next;
	}
	return ((float)mistakes / (float)total_pairs);
}

// Operates the printing parameters
// for Bench Mode as seen in the subject
void	bench_mode(float disorder, int option, int **actions)
{
	ft_print_err("[bench] disorder:\t%i.%i%%\n",
		(int)(disorder * 100), (int)(disorder * 10000) % 100);
	ft_print_err("[bench] strategy:\t");
	if (option % 10 == 4 || option % 10 == 0)
	{
		ft_print_err("Adaptive / ");
		ft_sorttype(disorder);
	}
	else if (option % 10 == 3)
		ft_print_err("Complex / O(n log n)\n");
	else if (option % 10 == 2)
		ft_print_err("Medium / O(n√n)\n");
	else if (option % 10 == 1)
		ft_print_err("Simple / O(n^2)\n");
	ft_ptotal(actions);
	ft_pactions(actions);
}

// prints the sorting algorithm type based on disorder
void	ft_sorttype(float disorder)
{
	if ((int)(disorder * 10) < 2)
		ft_print_err("O(n^2)\n");
	else if ((int)(disorder * 10) >= 2 && (int)(disorder * 10) < 5)
		ft_print_err("O(n√n)\n");
	else if ((int)(disorder * 10) >= 5)
		ft_print_err("O(n log n)\n");
}

// prints the total number of actions
void	ft_ptotal(int **actions)
{
	int	i;
	int	total;

	i = 0;
	total = 0;
	while (i <= 10)
	{
		total = total + (*actions)[i];
		i++;
	}
	ft_print_err("[bench] total_ops:\t%i\n", total);
}

// prints the amount of times each action was called
void	ft_pactions(int **actions)
{
	ft_print_err("[bench] sa:\t%i\tsb:\t%i\t", (*actions)[0], (*actions)[1]);
	ft_print_err("ss:\t%i\tpa:\t%i\tpb:\t%i\n",
		(*actions)[2], (*actions)[3], (*actions)[4]);
	ft_print_err("[bench] ra:\t%i\trb:\t%i\t", (*actions)[5], (*actions)[6]);
	ft_print_err("rr:\t%i\trra:\t%i\trrb:\t%i\trrr:\t%i\n",
		(*actions)[7], (*actions)[8], (*actions)[9], (*actions)[10]);
}
