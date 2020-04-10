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
  database : 'intermedias',
  port: 3306
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

//--------------------------CRUD PRODUCTO ---------------------

app.get('/producto', (req, res) => {
  connection.query('select * from producto', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/productoid', (req, res) => {
  connection.query(`select * from producto where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/producto', (req, res) => {
  connection.query(`insert into producto ( sku, barcode, nombre, descripcion, precio) values ( '${req.body.sku}', ${req.body.barcode},'${req.body.nombre}', '${req.body.descripcion}', ${req.body.precio} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarproducto', (req, res) => {
  connection.query(`update producto set sku = '${req.body.sku}', barcode = ${req.body.barcode}, nombre = '${req.body.nombre}', descripcion = '${req.body.descripcion}', precio = ${req.body.precio} where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarproducto', (req, res) => {
  connection.query(`delete from producto where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//------------------------CRUD CATEGORIA---------------------------------------

app.get('/categoria', (req, res) => {
  connection.query('select * from categoria', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/categoriaid', (req, res) => {
  connection.query(`select * from categoria where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/categoria', (req, res) => {
  connection.query(`insert into categoria ( cod_categoria, nombre) values ( ${req.body.cod_categoria},'${req.body.nombre}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarcategoria', (req, res) => {
  connection.query(`update categoria set cod_categoria = ${req.body.cod_categoria}, nombre ='${req.body.nombre}' where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarcategoria', (req, res) => {
  connection.query(`delete from categoria where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------PRODUCTO CATEGORIA------------------------------

app.post('/productocategoria', (req, res) => {
  connection.query(`insert into producto_categoria ( cod_categoria, sku) values ( ${req.body.cod_categoria},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarproductocategoria', (req, res) => {
  connection.query(`delete from producto_categoria where cod_categoria = ${req.body.cod_categoria} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD TRANSFERENCIA------------------------------------------

app.get('/transferencia', (req, res) => {
  connection.query('select * from transferencia', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/transferenciaid', (req, res) => {
  connection.query(`select * from transferencia where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/transferencia', (req, res) => {
  connection.query(`insert into transferencia ( cod_transferencia, estado_aceptacion,tipo_transf,estado_entrega,cod_repartidor,cod_solicitante) values ( ${req.body.cod_transferencia},${req.body.estado_aceptacion},${req.body.tipo_transf},${req.body.estado_entrega},${req.body.cod_repartidor},${req.body.cod_solicitante})`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editartransferencia', (req, res) => {
  connection.query(`update transferencia set cod_transferencia = ${req.body.cod_transferencia}, estado_aceptacion = ${req.body.estado_aceptacion},tipo_transf = ${req.body.tipo_transf},estado_entrega = ${req.body.estado_entrega},cod_repartidor = ${req.body.cod_repartidor},cod_solicitante = ${req.body.cod_solicitante} where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminartransferencia', (req, res) => {
  connection.query(`delete from transferencia where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------LISTA PRODUCTOS------------------------------

app.post('/listaproductos', (req, res) => {
  connection.query(`insert into lista_productos (cantidad,cod_transferencia,sku) values (${req.body.cantidad}, ${req.body.cod_transferencia},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarlistaproductos', (req, res) => {
  connection.query(`delete from lista_productos where cod_transferencia = ${req.body.cod_transferencia} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------VENTA PRODUCTO------------------------------

app.post('/ventaproducto', (req, res) => {
  connection.query(`insert into venta_producto (cod_venta,sku) values (${req.body.cod_venta},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarventaproducto', (req, res) => {
  connection.query(`delete from venta_producto where cod_venta = ${req.body.cod_venta} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------------LOG INVENTARIO-----------------------------

app.get('/loginventario', (req, res) => {
  connection.query('select * from log_inventario', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/loginventario', (req, res) => {
  connection.query(`insert into log_inventario ( cod_log, cantidad_antigua,cantidad_nueva,motivo,fecha,cod_usuario,sku) values ( ${req.body.cod_log},${req.body.cantidad_antigua},${req.body.cantidad_nueva},'${req.body.motivo}',str_to_date('${req.body.fecha}', '%d/%m/%Y' ),${req.body.cod_usuario},'${req.body.sku}')`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.listen(3000, () => console.log('server started'));
