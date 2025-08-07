from invoke import task
import shutil
import sys
from pathlib import Path


@task
def clean(c):
    """Clean build artifacts"""
    patterns = ["build", "dist", "*.egg-info", "**/__pycache__"]
    for pattern in patterns:
        for path in Path().glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Removed {path}")
            else:
                path.unlink()
                print(f"Removed {path}")


@task
def build(c):
    """Build distribution packages using Flit"""
    clean(c)
    c.run("python -m flit build")
    print("\nBuild complete! Packages are in dist/")


@task
def check_dist(c):
    """Check distribution packages with twine"""
    c.run("python -m twine check dist/*")


@task
def deploy(c, repository="pypi"):
    """Deploy to PyPI or TestPyPI
    
    Args:
        repository: Either 'pypi' or 'testpypi' (default: 'pypi')
    """
    if repository not in ["pypi", "testpypi"]:
        print(f"Error: repository must be 'pypi' or 'testpypi', got '{repository}'")
        sys.exit(1)
    
    # Check if dist directory exists and has files
    dist_path = Path("dist")
    if not dist_path.exists() or not list(dist_path.glob("*")):
        print("No distribution files found. Run 'invoke build' first.")
        sys.exit(1)
    
    # Check the distribution files
    check_dist(c)
    
    # Deploy to PyPI
    cmd = f"python -m twine upload --repository {repository}"
    cmd += " dist/*"
    
    print(f"\nDeploying to {repository}...")
    c.run(cmd)


@task
def test_deploy(c):
    """Build and deploy to TestPyPI"""
    build(c)
    deploy(c, repository="testpypi")


@task
def release(c):
    """Build and deploy to PyPI"""
    build(c)
    deploy(c, repository="pypi")


@task
def dev(c):
    """Install package in development mode"""
    c.run("python -m flit install --symlink")


@task
def lint(c):
    """Run linting (placeholder for future linting setup)"""
    print("No linters configured yet. Consider adding ruff or flake8.")


@task
def test(c):
    """Run tests (placeholder for future test setup)"""
    print("No tests configured yet. Consider adding pytest.")