/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 19:07:55 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/25 20:05:07 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *str);

int	ft_nblen(long nb, int size);

int	ft_basecheck(char *base);

int	ft_base_index(char c, char *base)
{
	int	i;

	i = 0;
	while (base[i])
	{
		if (base[i] == c)
			return (i);
		i++;
	}
	return (-1);
}

int	ft_atoi_base(char *str, char *base)
{
	int		i;
	int		sign;
	long	result;

	i = 0;
	sign = 1;
	result = 0;
	while (str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	while (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = sign * -1;
		i++;
	}
	while (str[i])
	{
		if (str[i] && ft_base_index(str[i], base) != -1)
			result = (result * ft_strlen(base)) + ft_base_index(str[i], base);
		i++;
	}
	return (result * sign);
}

void	ft_alloc_result(char *result, long n, char *base_to, int size)
{
	int	base;

	base = ft_strlen(base_to);
	result[size] = '\0';
	if (n == 0)
		result[0] = base_to[0];
	if (n < 0)
	{
		result[0] = '-';
		n = -n;
	}
	while (n > 0)
	{
		result[size - 1] = base_to[n % base];
		n = n / base;
		size--;
	}
}

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	long	n;
	char	*result;
	int		size;

	if (!nbr || !base_from || !base_to)
		return (NULL);
	if (!ft_basecheck(base_from) || !ft_basecheck(base_to))
		return (NULL);
	n = ft_atoi_base(nbr, base_from);
	size = ft_nblen(n, ft_strlen(base_to));
	result = malloc((size + 1) * sizeof(char));
	if (!result)
		return (NULL);
	ft_alloc_result(result, n, base_to, size);
	return (result);
}
/*
#include <stdio.h>

int	main(void)
{
	char	*result;
	char	*hex;
	char	*bin;
	char	*dec;
	char	*pon;

	hex = "0123456789abcdef";
	dec = "0123456789";
	bin = "01";
	pon = "poneyvif";
	printf("42, Decimal to Binary\n");
	result = ft_convert_base("42", dec, bin);
	if (result == NULL)
		printf("Error\n");
	printf("Result: %s\n", result);
	free(result);
	printf("2a (42), Hex to Poneyvif\n");
	result = ft_convert_base("2a", hex, pon);
	if (result == NULL)
		printf("Error\n");
	printf("Result: %s\n", result);
	free(result);
	printf("0, Decimal to Binary\n");
	result = ft_convert_base("0", dec, bin);
	if (result == NULL)
		printf("Error\n");
	printf("Result: %s\n", result);
	free(result);
	printf("-2147483648, Decimal to Hex\n");
	result = ft_convert_base("-2147483648", dec, hex);
	if (result == NULL)
		printf("Error\n");
	printf("Result: %s\n", result);
	free(result);
	printf("---+--101010, Binary to Decimal\n");
	result = ft_convert_base("---+--101010", bin, dec);
	if (result == NULL)
		printf("Error\n");
	printf("Result: %s\n", result);
	free(result);
	printf("NULL, Binary to Decimal\n");
	result = ft_convert_base(NULL, bin, dec);
	if (result == NULL)
		printf("Error, NULL as variable (expected outcome)\n");
	else
	{
		printf("Result: %s\n", result);
		free(result);
	}
	return (0);
}
*/
