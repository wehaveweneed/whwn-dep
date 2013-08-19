
require.config({
  paths: {
    cs: "components/require-cs/cs",
    "coffee-script": "components/require-cs/coffee-script",
    underscore: 'components/underscore/underscore',
    jquery: 'components/jquery/jquery',
    jquery_modal: 'components/bolster.simplemodal/src/jquery.simplemodal',
    jquery_cookie: 'components/jquery.cookie/jquery.cookie',
    jquery_ui: 'components/jquery_ui/src/jquery-ui-1.10.3.custom',
    text: 'components/text/text',
    backbone: 'components/backbone/backbone',
    backbone_tastypie: 'components/backbone-tastypie/backbone-tastypie',
    backgrid: 'components/backgrid/backgrid',
    select2: 'components/select2/select2',
    spreadsheet: 'components/backgrid/extensions/spreadsheet/backgrid-spreadsheet',
    selectall: 'components/backgrid/extensions/select-all/backgrid-select-all',
    select2cell: 'components/backgrid/extensions/select2-cell/backgrid-select2-cell',
    keymaster: 'components/keymaster/keymaster',
    handlebars: 'components/handlebars/handlebars',
    moment: 'components/moment/moment',
  },
  shim: {
    underscore: {
      exports: '_'
    },
    backbone: {
      deps: ['underscore', 'jquery', 'jquery_ui'],
      exports: 'Backbone'
    },
    backbone_relational: ['backbone'],
    backbone_tastypie: ['backbone'],
    backgrid: {
      deps: ['backbone'],
      exports: 'Backgrid'
    },
    spreadsheet: ['backgrid'],
    selectall: ['backgrid'],
    select2cell: ['backgrid', 'select2'],
    handlebars: {
      exports: "Handlebars"
    }
  }
});

require(["cs!csmain"]);
