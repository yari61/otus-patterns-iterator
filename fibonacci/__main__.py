from __future__ import annotations

from .cli import parser
from .fibonacci import FibonacciLinear
from .iterate import LinearIteratorFactory
from .output import Dump, JsonFormatter, StdoutStream, DefaultStream


def main():
    args = parser.parse_args()
    fibonacci = FibonacciLinear()
    indices = range(args.start, args.stop, args.step)
    iterator_factory = LinearIteratorFactory(collection=fibonacci, indices=indices.__iter__())
    iterator = iterator_factory()

    formatter = JsonFormatter()
    if not args.output:
        stream = StdoutStream()
    else:
        output_stream = open(args.output, mode="w")
        stream = DefaultStream(stream=output_stream)
    dump = Dump(stream=stream, formatter=formatter)
    dump(iterator=iterator)

if __name__ == "__main__":
    main()
