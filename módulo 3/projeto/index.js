const express = require("express");

const app = express();

const port = 4040;

const legumes = [
  "abóbora",
  "abobrinha",
  "alcachofra",
  "aspargos",
  "batata-doce",
  "berinjela",
  "beterraba",
  "cenoura",
  "cogumelo",
  "ervilha",
];

// [GET] /home
app.get("/", (req, res) => {
  res.send("Olá, usuário.");
});

// [GET] /legumes retorna a lista de legumes

app.get("/legumes", (req, res) => {
  res.send(legumes);
});

app.get("/legumes/:id", (req, res) => {
    const id = req.params.id-1;
    const legume = legumes[id];
    res.send(legume);
});

app.listen(port, () => {
  console.info(`APP rodando em : http://localhost:${port}`);
});
