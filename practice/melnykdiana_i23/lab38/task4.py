from __future__ import annotations
import sys
import task2

if len(sys.argv) != 2 or sys.argv[1] not in {"connection", "http", "timeout"}:
    print("Використання: python task4.py connection|http|timeout", file=sys.stderr)
    raise SystemExit(2)

sys.argv = ["task2.py", "--demo-error", sys.argv[1]]
raise SystemExit(task2.main())
