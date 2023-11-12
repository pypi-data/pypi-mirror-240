import click
from tidydata.config import ProjectMeta
from pathlib import Path
from loguru import logger
import re
from typeguard import typechecked
from datetime import datetime
import toml
from seedir import seedir
import shutil

__version__ = '0.1.14'

@click.group()
@click.version_option(version=__version__)
def tidydata():
    pass


@tidydata.command()
@click.argument("project")
@typechecked
def new(project: str):
    print(f"Creating project with project name {project}")
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", project):
        raise logger.error(
            f"Project name '{project}' is not string which starts with a letter or the underscore character, and only contains alpha-numeric characters and underscores"
        )

    proj = Path(project).resolve()
    if proj.exists():
        raise logger.error(
            f"file path '{proj}' exists while creating project '{project}'"
        )

    # creating file structure
    try:
        proj.mkdir()
        (proj / "cleaned").mkdir()
        (proj / "raw").mkdir()
        (proj / "project.toml").write_text(
            toml.dumps(
                {
                    "project": {
                        "name": project,
                        "description": "Describe your project here",
                        "date": datetime.now().date(),
                        "sources": "sources.yaml",
                        "actions": "actions.yaml",
                        "export_dir": "cleaned/",
                    }
                }
            )
        )
        (proj / "sources.yaml").touch(exist_ok=False)
        (proj / "actions.yaml").touch(exist_ok=False)
        (proj / "README.md").touch(exist_ok=False)
        (proj / "cleaned" / "README.md").touch(exist_ok=False)
        (proj / "raw" / "README.md").touch(exist_ok=False)
        print(f"Sucessfully created project {project} in directory {proj}.")
        print(f"Project initial structure: ")
        seedir(proj, style="emoji")
        print(
            f"Please change your work directory to your newly created directory: '{proj}', and enjoy your working time!"
        )
        print(f"Read the documentation at https://gtdata.ren for more detailed guides.")
    except Exception as e:
        if proj.exists():
            shutil.rmtree(proj)
        raise logger.error(f"An error occurs while creating project: {e}")


@tidydata.command()
def run():
    logger.info(
        f"==> Checking the existence of config files: 'project.toml', 'sources.yaml', and 'actions.yaml'"
    )

    if not Path("project.toml").exists():
        raise logger.error(f"'project.toml' file does not exists in current directory")
    if not Path("sources.yaml").exists():
        raise logger.error(f"'sources.yaml' file does not exists in current directory")
    if not Path("actions.yaml").exists():
        raise logger.error(f"'actions.yaml' file does not exists in current directory")


    logger.info(f"==> Loading config files as Config object")
    conf = ProjectMeta.from_toml("project.toml")
    logger.info(
        f"==> Cleaning data"
    )
    conf.run()

    logger.info(
        f"All done!!! Cleaned data is in the directory {conf.export_dir}"
    )
    




if __name__ == "__main__":
    tidydata()
