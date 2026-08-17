python - <<'PY'
import json

with open(
    'data/chunks/Lei_Complementar_214_chunks.json',
    encoding='utf-8'
) as f:
    data = json.load(f)

print(data[0])
print()
print("Total:", len(data))
PY
