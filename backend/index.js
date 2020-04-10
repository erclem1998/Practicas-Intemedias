const express = require('express');
const bodyParser = require('body-parser');

const app = express();

let cors = require('cors');
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : '54.161.210.216',
  user     : 'root',
  password : 'lemus540',
  database : 'intermedias'
});
connection.connect();




app.get('/', (req, res) => {
  connection.query('select * from USUARIO', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/rol', (req, res) => {
  connection.query(`INSERT INTO ROL ( nombre_rol ) VALUES ('${req.body.nombre_rol}')`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.get('/rol', (req, res) => {
  connection.query('SELECT * FROM ROL', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/usuario', (req, res) => {
  connection.query(`INSERT INTO USUARIO ( dpi, nombre, fecha_nac, correo, pass, es_encargado ) VALUES ( ${req.body.dpi}, '${req.body.nombre}', STR_TO_DATE('${req.body.fecha_nac}', '%d/%m/%Y' ), '${req.body.correo}', '${req.body.pass}', '${req.body.es_encargado}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.get('/usuario', (req, res) => {
  connection.query('SELECT * FROM USUARIO', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.listen(3000, () => console.log('server started'));
