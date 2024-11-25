#ifndef CALC_H
#define CALC_H
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define OK 1
#define ERR 0

typedef struct t_stack_num {
  double number;
  struct t_stack_num *next;
} t_stack_num;

typedef struct stack_opt {
  struct stack_opt *next;
  char option;
} t_stack_opt;

void create_node_num(double number, t_stack_num **stack_num);
void push_stack_num(t_stack_num **stack_num, double number);
double pop_stack_num(t_stack_num **stack_num);
t_stack_num *peek_stack_num(t_stack_num **stack_num);
void free_stack_num(t_stack_num **stack_num);

t_stack_opt *create_node_opt(char option);
int push_stack_opt(t_stack_opt **stack_opt, char option);
char pop_stack_opt(t_stack_opt **stack_opt);
t_stack_opt *peek_stack_opt(t_stack_opt **stack_opt);
void free_stack_opt(t_stack_opt **stack_opt);

long double s21_strtoqld(char *nptr);

int math_calc(t_stack_num **stack_num, t_stack_opt **stack_opt);
int calculation(t_stack_num **stack_num, t_stack_opt **stack_opt);
void function_mul(t_stack_num **stack_num, double a);
int function_div(t_stack_num **stack_num, double a);
int function_mod(t_stack_num **stack_num, double a);
void function_sum(t_stack_num **stack_num, double a);
void function_sub(t_stack_num **stack_num, double a);
void function_exp(t_stack_num **stack_num, double a);
void function_cos(t_stack_num **stack_num, double a);
void function_sin(t_stack_num **stack_num, double a);
void function_tan(t_stack_num **stack_num, double a);
void function_acos(t_stack_num **stack_num, double a);
void function_asin(t_stack_num **stack_num, double a);
void function_atan(t_stack_num **stack_num, double a);
void function_sqrt(t_stack_num **stack_num, double a);
void function_ln(t_stack_num **stack_num, double a);
void function_log10(t_stack_num **stack_num, double a);

int check_str(const char *str);
int check_extra(const char *str);
int check_priority(char ibuf);
int parser_option(const char ibuf, t_stack_num **stack_num,
                  t_stack_opt **stack_opt, int *to_left, int *j);
int parser_bracket(const char ibuf, t_stack_num **stack_num,
                   t_stack_opt **stack_opt, int *to_left, int *j);
int check_func_ex(t_stack_opt **stack_opt, char *func_ex);
void to_str(const char **ibuf, char *str_num);
int parser_v_1(const char *ibuf, t_stack_num **stack_num,
               t_stack_opt **stack_opt);
double result_c(const char *str, int *error);
#endif  // CALC_H
