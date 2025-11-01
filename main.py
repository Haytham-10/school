"""Command line interface for AI LifeHub demo."""

from __future__ import annotations

import argparse
import logging
import sys

from ai_lifehub.modules.router import available_routes


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="واجهة تجريبية لتطبيق AI LifeHub المتكامل",
    )
    parser.add_argument(
        "mode",
        choices=sorted(available_routes().keys()),
        help="الوحدة الذكية المطلوب تشغيلها",
    )
    parser.add_argument(
        "prompt",
        help="الوصف أو الطلب المرسل للوحدة",
    )
    parser.add_argument(
        "--log-level",
        default="WARNING",
        help="مستوى السجلات (DEBUG, INFO, WARNING...)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    logging.basicConfig(level=args.log_level.upper())

    routes = available_routes()
    route = routes[args.mode]
    response = route.handler(args.prompt)

    print(response.as_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
