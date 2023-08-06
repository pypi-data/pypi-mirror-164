# Inkplot
Inkplot makes a [PDF](https://gitlab.com/frameworklabs/inkplot/-/raw/master/docs/examples/sample-output.pdf?inline=false) out of [Inkscape](https://inkscape.org/) SVG documents
using a [simple YAML file](https://gitlab.com/frameworklabs/inkplot/-/blob/master/docs/examples/farm-pages.yml) that describes for each page:
* the [source SVG]()
* set of rules for determining the visibiilty for each of SVG's layers
* the page's zoom extents

It's goal is to make it easy to produce PDFs from SVGs where the workflow
includes turning layers on and off and zooming around to different spots
in the document space.

## Pages
To keep things brief, inkplot pages can use shared layersets and zoom
rectangles:
```yaml
shared:
  layersets:
    - name: hide-all
      source: farm.svg
      hidden:
        - '**'
    - name: basemap-imagery
      source: farm.svg
      visible: True
      layers:
        - "site>>basemap>>**"
    - name: titleblock-frontpage
      source: farm.svg
      visible:
        - "titleblock>>full extent frame>>boxes"
        - "titleblock>>full extent frame>>mask"
        - "scale>>full extent scale"
  zoom-rectangles:
    - name: whole-site-frame
      id: residences-site-frame-lg
    - name: both-residences-frame
      id: residences-site-frame-sm
```

So a page definition can reference layersets and simply define any additional
layers that need to be turned on or off above and beyond the shared layersets
listed in `include-layersets`:
```yaml
pages:
  - name: frontpage
    source: farm.svg
    include-layersets:
      - "hide-all"
      - "basemap-imagery"
      - "titleblock-frontpage"
    layersets:
      - visible: True
        layers:
          - "titleblock>>full extent frame>>title>>overview-basemap"
    include-zoom-rectangle: whole-site-frame
```

And, because it's a [YAML](https://yaml.org/) file, we can gain a bit more
brevity yet using YAML aliases:
```yaml
pages:
  # this one defines the front page but also makes a template of sorts named
  # pg-imagery-with-titleblock that can be used later
  - &pg-imagery-with-titleblock
    name: frontpage
    source: farm.svg
    include-layersets:
      - "hide-all"
      - "basemap-imagery"
      - "titleblock-frontpage"
    layersets:
      - visible: True
        layers:
          - "titleblock>>full extent frame>>title>>overview-basemap"
    include-zoom-rectangle: whole-site-frame
    
  # this defines a page that includes everything in the frontpage def, but
  # redefines the layersets (keeping the layersets referenced in
  # include-layersets)
  - *pg-imagery-with-titleblock
    name: siteplan
    layersets:
        visible:
          - "titleblock>>full extent frame>>title>>site-plan"
          - "bldgs>>**"
          - "site/infrastructure/fences/**"
```

## Using the CLI
To create a PDF with, use the simple CLI:
```bash
inkplot example.yml /tmp/example.pdf
```

And that should do it.

## Installing
For now, to install, you need to use pip (I'll work on a deb) and:
```bash
pip install inkplot
```
