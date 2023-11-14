#!/usr/bin/env python3
import logging
import sys
import pathlib
import fire

from text_fancipy import __version__

__author__ = "Adam Twardoch"
__copyright__ = "(c) 2023 Adam Twardoch"
__license__ = "Apache-2.0"

_logger = logging.getLogger(__name__)


def create_tables() -> dict:
    """
    Create translation tables for different font styles.

    Returns:
        dict: A dictionary where each key is a style and each value is a tuple
              of two translation tables (normal and reverse) and the fancified style name.
    """
    styles = {
        # Style mappings with fancified names
        "dflt": ("A", "a", "Default"),
        "mono": ("𝙰", "𝚊", "𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎"),
        "bold": ("𝐀", "𝐚", "𝐁𝐨𝐥𝐝"),
        "ital": ("𝐴", "𝑎", "𝐼𝑡𝑎𝑙𝑖𝑐"),
        "bdit": ("𝑨", "𝒂", "𝑩𝒐𝒍𝒅 𝑰𝒕𝒂𝒍𝒊𝒄"),
        "sans": ("𝖠", "𝖺", "𝖲𝖺𝗇𝗌-𝗌𝖾𝗋𝗂𝖿"),
        "snbd": ("𝗔", "𝗮", "𝗦𝗮𝗻𝘀-𝘀𝗲𝗿𝗶𝗳 𝗕𝗼𝗹𝗱"),
        "snit": ("𝘈", "𝘢", "𝘚𝘢𝘯𝘴-𝘴𝘦𝘳𝘪𝘧 𝘐𝘵𝘢𝘭𝘪𝘤"),
        "snbi": ("𝘼", "𝙖", "𝙎𝙖𝙣𝙨-𝙨𝙚𝙧𝙞𝙛 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘"),
        "dbst": ("𝔸", "𝔞", "𝔻𝕠𝕦𝕓𝕝𝕖-𝕤𝕥𝕣𝕦𝕔𝕜"),
        "bscr": ("𝓐", "𝓪", "𝓑𝓸𝓵𝓭 𝓢𝓬𝓻𝓲𝓹𝓽"),
    }

    tables = {}
    for s, (uc, lc, fancy_name) in styles.items():
        upper_mapping = {
            i: i + ord(uc) - ord("A") for i in range(ord("A"), ord("Z") + 1)
        }
        lower_mapping = {
            i: i + ord(lc) - ord("a") for i in range(ord("a"), ord("z") + 1)
        }
        upper_mapping.update(lower_mapping)

        reverse_upper_mapping = {v: k for k, v in upper_mapping.items()}

        tables[s] = (
            str.maketrans(upper_mapping),
            str.maketrans(reverse_upper_mapping),
            fancy_name,
        )

    return tables


_precomputed_tables = create_tables()


def get_table(style: str, reverse: bool) -> dict:
    """
    Retrieve the translation table for a given style and direction.

    Args:
        style (str): The style of the text.
        reverse (bool): Whether to use the reverse translation table.

    Returns:
        dict: The translation table.
    """
    return _precomputed_tables.get(style, (None, None))[reverse]


def fancipy(text: str, style: str) -> str:
    """
    Convert plain English letters in text to a fancy-styled text.

    Args:
        text (str): The text to convert.
        style (str): The style to apply.

    Returns:
        str: The converted text.
    """
    return text.translate(get_table(style, False))


def unfancipy(text: str, style: str) -> str:
    """
    Convert fancy-styled text of a given style back to plain text.

    Args:
        text (str): The text to convert.
        style (str): The style of the input text.

    Returns:
        str: The converted text.
    """
    return text.translate(get_table(style, True))


def unfancipy_all(text: str) -> str:
    """
    Convert all fancy-styled text back to plain text.

    Args:
        text (str): The text to convert.

    Returns:
        str: The converted text.
    """
    for style in _precomputed_tables:
        text = text.translate(get_table(style, True))
    return text
