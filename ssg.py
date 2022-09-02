import typer
from ssg.site import Site


def main(source: str = "content", dest: str = "dist"):
    config = {
        "source": source,
        "dest": dest
    }
    Site(**config).build()


typer.run(main)
