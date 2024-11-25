#include "s21_calc.h"

void push_stack_num(t_stack_num **stack_num, double number) {
  t_stack_num *new_node = (t_stack_num *)calloc(1, sizeof(t_stack_num));
  if (new_node != NULL) {
    new_node->next = *stack_num;
    new_node->number = number;
    *stack_num = new_node;
  }
}

double pop_stack_num(t_stack_num **stack_num) {
  t_stack_num *old_node = NULL;
  double res = 0;
  if (stack_num != NULL) {
    old_node = *stack_num;
    if (old_node != NULL) {
      res = old_node->number;
      *stack_num = (*stack_num)->next;
    }
    free(old_node);
  }
  return res;
}

int push_stack_opt(t_stack_opt **stack_opt, char option) {
  t_stack_opt *new_node = calloc(1, sizeof(t_stack_opt));
  if (new_node != NULL) {
    new_node->next = *stack_opt;
    new_node->option = option;
    *stack_opt = new_node;
  } else {
    return -1;
  }
  return 0;
}

char pop_stack_opt(t_stack_opt **stack_opt) {
  t_stack_opt *old_node = NULL;
  char res = 0;
  if (*stack_opt != NULL) {
    old_node = *stack_opt;
    res = old_node->option;
    *stack_opt = (*stack_opt)->next;
    free(old_node);
  }
  return res;
}

void function_mul(t_stack_num **stack_num, double a) {
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  c = a * b;
  push_stack_num(stack_num, c);
}

int function_div(t_stack_num **stack_num, double a) {
  int status = OK;
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  if (a != 0) {
    c = b / a;
    push_stack_num(stack_num, c);
  } else {
    status = ERR;
  }
  return status;
}

int function_mod(t_stack_num **stack_num, double a) {
  int status = OK;
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  if (a != 0) {
    c = (int)b % (int)a;
    push_stack_num(stack_num, c);
  } else {
    status = ERR;
  }
  return status;
}

void function_sum(t_stack_num **stack_num, double a) {
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  c = a + b;
  push_stack_num(stack_num, c);
}

void function_sub(t_stack_num **stack_num, double a) {
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  c = b - a;
  push_stack_num(stack_num, c);
}

void function_exp(t_stack_num **stack_num, double a) {
  double b = 0, c = 0;
  b = pop_stack_num(stack_num);
  c = pow(b, a);
  push_stack_num(stack_num, c);
}

void function_cos(t_stack_num **stack_num, double a) {
  double c = 0;
  c = cos(a);
  push_stack_num(stack_num, c);
}

void function_sin(t_stack_num **stack_num, double a) {
  double c = 0;
  c = sin(a);
  push_stack_num(stack_num, c);
}

void function_tan(t_stack_num **stack_num, double a) {
  double c = 0;
  c = tan(a);
  push_stack_num(stack_num, c);
}

void function_acos(t_stack_num **stack_num, double a) {
  double c = 0;
  c = acos(a);
  push_stack_num(stack_num, c);
}

void function_asin(t_stack_num **stack_num, double a) {
  double c = 0;
  c = asin(a);
  push_stack_num(stack_num, c);
}

void function_atan(t_stack_num **stack_num, double a) {
  double c = 0;
  c = atan(a);
  push_stack_num(stack_num, c);
}

void function_sqrt(t_stack_num **stack_num, double a) {
  double c = 0;
  c = sqrt(a);
  push_stack_num(stack_num, c);
}

void function_ln(t_stack_num **stack_num, double a) {
  double c = 0;
  c = log(a);
  push_stack_num(stack_num, c);
}

void function_log10(t_stack_num **stack_num, double a) {
  double c = 0;
  c = log10(a);
  push_stack_num(stack_num, c);
}

int math_calc(t_stack_num **stack_num, t_stack_opt **stack_opt) {
  int status = OK;
  double a = pop_stack_num(stack_num);
  char ch = pop_stack_opt(
      stack_opt);
  switch (ch) {
    case '*':
      function_mul(stack_num, a);
      break;
    case '/':
      status = function_div(stack_num, a);
      break;
    case '+':
      function_sum(stack_num, a);
      break;
    case '-':
      function_sub(stack_num, a);
      break;
    case '^': 
      function_exp(stack_num, a);
      break;
    case 'o': 
      function_cos(stack_num, a);
      break;
    case 't':
      function_sin(stack_num, a);
      break;
    case 'h':
      function_tan(stack_num, a);
      break;
    case 'f':
      function_acos(stack_num, a);
      break;
    case 'i':
      function_asin(stack_num, a);
      break;
    case 'x':
      function_atan(stack_num, a);
      break;
    case 's':
      function_sqrt(stack_num, a);
      break;
    case 'e':
      function_ln(stack_num, a);
      break;
    case 'n':
      function_log10(stack_num, a);
      break;
    case 'm':
      status = function_mod(stack_num, a);
      break;
    default:
      status = ERR;
  }
  return status;
}

