import ast
import builtins


def get_function_from_input(input_code, function_name):
    try:
        parsed_ast = ast.parse(input_code, mode='exec')
        function = next(
            (node for node in ast.walk(parsed_ast) if isinstance(node, ast.FunctionDef) and node.name == function_name),
            None)
        if function:
            globals_dict = {'__builtins__': builtins}
            exec(compile(parsed_ast, filename='<string>', mode='exec'), globals_dict)
            return globals_dict[function_name]
        else:
            raise AttributeError(f"Функция {function_name} не найдена во вводе.")
    except SyntaxError:
        raise SyntaxError("Недопустимый синтаксис ввода.")
    except KeyError:
        raise KeyError(f"Функция {function_name} не найдена во вводе.")


def input_from_text(func_text):
    #func_text = input("Введите функцию:")
    input_code = """
def my_function(x, y):
    return """ + func_text

    function_name = "my_function"
    return get_function_from_input(input_code, function_name)

