import ast
import inspect


def f(template: str) -> str:
    if not isinstance(template, str):
        raise TypeError(f'Cannot format {type(template)}')
    parent_frame = inspect.stack()[1].frame
    f_str_ast = parse_format_string(template)
    f_str_code = compile(f_str_ast, '<fyeah>', 'eval')
    formatted = eval(f_str_code, parent_frame.f_globals, parent_frame.f_locals)
    assert isinstance(formatted, str)
    return formatted


def parse_format_string(source: str) -> ast.Expression:
    return ast.fix_missing_locations(ast.Expression(_parse_format_string(source)))


def _parse_format_string(source: str) -> ast.JoinedStr:
    i = 0
    chunk_start = 0
    str_parts = []
    while i < len(source):
        if source[i] == '}':
            if source[i : (i + 2)] == '}}':
                i += 2
                continue
            else:
                # expr-terminating }s are consumed elsewhere
                raise SyntaxError("f-string: single '}' is not allowed")
        if source[i] == '{':
            if len(source) == (i + 1):
                raise SyntaxError("f-string: '{' was never closed")
            if source[i + 1] == '{':
                i += 2
                continue
            if i > chunk_start:
                str_parts.append(ast.Constant(source[chunk_start:i]))

            in_str = ''
            in_set_dict = 0
            in_parens = 0
            i += 1
            chunk_start = i
            fmt_start = None
            while i < len(source):
                if source[i] == '}' and not in_str:
                    if in_set_dict:
                        in_set_dict -= 1
                    else:
                        break
                elif source[i] == '{' and not in_str:
                    in_set_dict += 1
                elif source[i] == '(' and not in_str:
                    in_parens += 1
                elif source[i] == ')' and in_parens > 0 and not in_str:
                    in_parens -= 1
                elif source[i] == '#':
                    i += 1
                    while i < len(source):
                        if source[i] == '\n' or source[i : (i + 2)] == '\r\n':
                            break
                        i += 1
                    else:
                        raise SyntaxError("f-string: '{' was never closed")
                elif source[i] == '\\' and source[i + 1 : i + 2] in ('"', "'", '\\'):
                    # ast.parse will raise errors for illegal use of '\' in or out of strings
                    i += 2
                    continue
                elif source[i] in ('"', "'"):  # not escaped
                    if in_str:
                        if source[i : i + len(in_str)] == in_str:
                            i += len(in_str)
                            in_str = ''
                            continue
                    else:
                        if len(source) >= i + 3 and (
                            source[i] == source[i + 1] == source[i + 2]
                        ):
                            in_str = source[i : i + 3]
                            i += 3
                            continue
                        else:
                            in_str = source[i]
                elif (
                    source[i] == ':'
                    and not fmt_start
                    and not in_str
                    and not in_set_dict
                    and not in_parens
                ):
                    # it is easier to not this location while walking
                    # forward through the string because a ':' denotes
                    # the start of a format_spec however, a ':' can
                    # appear in the main expression in any of
                    #   string literal, dict literal, slice literal
                    #   assignment expression, lambda
                    # a ':' can _also_ appear anywhere within the
                    # format_spec as the format_spec is a free-form
                    # string and can contain any characters except '{' '}'
                    fmt_start = i - chunk_start
                i += 1
            else:
                raise SyntaxError("f-string: '{' was never closed")

            expr_part = source[chunk_start:i]
            last_f_token = '}'

            if fmt_start is not None:
                # drop the delimiting ':'
                fmt = _parse_format_string(expr_part[fmt_start + 1 :])
                expr_part = expr_part[:fmt_start]
            else:
                fmt = None

            conversion = -1
            if len(expr_part) >= 2 and expr_part[-2] == '!':
                last_f_token = '!'
                if expr_part[-1] == 's':
                    conversion = 115
                if expr_part[-1] == 'r':
                    conversion = 114
                if expr_part[-1] == 'a':
                    conversion = 97
                else:
                    raise SyntaxError(
                        f"f-string: invalid conversion character {expr_part[-1]!r}: expected 's', 'r', or 'a'"
                    )
                expr_part = expr_part[:-2]

            expr_end = len(expr_part) - 1
            while expr_end >= 0:
                if expr_part[expr_end] == ' ':
                    expr_end -= 1
                    continue
                if expr_part[expr_end] == '=':
                    last_f_token = '='
                    str_parts.append(ast.Constant(expr_part))
                    expr_part = expr_part[:expr_end]
                    if conversion == -1:
                        if fmt is None:
                            conversion = 114
                        else:
                            conversion = 115
                break
            expr_part = expr_part.strip()

            if not expr_part:
                raise SyntaxError(
                    f'f-string: valid expression required before {last_f_token!r}'
                )
            expr_ast = ast.parse(expr_part, mode='eval').body

            str_parts.append(ast.FormattedValue(expr_ast, conversion, fmt))
            chunk_start = i + 1
        i += 1

    if chunk_start < len(source):
        str_parts.append(ast.Constant(source[chunk_start:]))
    for j, part in enumerate(str_parts):
        if isinstance(part, ast.Constant):
            str_parts[j] = ast.Constant(
                part.value.replace('}}', '}').replace('{{', '{')
            )

    return ast.JoinedStr(str_parts)
