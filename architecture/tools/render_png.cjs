/* Render presentation PNGs from the six authoritative SVG exports. */
const path = require('node:path');
const sharp = require('sharp');
const root = path.resolve(__dirname, '../v1');
const views = ['level-1-architecture', 'component-views/01-real-time-ingestion',
  'component-views/02-intelligence-processing', 'component-views/03-intelligence-delivery',
  'integration-views/04-component-interactions', 'integration-views/05-high-level-flows'];
(async () => {
  for (const view of views) {
    const file = path.join(root, view);
    await sharp(file + '.svg').png().toFile(file + '.png');
    console.log(view);
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
