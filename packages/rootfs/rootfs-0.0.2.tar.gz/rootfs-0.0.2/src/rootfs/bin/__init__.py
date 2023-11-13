#!/usr/bin/env python

__all__ = ['main']

import sys
import argparse

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('rootfs')
    parser.add_argument('--root', action='store_true', help="Show root directory")
    parser.add_argument('--list', action='store_true', help="Run ls on root directory")
    parser.add_argument('--find', action='store_true', help="Run find on root directory")
    # TODO: make --list and --find take an argument
    args = parser.parse_args(argv)

    if [args.root, args.list, args.find].count(True) > 1:
        print(f"at most one of --root, --list, --find allowed", file=sys.stderr)
        sys.exit(1)
    if [args.root, args.list, args.find].count(True) == 0:
        parser.print_help()
        sys.exit(1)

    import rootfs

    root = rootfs.root()
    if args.root:
        print(root)
    if args.list:
        print(rootfs.list(root))
    if args.find:
        print(rootfs.find(root))

if __name__ == '__main__':
    main(sys.argv[1:])
