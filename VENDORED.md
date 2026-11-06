# Vendored tools

The extractor runs on stock runners and on any clone; these helper tools are bundled so no
out-of-band host is needed. Each is third-party and kept verbatim.

| File | Origin | License | sha256 |
|------|--------|---------|--------|
| `avbtool` | Android Open Source Project (`external/avb/avbtool`) | Apache-2.0 / MIT (see header) | `02aa3572eb00ff994761e9222ce8dbb1c73dc5cffa2733383498e18414bc7a5b` |
| `lpunpack.py` | Python port of AOSP `lpunpack` (unix3dgforce) | MIT | `877053416c9fb608735cd6c0750157a3e6c4f4159c23f62c63de83e5f481c4fe` |
| `payload_dumper/` | git submodule `github.com/5ec1cff/payload-dumper` | see submodule | pinned by submodule commit |

Own code (GPL-3.0-or-later, VictorGabriel7Dev): `pixel_fullprop.py` (extractor), `pixel_factory.py`
(flashstation client + HTTP-range reader), `gen_index.py` (index generator).

Verify: `sha256sum avbtool lpunpack.py`.
