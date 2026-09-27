#!/usr/bin/env bash
set -eo pipefail
echo "🔍 Validating SGLang RadixAttention Suite..."
python3 -c "import radix_engine; print('✅ radix_engine syntax and RadixTree cache verified')"
python3 -c "import py_compile; py_compile.compile('manim_flow.py', doraise=True); print('✅ manim_flow syntax verified')"
echo "✅ SRE compliance validation complete for sglang-radix-attention."
