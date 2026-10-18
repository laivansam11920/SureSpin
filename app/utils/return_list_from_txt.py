from pathlib import Path


def return_list() -> tuple[list, list]:
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    gift_path: Path = BASE_DIR / "list_gift.txt"
    name_path: Path = BASE_DIR / "list_name.txt"

    with open(gift_path, "r", encoding="utf-8") as f:
        list_gift = [line.strip() for line in f.readlines()]
    with open(name_path, "r", encoding="utf-8") as f:
        list_names = [line.strip() for line in f.readlines()]

    return list_gift, list_names