int calculation(t_stack_num **stack_num, t_stack_opt **stack_opt) {
  int result = 1;
  while (*stack_opt != NULL && result == 1) {
    if (!math_calc(stack_num,
                   stack_opt)) {
      result = 0;
    }
  }
  return result;
}

int check_priority(char ibuf) {
  int result = 0;
  char massive[10] =
      "othfixsen"; 
  if ((ibuf == '+' || ibuf == '-')) {
    result = 1;
  } else if (ibuf == '*' || ibuf == '/' || ibuf == 'm') {
    result = 2;
  } else if (ibuf == '^') {
    result = 3;
  } else if (strchr(massive, ibuf) != NULL) {
    result = 4;
  }
  return result;
}

int parser_option(const char ibuf, t_stack_num **stack_num,
                  t_stack_opt **stack_opt, int *to_left, int *j) {
  int status = OK;
  if (ibuf == '+' || ibuf == '-' || ibuf == '*' || ibuf == '/' ||
      ibuf == '^') { 
    if (*stack_opt == NULL) {
      push_stack_opt(stack_opt, ibuf);
      *j = -1;
      *to_left = 1;
    } else {
      if (check_priority(ibuf) >
          check_priority((*stack_opt)->option)) {
        push_stack_opt(stack_opt, ibuf);
        *j = -1;
        *to_left = 1;
      } else if ((check_priority(ibuf) <=
                  check_priority((*stack_opt)->option)) &&
                 (*stack_opt)->option != '(') {
        if (!math_calc(stack_num, stack_opt)) {
          status = ERR;
        }
        *to_left = 0;
      }
    }
  }
  return status;
}

int parser_bracket(const char ibuf, t_stack_num **stack_num,
                   t_stack_opt **stack_opt, int *to_left, int *j) {
  int status = OK;
  if (ibuf == '(') {
    push_stack_opt(stack_opt, ibuf);
    *to_left = 1;
    *j = -1;
  } else if (ibuf == ')') {
    while (
        *stack_num != NULL && *stack_opt != NULL &&
        (*stack_opt)->option != '(' &&
        status ==
            OK) {
      if (!math_calc(
              stack_num,
              stack_opt)) {
        status = ERR;
        break;
      }
    }
    pop_stack_opt(stack_opt);
  }
  return status;
}

int check_func_ex(t_stack_opt **stack_opt, char *func_ex) {
  char functions[11][5] = {"cos",  "sin",  "tan", "acos", "asin",
                           "atan", "sqrt", "ln",  "log",  "mod"};
  int error = 1;
  int status = OK;
  char example = 0;
  for (int i = 0; i < 10 && error == 1; i++) {
    if (strcmp(func_ex, functions[i]) == 0) {
      if (i == 0) { /* i = 0 - cos */
        example = 'o';
      } else if (i == 1) { /* i = 1 - sin */
        example = 't';
      } else if (i == 2) { /* i = 2 - tan */
        example = 'h';
      } else if (i == 3) { /* i = 3 - acos */
        example = 'f';
      } else if (i == 4) { /* i = 4 - asin */
        example = 'i';
      } else if (i == 5) { /* i = 5 - atan */
        example = 'x';
      } else if (i == 6) { /* i = 6 - sqrt */
        example = 's';
      } else if (i == 7) { /* i = 7 - ln */
        example = 'e';
      } else if (i == 8) { /* i = 8 - log */
        example = 'n';
      } else if (i == 9) { /* i = 9 - log */
        example = 'm';
      }
      push_stack_opt(stack_opt, example);
      error = 0;
    }
    if (i == 9 && error == 1) {
      status = ERR;
    }
  }
  return status;
}

void to_str(const char **ibuf, char *str_num) {
  if (**ibuf == '-') {
    *str_num = **ibuf;
    (*ibuf)++;
    str_num++;
  }
  while (isdigit(**ibuf)) {
    *str_num = **ibuf;
    str_num++;
    (*ibuf)++;
  }
  if (**ibuf == '.' || **ibuf == ',') {
    *str_num = '.';
    (*ibuf)++;
    str_num++;
  }
  while (isdigit(**ibuf)) {
    *str_num = **ibuf;
    str_num++;
    (*ibuf)++;
  }
}

