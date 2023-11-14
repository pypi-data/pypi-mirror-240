"""Python CLI for flashxtest"""

import os
import subprocess
import click
import pkg_resources
import warnings

from .. import api


@click.group(name="flashxtest", invoke_without_command=True)
@click.pass_context
@click.option("--version", "-v", is_flag=True)
def flashxtest(ctx, version):
    """
    \b
    Command line interface for managing
    Flash-X testing framework. Type --help
    for individual commands to learn more.
    """
    if ctx.invoked_subcommand is None and not version:
        subprocess.run(
            f"export PATH=~/.local/bin:/usr/local/bin:$PATH && flashxtest --help",
            shell=True,
            check=True,
        )

    if version:
        click.echo(pkg_resources.require("FlashXTest")[0].version)


@flashxtest.command(name="init")
@click.option(
    "--source",
    "-z",
    default=None,
    type=click.Path(exists=True),
    help="Flash-X source directory",
)
@click.option("--site", "-s", default=None, type=click.STRING, help="Flash-X site name")
@click.option(
    "--local-archive",
    "-a",
    default=None,
    type=click.Path(exists=False),
    help="Path to local archive",
)
@click.option(
    "--main-archive",
    "-m",
    default=None,
    type=click.Path(exists=False),
    help="Path to main archive",
)
@click.option(
    "--outdir",
    "-o",
    default=None,
    type=click.Path(exists=False),
    help="Path to results directory",
)
@click.option(
    "--mpi-cmd",
    "-mpi",
    default="mpiexec",
    type=click.STRING,
    help="MPI command mpiexec/mpirun/aprun",
)
@click.option(
    "--make-cmd-opts",
    "-make",
    default="make",
    type=click.STRING,
    help="Gmake command and options",
)
@click.option(
    "--view-archive",
    "-vv",
    default=None,
    help="Path to view archive",
)
def init(
    source,
    site,
    local_archive,
    main_archive,
    view_archive,
    outdir,
    mpi_cmd,
    make_cmd_opts,
):
    """
    \b
    Initialize site specific configuration.

    \b
    This command is used to setup site specific
    configuration for your testing environment
    using "config" and "execfile".

    \b
    This command will not replace exisiting
    "config" or "execfile" in the working
    directory. To edit existing site specific
    configuration, "config" and "execfile"
    should be edited directly.
    """
    api.init(
        flashSite=site,
        pathToFlash=source,
        pathToLocalArchive=local_archive,
        pathToMainArchive=main_archive,
        pathToViewArchive=view_archive,
        pathToOutdir=outdir,
        pathToMPI=mpi_cmd,
        pathToGmake=make_cmd_opts,
    )


@flashxtest.command(name="setup-suite")
@click.argument("suitelist", type=click.Path(exists=True), nargs=-1)
@click.option(
    "--overwrite", is_flag=True, help="Overwrite current test.info in working directory"
)
@click.option(
    "--add-setup-opts",
    "-as",
    default=None,
    help="Add common setup options to all tests",
)
@click.option("--seed-from-info", "-i", default=None, help="Seed info file")
def setup_suite(suitelist, overwrite, add_setup_opts, seed_from_info):
    """
    \b
    Create a "test.info" from a list of suite files.

    \b
    This command accepts multiple files with suffix,
    ".suite" to build a "test.info". If no arguments are
    supplied, all "*.suite" files are used from the working
    directory.

    \b
    The ".suite" files represent a collection of mutually
    exclusive test specifications associated with a "config" file.
    Each line in a file represent a unique test specification
    defined as,

    \b
        incompFlow/LidDrivenCavity -t "UnitTest/LidDrivenCavity/AMReX/2d" -np 4 --debug
    \b
        Sod -t "Composite/Sod/PseudoUG/2d/AMReX/simpleUnsplit" -np 4 -cbase 2023-01-13 -rbase 2023-01-14
    \b
        Sod -t "Comparison/Sod/UG/2d/simpleUnsplit" -np 1 -e OMP_NUM_THREADS=1 -e OMP_STACKSIZE=16M -cbase 2023-01-13

    \b
    The first value represents a Flash-X setup defined in
    source/Simulation/SimulationMain directory with following
    options,

    \b
    -t, --test             TEXT     Defined in */tests/tests.yaml
    -np, --nprocs          INTEGER  Number of processors
    -cbase, --cbase        TEXT     Date for comparsion benchmark
    -rbase, --rbase        TEXT     Date for restart benchmark
    -tol, --tolerance      FLOAT    Tolerance for comparsion and composite tests
    -e, --env              TEXT     Environment variables
    -debug, --debug        BOOLEAN  Debug test
    -as, --add-setup-opts  TEXT     Additional setup options
    """
    api.setup_suite(
        pathToSuites=suitelist,
        overwriteCurrInfo=overwrite,
        addSetupOptions=add_setup_opts,
        seedFromInfo=seed_from_info,
    )


