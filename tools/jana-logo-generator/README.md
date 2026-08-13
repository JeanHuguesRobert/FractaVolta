# Jana logo generator

This directory is the canonical in-repository home of the Jana logo generator used by FractaVolta.

## Provenance

The generator was first published as a standalone GitHub Gist on 2026-03-13:

- Gist: `JeanHuguesRobert/fed24b8cf6a126a9a41a41591c73b005`
- File: `jana.html`
- Historical role: standalone publication and provenance anchor

The Gist SHOULD remain available as the historical snapshot. Development and maintenance MAY move here without rewriting that history.

## Relationship with FractaVolta

Jana is a small autonomous software asset embedded in the FractaVolta repository. It defines the generative visual system used to produce the solar-cross mark and its variants, including the primary palette:

- red `#D7141A`
- yellow `#F0C30F`
- blue `#0046AD`
- black `#1A1A1A`
- white `#FFFFFF`

A generated SVG is already used at `docs/assets/jana.svg`.

## Hosted-code precedent

This directory is also a first retrofit example for the emerging **hosted repository** convention: a repository-scale autonomous unit may live inside another Git repository while remaining independently understandable, operable and extractable.

For a hosted software unit, the host SHOULD preserve:

1. **Identity** — a stable local name and purpose.
2. **Provenance** — links to earlier publication/history.
3. **Operational autonomy** — enough local documentation and dependencies to run or maintain the code.
4. **Extractability** — the subtree should be separable into an autonomous repository with minimal repair.
5. **No history rewriting** — external historical publications such as Gists remain provenance anchors rather than being silently replaced.

## Retrofit status

- [x] Canonical in-repository location established.
- [x] Historical Gist recorded.
- [x] Relationship to `docs/assets/jana.svg` documented.
- [ ] Mirror the historical `jana.html` source here verbatim.
- [ ] Add a minimal smoke test or deterministic rendering check if/when the generator resumes active development.

The source license embedded in the historical Gist remains authoritative for that historical snapshot until an explicit licensing decision states otherwise.