int parser_v_1(const char *ibuf, t_stack_num **stack_num,
               t_stack_opt **stack_opt) {
  int status = OK, to_left = 0, j = 0;
  double number = 0;
  char str_func[7] = "cstalm";
  for (; *ibuf && status == OK; ibuf++, j++) {
    if (strchr(str_func, *ibuf) !=
        NULL) {
      char func_ex[5] = {0};
      if (*ibuf != 'm') {
        for (int i = 0; *ibuf != '(' && status == OK;
             i++, ibuf++) {
          if (i > 4) {
            status = ERR;
          }
          func_ex[i] = *ibuf;
        }
      } else if (*ibuf == 'm') {
        for (int i = 0; !isdigit(*ibuf) && status == OK;
             i++, ibuf++) {
          if (i > 3) {
            status = ERR;
          }
          func_ex[i] = *ibuf;
        }
      }
      if (status == OK) {
        status =
            check_func_ex(stack_opt, func_ex);
      }
    }
    if (isdigit(*ibuf) ||
        ((*ibuf == '-' || *ibuf == '+') && isdigit(*ibuf) + 1 &&
         j == 0)) {
      char str_num[256] = {0};
      to_str(&ibuf, str_num);
      number = atof(str_num);
      push_stack_num(stack_num, number);
    }
    if (!parser_option(*ibuf, stack_num, stack_opt, &to_left, &j)) {
      status = ERR;
    }
    if (!parser_bracket(*ibuf, stack_num, stack_opt, &to_left, &j)) {
      status = ERR;
    }
    if (to_left == 0 &&
        *ibuf != ' ') {
      ibuf--;
    }
  }
  return status;
}

double result_c(const char *str, int *error) {
  double res = 0;
  if (check_str(str)) {
    t_stack_num *stack_num = NULL;
    t_stack_opt *stack_opt = NULL;
    *error = parser_v_1(str, &stack_num, &stack_opt);
    if (*error == OK) {
      *error = calculation(&stack_num, &stack_opt);
    }
    if (*error == OK && stack_num != NULL) {
      res = stack_num->number;
    }
    while (stack_num) {
      pop_stack_num(&stack_num);
    }
    while (stack_opt) {
      pop_stack_opt(&stack_opt);
    }
  }
  return res;
}

int check_str(const char *str) {
  int close = 0, open = 0;
  char str_func[15] = "cosintaqrlogmd";
  char str_check[24] = " p1234567890*/+-()^.,";
  int error = OK;
  for (int i = 0; str[i] != '\0' && error == OK; i++) {
    if (str[i] == '(') {
      open++;
    } else if (str[i] == ')') {
      close++;
    }
    if (strchr(str_check, str[i]) == NULL && strchr(str_func, str[i]) == NULL) {
      error = ERR;
    }
    if (str[i] == 'm' && str[i + 1] == 'o' && str[i + 2] == 'd' &&
        str[i + 3] == '\0') {
      error = ERR;
    }
    if (str[0] == 'm' && str[1] == 'o' && str[2] == 'd') {
      error = ERR;
    }
    if (str[i] == '(' && str[i + 1] == '.' && str[i + 2] == ')') {
      error = ERR;
    }
    if (str[i] == '.' && isdigit(str[i + 1]) && str[i + 2] == '.') {
      error = ERR;
    }
    if (str[i] == '^' &&
        ((!isdigit(str[i + 1]) && str[i + 1] != '(' && str[i + 1] != ' '))) {
      error = ERR;
    }
    if (str[i] == '^' &&
        ((!isdigit(str[i - 1]) && str[i - 1] != ')' && str[i + 1] != ' '))) {
      error = ERR;
    }
    if (str[i] == '(' && str[i + 1] == ')') {
      error = ERR;
    }
  }
  if (open != close) {
    error = ERR;
  }
  if (error == OK) {
    error = check_extra(str);
  }
  return error;
}

int check_extra(const char *str) {
  int error = OK;
  char str_check_opr[7][1] = {"+", "-", "/", "*", ".", ","};
  char str_check_all[10][1] = {"+", "-", "/", "*", "(", ")", "^", ".", ","};
  for (int i = 0; str[i] != '\0'; i++) {
    for (int j = 0; j < 7 && error == OK; j++) {
      if (strchr(str_check_opr[j], str[i]) != NULL &&
          strchr(str_check_opr[j], str[i + 1]) != NULL && str[i] != '-' &&
          str[i + 1] != '-') {
        error = ERR;
      }
    }
    for (int j = 0; j < 9 && error == OK; j++) {
      if (strchr(str_check_all[j], str[i]) != NULL && str[i + 1] == '\0' &&
          str[i] != ')') {
        error = ERR;
      }
    }
    for (int j = 0; j < 7 && error == OK; j++) {
      if (strchr(str_check_opr[j], str[i]) != NULL && str[i + 1] == '\0') {
        error = ERR;
      }
    }
  }
  return error;
}