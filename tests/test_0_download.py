import os
from pathlib import Path

import responses

from wikidict import download
from wikidict.constants import BASE_URL, DUMP_URL

WIKTIONARY_INDEX = """<html>
<head><title>Index of /frwiktionary/</title></head>
<body bgcolor="white">
<h1>Index of /frwiktionary/</h1><hr><pre><a href="../">../</a>
<a href="20191120/">20191120/</a>                                          02-Jan-2020 01:29                   -
<a href="20191201/">20191201/</a>                                          21-Jan-2020 01:36                   -
<a href="20191220/">20191220/</a>                                          02-Feb-2020 01:28                   -
<a href="20200101/">20200101/</a>                                          21-Feb-2020 01:38                   -
<a href="20200120/">20200120/</a>                                          02-Mar-2020 01:28                   -
<a href="20200201/">20200201/</a>                                          02-Apr-2020 01:36                   -
<a href="20200220/">20200220/</a>                                          24-Feb-2020 17:32                   -
<a href="20200301/">20200301/</a>                                          09-Mar-2020 03:42                   -
<a href="{date}/">{date}/</a>                                          17-Apr-2020 15:20                   -
<a href="latest/">latest/</a>                                            17-Apr-2020 15:20                   -
</pre><hr></body>
</html>
"""


@responses.activate
def test_simple(craft_data):
    """It should download the Wiktionary dump file and extract it."""

    output_dir = Path(os.environ["CWD"]) / "data" / "fr"

    date = "20200417"
    pages_xml = output_dir / f"pages-{date}.xml"
    pages_bz2 = output_dir / f"pages-{date}.xml.bz2"

    # Clean-up before we start
    for file in (pages_xml, pages_bz2):
        file.unlink(missing_ok=True)

    # List of requests responses to falsify:
    #   - fetch_snapshots()
    #   - fetch_pages()
    responses.add(
        responses.GET,
        BASE_URL.format("fr"),
        body=WIKTIONARY_INDEX.format(date=date),
    )
    responses.add(
        responses.HEAD,
        DUMP_URL.format("fr", date),
        headers={},
    )
    responses.add(
        responses.GET,
        DUMP_URL.format("fr", date),
        body=craft_data(date, "fr"),
    )

    # Start the whole process
    assert download.main("fr") == 0

    # Check that files are created
    assert pages_xml.is_file()
    assert pages_bz2.is_file()


@responses.activate
def test_download_already_done(craft_data):
    """It should not download again a processed Wiktionary dump."""

    output_dir = Path(os.environ["CWD"]) / "data" / "fr"

    date = "20200417"
    pages_xml = output_dir / f"pages-{date}.xml"
    pages_bz2 = output_dir / f"pages-{date}.xml.bz2"

    # The BZ2 file was already downloaded
    pages_bz2.write_bytes(craft_data(date, "fr"))

    # List of requests responses to falsify:
    #   - fetch_snapshots()
    responses.add(
        responses.GET,
        BASE_URL.format("fr"),
        body=WIKTIONARY_INDEX.format(date=date),
    )
    responses.add(
        responses.HEAD,
        DUMP_URL.format("fr", date),
        headers={},
    )

    # Start the whole process
    assert download.main("fr") == 0

    # Check that files are created
    assert pages_xml.is_file()
    assert pages_bz2.is_file()


@responses.activate
def test_ongoing_dump(craft_data, capsys):
    """When the dump is not finished on the Wiktionary side, the previous dump should be used."""

    output_dir = Path(os.environ["CWD"]) / "data" / "fr"

    # Clean-up before we start
    for date in ("20200301", "20200514"):
        (output_dir / f"pages-{date}.xml").unlink(missing_ok=True)
        (output_dir / f"pages-{date}.xml.bz2").unlink(missing_ok=True)

    # List of requests responses to falsify:
    #   - fetch_snapshots()
    #   - fetch_pages() for 20200514
    #   - fetch_pages() for 20200301
    responses.add(
        responses.GET,
        BASE_URL.format("fr"),
        body=WIKTIONARY_INDEX.format(date="20200514"),
    )
    responses.add(
        responses.HEAD,
        DUMP_URL.format("fr", "20200514"),
        status=404,
    )
    responses.add(
        responses.HEAD,
        DUMP_URL.format("fr", "20200301"),
        headers={},
    )
    responses.add(
        responses.GET,
        DUMP_URL.format("fr", "20200301"),
        body=craft_data("20200301", "fr"),
    )

    # Start the whole process
    assert download.main("fr") == 0

    # Check that files are created
    assert (output_dir / "pages-20200301.xml").is_file()
    assert (output_dir / "pages-20200301.xml.bz2").is_file()

    # Check that files are not created
    assert not (output_dir / "pages-20200514.xml").is_file()
    assert not (output_dir / "pages-20200514.xml.bz2").is_file()


def test_progress_callback_normal(capsys):
    download.callback_progress("Some text: ", 42 * 1024, False)
    captured = capsys.readouterr()
    assert captured.out == "\rSome text: 43,008 bytes"

    download.callback_progress("Some text: ", 42 * 1024, True)
    captured = capsys.readouterr()
    assert captured.out == "\rSome text: OK [43,008 bytes]\n"

def test_progress_callback_normal_length(capsys):
    download.callback_progress("Some text: ", 42 * 1024, False, length=50 * 1024)
    captured = capsys.readouterr()
    assert captured.out == "\rSome text: 43,008 / 51,200 bytes"

    download.callback_progress("Some text: ", 42 * 1024, True, length=50 * 1024)
    captured = capsys.readouterr()
    assert captured.out == "\rSome text: OK [43,008 bytes]\n"

def test_progress_callback_ci(capsys):
    download.callback_progress_ci("Some text: ", 42 * 1024, False)
    captured = capsys.readouterr()
    assert captured.out == "."

    download.callback_progress_ci("Some text: ", 42 * 1024, True)
    captured = capsys.readouterr()
    assert captured.out == ". OK [43,008 bytes]\n"

def test_progress_callback_ci_length(capsys):
    download.callback_progress_ci("Some text: ", 42 * 1024, False, length=50 * 1024)
    captured = capsys.readouterr()
    assert captured.out == "."

    download.callback_progress_ci("Some text: ", 42 * 1024, True, length=50 * 1024)
    captured = capsys.readouterr()
    assert captured.out == ". OK [43,008 / 51,200 bytes]\n"
