#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ======================================================================
#  PIXEL PROP BUILDER  ::  Pixel build.prop archive
#  Build index.json from the Pixel build.prop files in this repository.
#
#  Copyright (C) 2026  VictorGabriel7Dev
#  SPDX-License-Identifier: GPL-3.0-or-later
#  Fork of Pixel-Props/build.prop by @T3SL4.
#
#  Site      : https://victorgabriel.dev
#  Source    : https://github.com/VictorGabriel7Dev/build.prop
# ======================================================================
"""Emit index.json: one small manifest of every device, its channels and the latest .prop per
channel, so a consumer fetches a single file instead of listing and sorting the tree.

All values come straight from the build.prop files (Google's OTA data). Channel is read from the
file name: <codename>_<inc>.prop = release, <codename>_beta_<inc> = beta, <codename>_canary_<inc> =
canary; "latest" per channel is the highest incremental. Each channel entry also carries `source`,
the pipeline that produced the committed corpus (additive; consumers ignore it if unknown).

This is THE single index generator. Run standalone (`python3 gen_index.py . [--source seed|ci]`)
or import `build_index()` so other tooling never keeps a second copy of this logic.
"""
import json, re, sys, pathlib, datetime


def prop(txt, *keys):
    for k in keys:
        m = re.search(rf"^{re.escape(k)}=(.*)$", txt, re.M)
        if m and m.group(1).strip():
            return m.group(1).strip()
    return None


def build_index(root=".", source="seed"):
    """Scan <root>/<codename>/*.prop, write <root>/index.json, return the manifest dict.
    `source` tags every channel entry with the pipeline that produced the committed corpus:
    one authoritative committer (the out-of-band "seed"); "ci" only if the manual workflow ever
    contributes. Additive field - existing readers that do not know it simply skip it."""
    root = pathlib.Path(root)
    devices = {}
    for f in sorted(root.glob("*/*.prop")):
        if f.parent.name in ("payload_dumper", ".github"):
            continue
        cn = f.parent.name
        rest = f.stem[len(cn) + 1:] if f.stem.startswith(cn + "_") else f.stem
        if rest.startswith("beta_"):
            ch, inc = "beta", rest[5:]
        elif rest.startswith("canary_"):
            ch, inc = "canary", rest[7:]
        else:
            ch, inc = "release", rest
        incn = int(inc) if inc.isdigit() else 0
        txt = f.read_text(errors="replace")
        d = devices.setdefault(cn, {"model": None, "soc": None, "first_api_level": None, "channels": {}})
        d["model"] = d["model"] or prop(txt, "ro.product.model", "ro.product.product.model",
                                        "ro.product.system.model", "ro.product.vendor.model")
        soc, socm = prop(txt, "ro.soc.model"), prop(txt, "ro.soc.manufacturer")
        if soc and not d["soc"]:
            d["soc"] = f"{socm} {soc}".strip() if socm else soc
        fa = prop(txt, "ro.product.first_api_level", "ro.board.first_api_level")
        if fa and d["first_api_level"] is None and fa.isdigit():
            d["first_api_level"] = int(fa)
        cur = d["channels"].get(ch)
        if cur and cur["_incn"] >= incn:
            continue
        d["channels"][ch] = {
            "_incn": incn, "latest": f"{cn}/{f.name}",
            "build": prop(txt, "ro.build.id", "ro.build.display.id"),
            "incremental": prop(txt, "ro.build.version.incremental") or inc,
            "security_patch": prop(txt, "ro.build.version.security_patch", "ro.vendor.build.security_patch"),
            "android": prop(txt, "ro.build.version.release"),
            "vbmeta_digest": prop(txt, "ro.boot.vbmeta.digest"),
            "source": source,
        }

    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "devices": {}}
    for cn in sorted(devices):
        d = devices[cn]
        chans = {}
        for ch in ("release", "beta", "canary"):
            if ch in d["channels"]:
                chans[ch] = {k: v for k, v in d["channels"][ch].items() if k != "_incn" and v is not None}
        out["devices"][cn] = {"model": d["model"], "soc": d["soc"],
                              "first_api_level": d["first_api_level"], "channels": chans}
    (root / "index.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    source = "seed"
    if "--source" in args:
        i = args.index("--source")
        source = args[i + 1] if i + 1 < len(args) else "seed"
        del args[i:i + 2]
    root = args[0] if args else "."
    res = build_index(root, source=source)
    print(f"index.json: {len(res['devices'])} devices")
