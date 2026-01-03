"""hca init - Initialize .claude in current project."""

import shutil
from datetime import datetime
from pathlib import Path
from typing import List

import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from cli.core.config import CLAUDE_DIR, COMPONENTS, DEFAULT_BRANCH, DEFAULT_SOURCE
from cli.core.deployer import Deployer
from cli.core.git_ops import GitOps

console = Console()


@click.command("init")
@click.option(
    "--source",
    "-s",
    default=DEFAULT_SOURCE,
    help="Source repository URL or local path",
)
@click.option(
    "--branch",
    "-b",
    default=DEFAULT_BRANCH,
    help="Source repository branch",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force overwrite without backup confirmation",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Preview operations without executing",
)
@click.option("--agents-only", is_flag=True, help="Only deploy agents")
@click.option("--commands-only", is_flag=True, help="Only deploy commands")
@click.option("--skills-only", is_flag=True, help="Only deploy skills")
@click.option(
    "--select",
    is_flag=True,
    help="Interactively select components to deploy",
)
@click.pass_context
def init_cmd(
    ctx: click.Context,
    source: str,
    branch: str,
    force: bool,
    dry_run: bool,
    agents_only: bool,
    commands_only: bool,
    skills_only: bool,
    select: bool,
) -> None:
    """Initialize Happy Coding Agent in the current project."""
    cwd = Path.cwd()
    claude_dir = cwd / CLAUDE_DIR
    verbose = ctx.obj.get("verbose", False)
    git_ops = GitOps()

    # 1. Check if current directory is a git repository
    if not git_ops.is_git_repo(cwd):
        if not Confirm.ask(
            "[yellow]Warning:[/] Current directory is not a git repository. Continue?",
            default=False,
        ):
            raise click.Abort()

    # 2. Determine components to deploy
    components = _determine_components(
        agents_only, commands_only, skills_only, select
    )

    if not components:
        console.print("[red]No components selected. Aborting.[/]")
        raise click.Abort()

    # 3. Handle existing .claude directory
    if claude_dir.exists():
        _handle_existing_claude(claude_dir, force, dry_run)

    # 4. Fetch source configuration
    console.print(f"\n[blue]Fetching configuration from:[/] {source} ({branch})")

    deployer = Deployer(source, branch, verbose=verbose)

    if dry_run:
        console.print("\n[yellow]Dry run mode - no changes will be made[/]")
        _preview_deployment(deployer, components)
        return

    # 5. Execute deployment
    try:
        with console.status("[bold green]Deploying..."):
            result = deployer.deploy(cwd, components)
        _show_deployment_summary(result)
    except Exception as e:
        console.print(f"[red]Deployment failed:[/] {e}")
        raise click.Abort()


def _determine_components(
    agents_only: bool,
    commands_only: bool,
    skills_only: bool,
    select: bool,
) -> List[str]:
    """Determine which components to deploy based on options."""
    if agents_only:
        return ["agents"]
    if commands_only:
        return ["commands"]
    if skills_only:
        return ["skills"]

    if select:
        # Interactive selection
        console.print("\n[bold]Select components to deploy:[/]")
        components = []
        if Confirm.ask("  Deploy agents?", default=True):
            components.append("agents")
        if Confirm.ask("  Deploy commands?", default=True):
            components.append("commands")
        if Confirm.ask("  Deploy skills?", default=True):
            components.append("skills")
        return components

    # Default: deploy all
    return COMPONENTS.copy()


def _handle_existing_claude(claude_dir: Path, force: bool, dry_run: bool) -> None:
    """Handle existing .claude directory."""
    console.print("\n[yellow]Existing .claude directory found[/]")

    if dry_run:
        console.print("  Would handle existing directory based on options")
        return

    if force:
        _backup_and_remove(claude_dir)
        return

    # Interactive prompt
    choice = Prompt.ask(
        "How to handle existing configuration?",
        choices=["backup", "overwrite", "abort"],
        default="backup",
    )

    if choice == "abort":
        raise click.Abort()
    elif choice == "backup":
        _backup_and_remove(claude_dir)
    elif choice == "overwrite":
        shutil.rmtree(claude_dir)
        console.print("  [yellow]Removed existing .claude directory[/]")


def _backup_and_remove(claude_dir: Path) -> None:
    """Backup existing .claude directory and remove it."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = claude_dir.parent / f".claude-backup-{timestamp}"

    shutil.move(str(claude_dir), str(backup_dir))
    console.print(f"  [green]Backed up to:[/] {backup_dir.name}")


def _preview_deployment(deployer: Deployer, components: List[str]) -> None:
    """Preview what would be deployed."""
    console.print("\n[bold]Components to deploy:[/]")

    table = Table(show_header=True, header_style="bold")
    table.add_column("Component")
    table.add_column("Files/Directories")

    manifest = deployer.get_manifest()

    for component in components:
        items = manifest.get(component, [])
        table.add_row(component, ", ".join(items[:5]) + ("..." if len(items) > 5 else ""))

    console.print(table)


def _show_deployment_summary(result: dict) -> None:
    """Show deployment summary."""
    console.print("\n" + "=" * 50)
    console.print("[bold green]Deployment Complete![/]")
    console.print("=" * 50)

    table = Table(show_header=True, header_style="bold")
    table.add_column("Component")
    table.add_column("Status")
    table.add_column("Files")

    for component, info in result["components"].items():
        status = "[green]OK[/]" if info["success"] else "[red]FAILED[/]"
        table.add_row(component, status, str(info["count"]))

    console.print(table)

    console.print(f"\n[dim]Version: {result['version']}[/]")
    console.print(f"[dim]Commit: {result['commit'][:8]}[/]")
    console.print("\n[bold]Next steps:[/]")
    console.print("  1. Review deployed configurations in .claude/")
    console.print("  2. Run 'hca status' to verify deployment")
    console.print("  3. Start using /feature-analyzer and other commands!")
