import ast
import os
from typing import List, Set, Union

AST_BODY_NODE: str = "body"
AST_NODES: List[str] = ["orelse", "handlers", "finalbody"]


def extract_imports_recursive(ast_obj: ast.Module) -> Set:
    """
    @param path: the AST Module
    @return: the module names that imported in code
    """
    imports_list = set()

    def extract_imports(
        ast_obj: Union[ast.Module, ast.stmt]
    ):
        if hasattr(ast_obj, AST_BODY_NODE):
            for ast_body_item in ast_obj.body:
                extract_imports(
                    ast_obj=ast_body_item,
                )

        for ast_node in AST_NODES:
            if hasattr(ast_obj, ast_node):
                for ast_node_item in getattr(ast_obj, ast_node):
                    extract_imports(
                        ast_obj=ast_node_item
                    )

        if isinstance(ast_obj, ast.Import):
            for module_name in ast_obj.names:
                imports_list.add(module_name.name.split('.')[0])

        if isinstance(ast_obj, ast.ImportFrom):
            # Ignore relative imports
            if not ast_obj.level:
                imports_list.add(ast_obj.module.split('.')[0])

    extract_imports(ast_obj)

    return imports_list


def get_imports_of_file(path: str) -> Set[str]:
    """
    @param path: the file path
    @return: the module names that imported in file
    """

    with open(path, encoding='utf-8') as file_obj:
        code = file_obj.read()

    try:
        return extract_imports_recursive(ast.parse(code))
    except Exception:
        return set()


def is_project_python_file(directory_path: str, filename: str) -> bool:
    return os.path.splitext(filename)[1] == '.py' and \
           'site-packages' not in directory_path


def get_all_python_files(root_path: str) -> List[str]:
    """
    @param root_path: the root path
    @return: the python file paths under the root path
    """
    project_files = [os.path.join(directory_path, filename)
                     for directory_path, _, filenames in os.walk(root_path)
                     for filename in filenames if is_project_python_file(directory_path, filename)]
    return project_files


def get_all_imports_of_project(project_path: str) -> List[str]:
    """
    @param root_path: the project path
    @return: the module names that imported in all files of the project
    """
    project_files = get_all_python_files(project_path)
    imports = set()
    for file in project_files:
        file_imports = get_imports_of_file(file)
        imports.update(file_imports)
    return sorted(list(imports))