@flashxtest.command(name="run-suite")
@click.option("--archive", is_flag=True, show_default=True, help="Archive test results")
@click.option(
    "--skip-viewarchive",
    is_flag=True,
    show_default=True,
    help="Skip saving results to view archive",
)
@click.option(
    "--skip-mainarchive",
    is_flag=True,
    show_default=True,
    help="Skip saving results to main archive",
)
def run_suite(archive, skip_viewarchive, skip_mainarchive):
    """
    \b
    Run the test suite using "test.info".

    \b
    This command runs all the tests defined in
    "test.info", and conveys errors.
    """
    api.run_suite(
        saveToArchive=archive,
        skipViewArchive=skip_viewarchive,
        skipMainArchive=skip_mainarchive,
    )


@flashxtest.command(name="check-suite")
@click.argument("suitelist", type=click.Path(exists=True), nargs=-1)
def check_suite(suitelist):
    """
    \b
    Check and report changes to "test.info".

    \b
    This command will compare "test.info"
    with "suite" files and report if changes
    are detected
    """
    api.check_suite(pathToSuites=suitelist)


@flashxtest.command(name="show-specs")
@click.argument("setupname", type=str, required=True)
def show_specs(setupname):
    """
    \b
    Show available tests for a given setup name

    \b
    This command prints tests located in tests/test.yaml
    for a given simulation name.
    """
    api.show_specs(setupName=setupname)


@flashxtest.command(name="dry-run")
@click.argument("setupname", type=str, required=True)
@click.option("--test", "-t", type=str, required=True)
@click.option("--nprocs", "-np", type=str, required=True)
@click.option("--objdir", "-ob", type=str, default="object")
def dry_run(setupname, test, nprocs, objdir):
    """
    \b
    Compile and run a test defined for a specific setup

    \b
    This command compiles and runs a test defined
    in tests.yaml for a specific setup. Note that
    this command does not perform testing for
    "cbase" and "rbase" benchmarks. Use "run-suite"
    command for that.
    """
    api.dry_run(
        setupName=setupname,
        nodeName=test,
        numProcs=nprocs,
        objDir=os.path.join(os.getcwd(), objdir),
        runTest=True,
    )


@flashxtest.command(name="webview")
def webview():
    """
    \b
    Launch FlashTestView

    \b
    This command will launch FlashTestView web interface
    """
    api.webview()


@flashxtest.command(name="remove-benchmarks")
@click.argument("suitelist", type=click.Path(exists=True), nargs=-1, required=True)
@click.option("--date", "-dd", default=None, help="Date for benchmarks to be removed")
@click.option("--strip-comments", is_flag=True, help="Strip comments")
def remove_benchmarks(suitelist, date, strip_comments):
    """
    \b
    Remove -cbase and -rbase entries from suite files

    \b
    This command accepts multiple files with suffix,
    ".suite" and removes benchmarks from Comparison
    and Composite tests. You can use the --date option
    to restrict the removal process specific dates.
    The default behavior is to remove all benchmarks
    """
    api.remove_benchmarks(
        pathToSuites=suitelist,
        cbaseDate=date,
        rbaseDate=date,
        stripComments=strip_comments,
    )


@flashxtest.command(name="add-cbase")
@click.argument("suitelist", type=click.Path(exists=True), nargs=-1, required=True)
@click.argument("date", required=True)
def add_cbase(suitelist, date):
    """
    \b
    Add missing -cbase values in suite files

    \b
    This command accepts multiple files with suffix,
    ".suite" and populates missing comparision benchmark
    tag for Comparison and Composite tests.
    """
    api.add_cbase(pathToSuites=suitelist, cbaseDate=date)


@flashxtest.command(name="add-rbase")
@click.argument("suitelist", type=click.Path(exists=True), nargs=-1, required=True)
@click.argument("date", required=True)
def add_rbase(suitelist, date):
    """
    \b
    Add missing -rbase values in suite files

    \b
    This command accepts multiple files with suffix,
    ".suite" and populates missing restart benchmark
    tag for Composite tests.
    """
    api.add_rbase(pathToSuites=suitelist, rbaseDate=date)
