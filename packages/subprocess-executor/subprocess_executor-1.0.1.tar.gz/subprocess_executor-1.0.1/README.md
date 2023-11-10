# `Subprocess Executor`

Subprocess Executor is a Python script that allows you to run multiple subprocess commands either consecutively or in parallel using Python's `subprocess` module and the `multiprocessing` library. It provides a convenient way to execute commands and log their output.

## Usage

### `Running Commands Consecutively`

You can run one or more commands `consecutively` by providing them as arguments when executing the script:

```bash
python executor.py <first_command>
python executor.py <first_command> <second_command> ...
```

### `Running Commands in Parallel`

To run commands in `parallel`, you can specify the number of processes to run in parallel using the `--pool-size` option:

```bash
python executor.py --pool-size <number_of_processes> <command1> <command2> ...
```

### License

This script is released under the `MIT` License.
