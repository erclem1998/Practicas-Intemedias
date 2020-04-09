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
    //res.send(rows);
  });
});

app.listen(3000, () => console.log('server started'));
