from arkdata.models import build_all, drop_all
from arkdata.seeds import seed



def rebuild():
    drop_all()
    build_all()
    seed()


if __name__ == "__main__":
    from pathlib import Path
    import arkdata
    rebuild()
