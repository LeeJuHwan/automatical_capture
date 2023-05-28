import argparse


def optional():
    """시스템 파라미터를 전달 합니다."""
    parser = argparse.ArgumentParser(
        description="System parameter by capture optional params"
    )
    parser.add_argument(
        "-t",
        "--time",
        default=1,
        type=int,
        help="Run process after wait time >> default = 1",
    )
    parser.add_argument(
        "-p",
        "--page",
        type=int,
        help="Count of pages in PDF viewr. this is most parameter",
    )
    parser.add_argument(
        "-r",
        "--remove",
        choices=["0", "1"],
        default=1,
        help="Is saved screenshot files remove all >> 0: keep  1: delete | default = 1",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    print(optional().time)
    print(optional().page)
    print(bool(int(optional().remove)))
