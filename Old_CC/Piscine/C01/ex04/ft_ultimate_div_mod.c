/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <asthibau@students.42.fr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/21 11:19:07 by asthibau          #+#    #+#             */
/*   Updated: 2025/02/21 11:24:16 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	tempdiv;
	int	tempmod;

	tempdiv = *a / *b;
	tempmod = *a % *b;
	*a = tempdiv;
	*b = tempmod;
}
