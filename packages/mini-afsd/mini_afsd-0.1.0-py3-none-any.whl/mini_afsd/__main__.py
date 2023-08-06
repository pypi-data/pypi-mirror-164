# -*- coding: utf-8 -*-
"""The main function of mini_afsd for use from the command line."""

import argparse

from mini_afsd import Controller


def main():
    """The command line interface for the package."""
    parser = argparse.ArgumentParser(
        description=('Creates a log of all commits to the specified git branch after '
                     'the specified start data, collects them into sections, and '
                     'formats a new entry for the changelog, output as new_changes.rst.')
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='If specified, will print out all input arguments.'
    )
    parser.add_argument(
        '--xyStepsPerMil', '-XYS', default=40, type=int,
        help=('something')
    )
    parser.add_argument(
        '--xyPulPerStep', '-XYP', default=2, type=int,
        help=('something')
    )
    parser.add_argument(
        '--aStepsPerMil', '-AS', default=1020, type=int,
        help=('something')
    )
    parser.add_argument(
        '--aPulPerStep', '-AP', default=4, type=int,
        help=('something')
    )
    parser.add_argument(
        '--port_regex', '-P', default='(CP21)', type=str,
        help=(
            'The regular expression to use for searching for the port to use. Default is "(CP21)".'
        )
    )
    # store_false means default is True and turns to False if flag is specified
    parser.add_argument(
        '--connect_serial', '-C', action='store_false',
        help=(
            'If specified, will not try to connect to the serial port for '
            'controlling mill movement.'
        )
    )
    # store_true means default is False and turns to True if flag is specified
    parser.add_argument(
        '--labjack_force', '-LF', action='store_true',
        help='If specified, will use the LabJack to measure the force during deposition.'
    )

    args = parser.parse_args()
    if args.port_regex.startswith('"') or args.port_regex.startswith("'"):
        # input was a nested string
        args.port_regex = args.port_regex[1:-1]
    if args.verbose:
        print(f'The input arguments were: {args}\n')

    Controller(
        xyStepsPerMil=args.xyStepsPerMil, xyPulPerStep=args.xyPulPerStep,
        aStepsPerMil=args.aStepsPerMil, aPulPerStep=args.aPulPerStep,
        port_regex=args.port_regex, connect_serial=args.connect_serial,
        labjack_force=args.labjack_force
    ).run()


if __name__ == '__main__':

    main()
