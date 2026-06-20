/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/23 14:27:35 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 07:40:24 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Call a sorting algorithm depending on disorder
void	dispatch_adaptive(t_stack **stack_a, t_stack **stack_b,
			int **actions, float disorder)
{
	if ((int)(disorder * 10) < 2)
		insertionsort(stack_a, actions, stacksize(*stack_a));
	else if ((int)(disorder * 10) >= 2 && (int)(disorder * 10) < 5)
		bucketsort(stack_a, stack_b, actions);
	else if ((int)(disorder * 10) >= 5)
		radix_sort(stack_a, stack_b, actions);
}

//	Call a sorting algorithm and benchmode depending on the options
void	dispatch_options(t_stack **stack_a, t_stack **stack_b,
			int options, int **actions)
{
	float	disorder;

	disorder = compute_disorder(*stack_a);
	if (options % 10 == 4 || options % 10 == 0)
		dispatch_adaptive(stack_a, stack_b, actions, disorder);
	else if (options % 10 == 3)
		radix_sort(stack_a, stack_b, actions);
	else if (options % 10 == 2)
		bucketsort(stack_a, stack_b, actions);
	else if (options % 10 == 1)
		insertionsort(stack_a, actions, stacksize(*stack_a));
	if (options >= 10)
		bench_mode(disorder, options, actions);
}

//	Print Error followed by a newline and exit
void	exit_perror(t_stack **a, t_stack **b, int **actions)
{
	ft_print_err("Error\n");
	free_all(a, b, actions);
	exit (EXIT_FAILURE);
}

//	Push Swap
int	main(int argc, char *argv[])
{
	int		options;
	int		*actions;
	t_stack	*stack_a;
	t_stack	*stack_b;

	if (argc < 2 || !valid_input(argv))
		exit_perror(&stack_a, &stack_b, &actions);
	options = valid_option(argv);
	actions = ft_calloc(10, sizeof(actions));
	stack_a = stackfill(argv);
	stack_b = NULL;
	if (!actions || !stack_a)
		exit_perror(&stack_a, &stack_b, &actions);
	if (!normalizer(argc, argv, &stack_a, options))
		exit_perror(&stack_a, &stack_b, &actions);
	dispatch_options(&stack_a, &stack_b, options, &actions);
	free_all(&stack_a, &stack_b, &actions);
	exit (EXIT_SUCCESS);
}
