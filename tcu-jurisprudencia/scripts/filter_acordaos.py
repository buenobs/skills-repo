#!/usr/bin/env python3
"""
Filtra localmente (sem rede) um JSON de acórdãos do TCU já obtido via a
ferramenta de fetch de URL contra o endpoint oficial:

  https://dados-abertos.apps.tcu.gov.br/api/acordao/recupera-acordaos

Uso:
  python3 filter_acordaos.py acordaos.json "termo de busca" [--field titulo,sumario,relator,colegiado]

O JSON de entrada deve ser uma lista de objetos de acórdão (o retorno bruto
do endpoint) ou um arquivo com várias listas concatenadas (uma por chamada de
paginação) — nesse caso, salve cada página em uma linha própria (JSON Lines)
ou dentro de uma lista externa; o script tenta lidar com ambos os formatos.

Este script não faz nenhuma chamada de rede. Ele existe só para permitir
filtrar centenas de resultados paginados sem colar tudo isso no contexto da
conversa.
"""
import json
import sys
import argparse


def load_records(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    records = []
    # Try a single JSON value first (list, or list-of-lists).
    try:
        data = json.loads(raw)
        if isinstance(data, list):
            for item in data:
                if isinstance(item, list):
                    records.extend(item)
                elif isinstance(item, dict):
                    records.append(item)
            return records
    except json.JSONDecodeError:
        pass

    # Fall back to JSON Lines (one page/list per line).
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(data, list):
            records.extend(data)
        elif isinstance(data, dict):
            records.append(data)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_file", help="Arquivo com o JSON retornado pelo endpoint de acórdãos")
    parser.add_argument("termo", help="Termo/palavra-chave a buscar (case-insensitive)")
    parser.add_argument(
        "--field",
        default="titulo,sumario,relator,colegiado",
        help="Campos onde buscar o termo, separados por vírgula (padrão: titulo,sumario,relator,colegiado)",
    )
    args = parser.parse_args()

    fields = [f.strip() for f in args.field.split(",") if f.strip()]
    termo = args.termo.lower()

    records = load_records(args.json_file)
    matches = []
    for r in records:
        haystack = " ".join(str(r.get(f, "")) for f in fields).lower()
        if termo in haystack:
            matches.append(r)

    print(f"# {len(matches)} de {len(records)} acórdãos combinam com '{args.termo}'\n")
    for m in matches:
        print(f"- {m.get('titulo', '(sem título)')}")
        print(f"  relator: {m.get('relator', '?')} | colegiado: {m.get('colegiado', '?')} | data: {m.get('dataSessao', '?')}")
        print(f"  sumario: {m.get('sumario', '')[:300]}")
        print(f"  inteiro teor (PDF): {m.get('urlArquivoPdf', '')}")
        print(f"  pesquisa integrada: {m.get('urlAcordao', '')}")
        print()


if __name__ == "__main__":
    main()
