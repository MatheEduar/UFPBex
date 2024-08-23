import express from "express";
import bodyParser from "body-parser";

const port = 3000;
const app = express();

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

let cursos = [
    {nome: "Ciência da Computação"},
    {nome: "Ciências de Dados e Inteligência Artificial"},
    {nome: "Engenharia da Computação"},
];

app.get("/", (req, res) =>{
    res.render("index.ejs", {cursos: cursos});
})

app.listen(port, () =>{
    console.log(`Executando na porta ${port}`);
})