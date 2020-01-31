const workboxBuild = require('workbox-build');

// NOTE: This should be run *AFTER* all your assets are built
const buildSW = () => {
  // This will return a Promise
  return workboxBuild.injectManifest({
    swSrc: 'src/service_worker.js',
    swDest: 'service_worker.js',
    globDirectory: '.',
    globPatterns: [
      "new_site/**\/*.{js,css,html,png,pdf,jpg,json,md,ico,svg}",
      "node_modules/bootstrap-select/dist/js/bootstrap-select.min.js",
      "node_modules/bootstrap/dist/js/bootstrap.min.js",
      "node_modules/jquery/dist/jquery.min.js",
      "node_modules/popper.js/dist/umd/popper.min.js",
      "site.webmanifest",
      'index.html',
      './',
      "assets/css/style.css"
    ],
    globIgnores: ["**/service_worker.js"],
  }).then(({count, size, warnings}) => {
    // Optionally, log any warnings and details.
    warnings.forEach(console.warn);
    console.log(`${count} files will be precached, totaling ${size} bytes.`);
  });
}


buildSW();