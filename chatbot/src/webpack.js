let { FabilabNlp } = require('./chatbot.js');
let nlp = new FabilabNlp();

(async () => {

  await nlp.initialise();

  window.chatbot = nlp;

  console.log("Module loaded");
})();
