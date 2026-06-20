/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   normalizer.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 17:51:12 by nmak              #+#    #+#             */
/*   Updated: 2026/06/09 23:46:03 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//	Return an int tab with the argv values
int	*fill_tab(int argc, char **argv)
{
	int	i;
	int	*tab;

	tab = malloc(sizeof(tab) * argc - 1);
	if (!tab)
		return (NULL);
	i = 0;
	while (argv[i])
	{
		tab[i] = ft_atoi(argv[i]);
		i++;
	}
	return (tab);
}

//	Normalize the numbers in stack
int	normalizer(int argc, char **argv, t_stack **stack, int options)
{
	int	*tab;

	argv++;
	while (options > 0)
	{
		argv++;
		argc--;
		options /= 10;
	}
	tab = fill_tab(argc, argv);
	if (!tab)
		return (0);
	quicksort(tab, 0, argc - 2);
	set_final_pos(stack, tab, argc - 2);
	free (tab);
	return (1);
}

//	Set the sorted pos of each number in the stack compared to the tab
void	set_final_pos(t_stack **stack, int *tab, int max)
{
	int		i;
	t_stack	*current;

	current = *stack;
	while (current)
	{
		i = 0;
		while (i < max && current->nb != tab[i])
			i++;
		if (current->nb == tab[i])
			current->sorted_pos = i;
		current = current->next;
	}
}
