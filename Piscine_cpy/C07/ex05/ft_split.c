/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: asthibau <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/03/11 16:00:00 by asthibau          #+#    #+#             */
/*   Updated: 2025/03/11 16:00:20 by asthibau         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int    ft_strlen_tosep(char *str, char *to_find)
{
    int    i;
    int    n;

    i = 0;
    n = 0;
    if (to_find[n] == '\0')
    {
        while(str[i])
            i++;
        return (i);
    }
    while (str[i])
    {
        while ((str[i + n] == to_find[n]) && (str[i + n] != '\0'))
        {
            n++;
        }
        if (to_find[n] == '\0')
            return(i - 1)
        i++;
    }
    return (i);
}

char    *ft_strstr(char *str, char *to_find)
{
    int    i;
    int    n;

    i = 0;
    n = 0;
    if (to_find[i] == '\0')
        return (str);
    while (str[i])
    {
        n = 0;
        while ((str[i + n] == to_find[n]) && (str[i + n] != '\0'))
        {
                n++;
        }
        if (to_find[n] == '\0')
        {
            return (str + i + n);
        }
        i++;
    }
    return (0);
}

char    *ft_strndup(char *src, int n)
{
    char    *copy;
    int        i;

    i = 0;
    while (src[i] || i <= n)
    {
        i++;
    }
    copy = malloc(sizeof(*copy) * (i + 1));
    i = 0;
    while (src[i] || i <= n)
    {
        copy[i] = src[i];
        i++;
    }
    copy[i] = '\0';
    return (copy);
}

int    ft_count_sep(char *str, char *to_find)
{
    int     i;
        int     n;
    int    count;

        i = 0;
        n = 0;
    count = 1;
        if (to_find[i] == '\0')
                return (count);
        while (str[i])
        {
                n = 0;
                while ((str[i + n] == to_find[n]) && (str[i + n] != '\0'))
                {
                                n++;
                }
                if (to_find[n] == '\0')
                {
            count++;
                }
                i++;
        }
        return (count);
}

char    **ft_split(char *str, char *charset)
{
    char    **result;
    char    *sepstr;
    int    strnum;
    int    i;

    strnum = ft_count_sep(charset);
    result = (char**)malloc(sizeof(*char) * strnum);
    while (i < strnum)
    {
        
        result[i] = ft_strndup(str, ft_strlen_tosep(
    }
}

#include <stdio.h>
int    main(void)
{
    if (argc == 3)
    {
        char str[] = argv[1];
        char charset[] = argv[2];
        char    **result = ft_split(str, charset);
        int    i = 0;
        int    n = 0;
        while (result[i])
        {
            printf("%s\n", result[i]);
            i++;
        }
    }
    return (0);
}
