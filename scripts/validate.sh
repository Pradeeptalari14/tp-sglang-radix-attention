#!/usr/bin/env bash
set -e
echo "🔍 Validating SGLang RadixAttention Suite..."
python3 -c "import py_compile; py_compile.compile('radix_engine.py', doraise=True); print('✅ radix_engine syntax verified')"
python3 -c "import py_compile; py_compile.compile('manim_flow.py', doraise=True); print('✅ manim_flow syntax verified')"
echo "✅ SRE compliance validation complete for sglang-radix-attention."
