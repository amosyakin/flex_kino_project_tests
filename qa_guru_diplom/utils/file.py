from pathlib import Path

import qa_guru_diplom


def abs_path_from_project(relative_path: str):
    if not relative_path:
        raise ValueError("Relative path is None or empty")

    return (
        Path(qa_guru_diplom.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
