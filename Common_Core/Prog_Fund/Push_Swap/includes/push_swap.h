/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nmak <nmak@learner.42.tech>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 18:45:52 by nmak              #+#    #+#             */
/*   Updated: 2026/06/12 06:38:54 by nmak             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

/* ------------------------------------- */
/*                Includes				 */
/* ------------------------------------- */

# include "libft.h"
# include "ft_printf.h"
# include <limits.h>

/* ------------------------------------- */
/*                Structs                */
/* ------------------------------------- */

typedef struct s_stack
{
	int				nb;
	int				sorted_pos;
	struct s_stack	*next;
}	t_stack;

//	Stack utils
int		stacksize(t_stack *stack);
void	stackaddback(t_stack **stack, t_stack *new);
void	stackaddfront(t_stack **stack, t_stack *new);
t_stack	*newnode(int nb);
t_stack	*stackfill(char **argv);

//	Stack free
void	freestack(t_stack *stack);
void	free_all(t_stack **a, t_stack **b, int **actions);

/* ------------------------------------- */
/*                 Main                  */
/* ------------------------------------- */

void	dispatch_adaptive(t_stack **stack_a, t_stack **stack_b,
			int **actions, float disorder);
void	dispatch_options(t_stack **stack_a, t_stack **stack_b,
			int options, int **actions);
void	exit_perror(t_stack **a, t_stack **b, int **actions);
int		main(int argc, char *argv[]);

/* ------------------------------------- */
/*             Input Checker             */
/* ------------------------------------- */

//	Input checker
int		valid_option(char **argv);
int		valid_nb(char **argv);
int		valid_int(char **argv);
int		valid_dup(char **argv);
int		valid_input(char **argv);

//	Input checker utils
int		atoi_error(const char *nptr, int *error);

/* ------------------------------------- */
/*               Operations              */
/* ------------------------------------- */

//	Swap
void	swap(t_stack *stack);
void	sa(t_stack *stack_a, int **actions);
void	sb(t_stack *stack_b, int **actions);
void	ss(t_stack *stack_a, t_stack *stack_b, int **actions);

//	Push
void	pa(t_stack **stack_a, t_stack **stack_b, int **actions);
void	pb(t_stack **stack_b, t_stack **stack_a, int **actions);
void	pp(t_stack **stack_b, t_stack **stack_a, int **actions);
void	pp(t_stack **stack_b, t_stack **stack_a, int **actions);

//	Rotate
void	rotate(t_stack **stack);
void	ra(t_stack **stack_a, int **actions);
void	rb(t_stack **stack_b, int **actions);
void	rr(t_stack **stack_a, t_stack **stack_b, int **actions);

//	Reverse rotate
void	reverse_rotate(t_stack **stack);
void	rra(t_stack **stack_a, int **actions);
void	rrb(t_stack **stack_b, int **actions);
void	rrr(t_stack **stack_a, t_stack **stack_b, int **actions);

/* ------------------------------------- */
/*               Algorithms              */
/* ------------------------------------- */

//	Instertion sort
int		get_lowest(t_stack **stack);
int		get_previous_nb(t_stack **stack);
int		get_dist_to_top(t_stack **stack, int nb);
void	opt_rotates_a(t_stack **stack, int **actions, int nb);
void	insertionsort(t_stack **stack_a, int **actions, int index);

//	Bucket sort
int		get_last_isqrt(t_stack **stack, int isqrt);
int		get_first_isqrt(t_stack **stack, int isqrt);
int		get_closest_isqrt(t_stack **stack, int isqrt);
int		push_over_isqrt(t_stack **a, t_stack **b, int **actions, int isqrt);
void	bucketsort(t_stack **a, t_stack **b, int **actions);

//	Bucket sort utils
int		ft_sqrt(int nb);
int		get_index_nb(t_stack **stack, int index);
void	opt_rotates_b(t_stack **b, int **actions, int index);

//	Radix sort
int		get_bits_len(int bits);
int		get_max_bits(t_stack **a);
void	radix_sort(t_stack **a, t_stack **b, int **actions);

//	Algorithms utils
int		is_sorted(t_stack *a);

/* ------------------------------------- */
/*               Normalizer              */
/* ------------------------------------- */

//	Normalizer
int		*fill_tab(int argc, char **argv);
int		normalizer(int argc, char **argv, t_stack **stack, int options);
void	set_final_pos(t_stack **stack, int *tab, int max);

//	Utils (Quicksort)
int		partition(int tab[], int low, int high);
void	qs_swap(int *a, int *b);
void	quicksort(int tab[], int low, int high);

/* ------------------------------------- */
/*               Benchmode               */
/* ------------------------------------- */

//	Benchmode
float	compute_disorder(t_stack *stack_a);
void	bench_mode(float disorder, int option, int **actions);
void	ft_printfloat(float disorder);
void	ft_sorttype(float disorder);
void	ft_ptotal(int **actions);
void	ft_pactions(int **actions);

/* ------------------------------------- */
/*            Print on stderr            */
/* ------------------------------------- */

void	ft_putchar_err(char c, int *ptr_count);
void	ft_putstr_err(const char *str, int *ptr_count);
void	ft_putnbr_err(long int nb, int *ptr_count);
void	ft_percent_err(const char *str, va_list list, int *ptr_count);
int		ft_print_err(const char *str, ...);

#endif
