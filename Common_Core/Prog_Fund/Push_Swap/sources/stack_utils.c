/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_utils.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 20:37:34 by nmak              #+#    #+#             */
/*   Updated: 2026/06/14 20:47:22 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

//  Return the size of the stack
int	stacksize(t_stack *stack)
{
	int	count;

	count = 0;
	while (stack)
	{
		stack = stack->next;
		count++;
	}
	return (count);
}

//	Add the newnode to the end of the stack
void	stackaddback(t_stack **stack, t_stack *new)
{
	t_stack	*current;

	if (!*stack)
	{
		*stack = new;
		return ;
	}
	current = *stack;
	while (current->next)
		current = current->next;
	current->next = new;
}

//	Add the newnode to the front of the stack
void	stackaddfront(t_stack **stack, t_stack *new)
{
	new->next = *stack;
	*stack = new;
}

//	Return a pointer to a new node with the given integer
//	NULL in case of error
t_stack	*newnode(int nb)
{
	t_stack	*new;

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->nb = nb;
	new->next = NULL;
	return (new);
}

//	Return a pointer to a t_stack containing
//	the arguments given converted into integers
//	NULL in case of error
t_stack	*stackfill(char **argv)
{
	int		i;
	int		options;
	t_stack	*stack_a;
	t_stack	*new;

	i = 1;
	stack_a = NULL;
	options = valid_option(argv);
	if (options)
		argv++;
	if (options >= 10)
		argv++;
	while (argv[i])
	{
		new = newnode(ft_atoi(argv[i]));
		if (!new)
			return (NULL);
		stackaddback(&stack_a, new);
		i++;
	}
	return (stack_a);
}
