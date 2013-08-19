({
  paths: {
    "coffee-script": "components/require-cs/coffee-script",
    cs: "components/require-cs/cs"
  },
  mainConfigFile: "backbone/main.js",
  name: "main",
  stubModules: ["cs"],
  insertRequire: ["cs!csmain"],
  exclude: ["coffee-script"]
})