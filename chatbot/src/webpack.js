let { FabilabNlp } = require('./chatbot.js');
let nlp = new FabilabNlp();


const intentCallback = (intent) => {
  let url = "/pages/" + intent + ".html";
  window.location.href = url;
};


const askAndRedirect = async (question) => {
  let response = await chatbot.ask(question);
  return intentCallback(response.intent);
};


(async () => {

  await nlp.initialise();
  window.chatbot = nlp;
  //console.log("Module loaded");
  window.chatbot.askAndRedirect = askAndRedirect;

})();
