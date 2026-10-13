# Build and validation

From repository root, using Python 3:

```sh
python3 architecture/gcp-gke-level-1/v4/build_v4.py
python3 architecture/gcp-gke-level-1/options-review/build_options.py
python3 architecture/tools/validate_package.py
```

Generators create editable draw.io XML and SVGs using bundled icons. V4 graph metadata is required by the options generator. Older diagram versions and historical validation files are not required.

PNG previews are included. If diagrams change, rerender the corresponding SVGs with your approved SVG renderer (for example Sharp) and visually inspect them. The included PNGs were rendered from SVG, not exported by the native organizational draw.io editor. Import into that editor remains an environment-specific validation step.

The package validator checks XML, per-page IDs, connector endpoints, local Markdown links and excluded image/cache files. It does not validate a running system or approve technology choices. The sharing-branch preparation verified that V4 diagram/PNG/SVG and latest options diagram/exports match their source files byte for byte.

## Icon provenance

Google product SVG icons are retained from the official Google Cloud legacy icon package, with vendor colors unchanged. See [Google Cloud icons](https://cloud.google.com/icons) and the [legacy icon package](https://services.google.com/fh/files/misc/google-cloud-legacy-icons.zip). Applicable vendor usage terms and internal approval still apply; no new license entitlement is asserted.

Files prefixed `neutral-` are project-created capability symbols, not vendor logos. Genesys and Redis alternatives use neutral symbols where a vendor logo is not bundled. Icons are embedded in draw.io, so viewing does not require external downloads. No input JPEGs or AMEX logo are included.
