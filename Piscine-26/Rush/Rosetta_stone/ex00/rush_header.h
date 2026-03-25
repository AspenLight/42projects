/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush_header.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aspthiba <aspthiba@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/22 17:44:05 by aspthiba          #+#    #+#             */
/*   Updated: 2026/03/22 19:09:10 by aspthiba         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef RUSH_HEADER_H
# define RUSH_HEADER_H

int					is_space(char c);
void				go_next_line(int src_fd);
int					get_nb_line(char *path);
unsigned long long	get_write_nb_space(int src_fd);
int					write_key(int src_fd);
int					write_value(int src_fd);
int					file_parsing(char *path);
int					number_len(char *str);
int					valid_number(char *number);
int					get_nb_line(char *path);
void				go_to_next_line(int src_fd);
int					str_key_len(char *key);
char				*get_keys(void);
int					write_number(char *number);
int					sort_file(void);
int					write_dict_n(int n);
char				*true_pointer(char *number);

#endif
