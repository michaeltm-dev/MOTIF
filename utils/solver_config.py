import ast
import os

from omegaconf import DictConfig, OmegaConf


def normalize_solver_config(solver_config: DictConfig) -> DictConfig:
    """Populate solver fields that are intentionally omitted from YAML."""
    base_path = str(solver_config.base_path)
    problem, algorithm = _infer_problem_and_algorithm(base_path)

    OmegaConf.update(solver_config, "problem", problem, force_add=True)
    OmegaConf.update(solver_config, "algorithm", algorithm, force_add=True)
    OmegaConf.update(solver_config, "eval_script", os.path.join(base_path, "eval.py"), force_add=True)

    functions = []
    for entry in solver_config.functions:
        strategy_id = _get_strategy_id(entry)
        path = _get_strategy_path(entry, base_path, strategy_id)
        name = _get_strategy_name(entry, path)
        functions.append({"id": strategy_id, "name": name, "path": path})

    OmegaConf.update(solver_config, "functions", functions, force_add=True)
    return solver_config


def _infer_problem_and_algorithm(base_path: str) -> tuple[str, str]:
    slug = os.path.basename(os.path.normpath(base_path))
    parts = slug.split("_", 1)
    problem = parts[0].upper()
    algorithm = parts[1].upper() if len(parts) > 1 else ""
    return problem, algorithm


def _get_strategy_id(entry) -> str:
    if isinstance(entry, str):
        return entry
    return str(entry.id)


def _get_strategy_path(entry, base_path: str, strategy_id: str) -> str:
    if isinstance(entry, DictConfig) and "path" in entry:
        return str(entry.path)
    return os.path.join(base_path, f"{strategy_id}.py")


def _get_strategy_name(entry, path: str) -> str:
    if isinstance(entry, DictConfig) and "name" in entry:
        return str(entry.name)

    with open(path, "r", encoding="utf-8") as f:
        module = ast.parse(f.read(), filename=path)

    for node in module.body:
        if isinstance(node, ast.FunctionDef):
            return node.name

    raise ValueError(f"No function definition found in {path}")
