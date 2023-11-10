import subprocess
import argparse
import logging

from multiprocessing import Pool


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_subprocess(command, shell=True, universal_newlines=True):
    """
    Run a subprocess command and log the output.

    :param command: The command to run.
    :return: The output of the command.
    :raises: RuntimeError if the command fails.
    """
    try:
        logger.info("Running command: %s", command)
        output = subprocess.check_output(command, shell=shell, universal_newlines=universal_newlines)
        logger.info("Command output:\n%s", output)
        return output
    except subprocess.CalledProcessError as e:
        error_message = f"Command failed with exit code {e.returncode}"
        logger.error(error_message)
        raise RuntimeError(error_message)
    
def run_subprocesses_consecutively(commands, shell=True, universal_newlines=True):
    """
    Run multiple subprocess commands consecutively and log their output.

    :param commands: A list of commands to run.
    :return: A list of the outputs of the commands.
    :raises: RuntimeError if any of the commands fail.
    """
    outputs = []
    for command in commands:
        outputs.append(run_subprocess(command, shell, universal_newlines))
    
    return outputs

def run_subprocesses_parallelly(commands, pool_size=None):
    """
    Run multiple subprocess commands in parallel and log their output.

    :param commands: A list of commands to run.
    :param pool_size: The number of processes to run in parallel (default is the number of CPU cores).
    :return: A list of the outputs of the commands.
    :raises: RuntimeError if any of the commands fail.
    """
    outputs = []
    
    if pool_size is None:
        pool_size = None  # Use the number of CPU cores
    
    with Pool(pool_size) as pool:
        pool.map(run_subprocess, commands)
    
    return outputs
    
def main():
    parser = argparse.ArgumentParser(description="Run subprocess commands consecutively or in parallel.")
    parser.add_argument("commands", nargs="*", help="Commands to execute consecutively or in parallel.")
    parser.add_argument("--pool-size", type=int, help="Number of processes to run in parallel.")
    args = parser.parse_args()

    if not args.commands:
        logger.warning("Will execute one or many commands concurrently.")
        logger.warning("Usage: python executor.py <first_command>")
        logger.warning("Usage: python executor.py <first_command> <second_command> ...")
        return

    if args.pool_size is not None:
        logger.info(f"Running commands in parallel with a pool size of {args.pool_size}.")
        run_subprocesses_parallelly(args.commands, args.pool_size)
    else:
        logger.info("Running commands consecutively.")
        run_subprocesses_consecutively(args.commands)

if __name__ == "__main__":
    main()