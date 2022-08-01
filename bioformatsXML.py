"""
Entrypoint
"""
import argparse
from pathlib import Path
import logging

from bioformatsXML import BioformatsXML


def get_args() -> argparse.Namespace:
    """
    Get the arguments from the commandline
    :return:
    """
    myparser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    myparser.add_argument(
        "-d",
        type=str,
        help="Directory: Runs on all bioformats compatible files.",
        default=Path.cwd(),
    )
    myparser.add_argument(
        "-f",
        type=str,
        help="File: Run on single file.",
        default='',
    )
    myparser.add_argument(
        "-l",
        type=str,
        help="LogLevel: 0 error (default), 1 warning, 2 info",
        default=0,
    )
    return myparser.parse_args()


def load_files(args: argparse.Namespace) -> None:
    pth = Path(args.d)
    files = [x for x in pth.glob('*') if x.is_file()]
    bfx = BioformatsXML()
    for file in files:
        xml = bfx.get_xml(file)
        if xml:
            out = Path(file.parent, file.stem + '.xml')
            xml.write(out)
            logging.info(f'Wrote {out}')
            if not bfx.verify_schema(out):
                logging.error(f'Invalid xml: {out}')
            else:
                logging.info(f'Validated {out}')


def load_file(args: argparse.Namespace) -> None:
    file = Path(args.f)
    bfx = BioformatsXML()
    xml = bfx.get_xml(file)
    if xml:
        out = Path(file.parent, file.stem + '.xml')
        xml.write(out)
        logging.info(f'Wrote {out}')


if __name__ == "__main__":
    args = get_args()
    loglevels = [logging.ERROR, logging.WARNING, logging.INFO]
    loglevel = loglevels[int(args.l)]
    logging.basicConfig(level=loglevel)
    logging.info('Arguments parsed')
    logging.info(f"Loglevel: {logging.getLevelName(loglevel)}")
    if args.f:
        load_file(args)
    else:
        load_files(args)
