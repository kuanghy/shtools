/**
 * Placeholder for custom user javascript
 * mainly to be overridden in profile/static/custom/custom.js
 * This will always be an empty file in IPython
 *
 * User could add any javascript in the `profile/static/custom/custom.js` file.
 * It will be executed by the ipython notebook at load time.
 *
 * Same thing with `profile/static/custom/custom.css` to inject custom css into the notebook.
 *
 */

 define([
     'base/js/namespace',
     'base/js/events'
     ],
     function(IPython, events) {
         events.on("app_initialized.NotebookApp",
             function () {
                 IPython.Cell.options_default.cm_config.lineNumbers = true;
             }
         );
     }
 );
