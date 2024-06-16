from pathlib import Path

import flex_kino_project_tests


def abs_path_from_project(relative_path: str):
    if not relative_path:
        raise ValueError("Relative path is None or empty")

    return (
        Path(flex_kino_project_tests.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
