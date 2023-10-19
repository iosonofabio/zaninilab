let { FabilabNlp } = require('./chatbot.js');
let nlp = new FabilabNlp();


const defaultQuestions = [
  "who are you?",
  "what do you research?",
  "where are you?",
  "what do you teach?",
  "how do I join?",
];


function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


const intentCallback = (intent) => {
  let url;
  if (intent != "research")
    url = "/pages/" + intent + ".html";
  else
    url = "/"
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

  // Connect event listener for chatbot HTML fotm
  // THANKS TO: https://stackoverflow.com/questions/5384712/intercept-a-form-submit-in-javascript-and-prevent-normal-submission
  window.onload = function() {
    const question = defaultQuestions[getRandomInt(0, defaultQuestions.length - 1)];
    let input = document.getElementById('chatbotText');
    input.value = newQuestion;

    document.getElementById('chatbotForm').onsubmit = function() {
      const question = this.getElementsByTagName("input")[0].value;

      // no need to await, it'll go anyway when it's ready
      window.chatbot.askAndRedirect(question);
  
      // You must return false to prevent the default form behavior
      return false;
    }
  }

})();
