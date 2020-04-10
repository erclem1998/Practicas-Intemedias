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

//--------------------------CRUD ROL ---------------------

app.get('/rol', (req, res) => {
  connection.query('select * from ROL', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/rolid', (req, res) => {
  connection.query(`select * from ROL where cod_rol = ${req.body.cod_rol}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/rol', (req, res) => {
  connection.query(`insert into ROL ( nombre_rol ) values ('${req.body.nombre_rol}')`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarrol', (req, res) => {
  connection.query(`update ROL set nombre_rol = '${req.body.nombre_rol}' where cod_rol = ${req.body.cod_rol}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarrol', (req, res) => {
  connection.query(`delete from ROL where cod_rol = ${req.body.cod_rol}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});


//--------------------------CRUD USUARIO ---------------------

app.get('/usuario', (req, res) => {
  connection.query('select * from USUARIO', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/usuarioid', (req, res) => {
  connection.query(`select * from USUARIO where dpi = ${req.body.dpi}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/usuario', (req, res) => {
  connection.query(`insert into USUARIO ( dpi, nombre, fecha_nac, correo, pass, es_encargado ) values ( ${req.body.dpi}, '${req.body.nombre}', str_to_date('${req.body.fecha_nac}', '%d/%m/%Y' ), '${req.body.correo}', '${req.body.pass}', '${req.body.es_encargado}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarusuario', (req, res) => {
  connection.query(`update USUARIO set nombre = '${req.body.nombre}', fecha_nac = str_to_date('${req.body.fecha_nac}', '%d/%m/%Y' ), correo = '${req.body.correo}', pass = '${req.body.pass}', es_encargado = '${req.body.es_encargado}' where dpi = ${req.body.dpi}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarusuario', (req, res) => {
  connection.query(`delete from USUARIO where dpi = ${req.body.dpi}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------USUARIO_ROL------------------------------

app.post('/usuariorol', (req, res) => {
  connection.query(`insert into USUARIO_ROL ( dpi, cod_rol ) values ( ${req.body.dpi}, ${req.body.cod_rol} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarusuariorol', (req, res) => {
  connection.query(`delete from USUARIO_ROL where dpi = ${req.body.dpi} and cod_rol = ${req.body.cod_rol}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD SEDE ---------------------

app.get('/sede', (req, res) => {
  connection.query('select * from SEDE', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/sedeid', (req, res) => {
  connection.query(`select * from SEDE where cod_sede = ${req.body.cod_sede}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/sede', (req, res) => {
  connection.query(`insert into SEDE ( alias, direccion, departamento, municipio, num_bodegas, cod_encargado ) values ( '${req.body.alias}', '${req.body.direccion}', '${req.body.departamento}', '${req.body.municipio}', ${req.body.num_bodegas}, ${req.body.cod_encargado} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarsede', (req, res) => {
  connection.query(`update SEDE set alias = '${req.body.alias}', direccion = '${req.body.direccion}', departamento = '${req.body.departamento}', municipio = '${req.body.municipio}', num_bodegas = ${req.body.num_bodegas}, cod_encargado = ${req.body.cod_encargado} where cod_sede = ${req.body.cod_sede}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarsede', (req, res) => {
  connection.query(`delete from SEDE where cod_sede = ${req.body.cod_sede}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD BODEGA ---------------------

app.get('/bodega', (req, res) => {
  connection.query('select * from BODEGA', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/bodegaid', (req, res) => {
  connection.query(`select * from BODEGA where cod_bodega = ${req.body.cod_bodega}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/bodega', (req, res) => {
  connection.query(`insert into BODEGA ( nombre, direccion, estado, cod_encargado, cod_sede ) values ( '${req.body.nombre}', '${req.body.direccion}', '${req.body.estado}', ${req.body.cod_encargado}, ${req.body.cod_sede} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarbodega', (req, res) => {
  connection.query(`update BODEGA set nombre = '${req.body.nombre}', direccion = '${req.body.direccion}', estado = '${req.body.estado}', cod_encargado = ${req.body.cod_encargado}, cod_sede = ${req.body.cod_sede} where cod_bodega = ${req.body.cod_bodega}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarbodega', (req, res) => {
  connection.query(`delete from BODEGA where cod_bodega = ${req.body.cod_bodega}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD CLIENTE ---------------------

app.get('/cliente', (req, res) => {
  connection.query('select * from CLIENTE', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/clienteid', (req, res) => {
  connection.query(`select * from CLIENTE where dpi = ${req.body.dpi}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/cliente', (req, res) => {
  connection.query(`insert into CLIENTE ( dpi, nit, nombre, direccion, cod_sede ) values ( ${req.body.dpi}, ${req.body.nit}, '${req.body.nombre}', '${req.body.direccion}', ${req.body.cod_sede} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarcliente', (req, res) => {
  connection.query(`update CLIENTE set nit = ${req.body.nit}, nombre = '${req.body.nombre}', direccion = '${req.body.direccion}', cod_sede = ${req.body.cod_sede} where dpi = ${req.body.dpi}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarcliente', (req, res) => {
  connection.query(`delete from CLIENTE where dpi = ${req.body.dpi}`, function(err, rows, fields) {
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
  connection.query('select * from CATEGORIA', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/categoriaid', (req, res) => {
  connection.query(`select * from CATEGORIA where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/categoria', (req, res) => {
  connection.query(`insert into CATEGORIA ( nombre) values ( '${req.body.nombre}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarcategoria', (req, res) => {
  connection.query(`update CATEGORIA set cod_categoria = ${req.body.cod_categoria}, nombre ='${req.body.nombre}' where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarcategoria', (req, res) => {
  connection.query(`delete from CATEGORIA where cod_categoria = ${req.body.cod_categoria}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD PRODUCTO ---------------------

app.get('/producto', (req, res) => {
  connection.query('select * from PRODUCTO', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/productoid', (req, res) => {
  connection.query(`select * from PRODUCTO where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/producto', (req, res) => {
  connection.query(`insert into PRODUCTO ( sku, barcode, nombre, descripcion, precio) values ( '${req.body.sku}', ${req.body.barcode},'${req.body.nombre}', '${req.body.descripcion}', ${req.body.precio} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarproducto', (req, res) => {
  connection.query(`update PRODUCTO set sku = '${req.body.sku}', barcode = ${req.body.barcode}, nombre = '${req.body.nombre}', descripcion = '${req.body.descripcion}', precio = ${req.body.precio} where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarproducto', (req, res) => {
  connection.query(`delete from PRODUCTO where barcode = ${req.body.barcode}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------PRODUCTO_CATEGORIA------------------------------

app.post('/productocategoria', (req, res) => {
  connection.query(`insert into PRODUCTO_CATEGORIA ( cod_categoria, sku ) values ( ${req.body.cod_categoria},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarproductocategoria', (req, res) => {
  connection.query(`delete from PRODUCTO_CATEGORIA where cod_categoria = ${req.body.cod_categoria} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------CRUD VENTA ---------------------

app.get('/venta', (req, res) => {
  connection.query('select * from VENTA', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/ventaid', (req, res) => {
  connection.query(`select * from VENTA where cod_venta = ${req.body.cod_venta}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/venta', (req, res) => {
  connection.query(`insert into VENTA ( fecha_factura, fecha_entrega, total_venta, cargototal, ganancia_empresa, ganancia_repartidor, estado_entrega, cod_cliente, cod_vendedor, cod_repartidor ) values ( str_to_date('${req.body.fecha_factura}', '%d/%m/%Y' ), str_to_date('${req.body.fecha_entrega}', '%d/%m/%Y' ), ${req.body.total_venta}, ${req.body.cargototal}, ${req.body.ganancia_empresa}, ${req.body.ganancia_repartidor}, ${req.body.estado_entrega}, ${req.body.cod_cliente}, ${req.body.cod_vendedor}, ${req.body.cod_repartidor} )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarventa', (req, res) => {
  connection.query(`update VENTA set fecha_factura = str_to_date('${req.body.fecha_factura}', '%d/%m/%Y' ), fecha_entrega = str_to_date('${req.body.fecha_entrega}', '%d/%m/%Y' ), total_venta = ${req.body.total_venta}, cargototal = ${req.body.cargototal}, ganancia_empresa = ${req.body.ganancia_empresa}, ganancia_repartidor = ${req.body.ganancia_repartidor}, estado_entrega = ${req.body.estado_entrega}, cod_cliente = ${req.body.cod_cliente}, cod_vendedor = ${req.body.cod_vendedor}, cod_repartidor = ${req.body.cod_repartidor} where cod_venta = ${req.body.cod_venta}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarventa', (req, res) => {
  connection.query(`delete from VENTA where cod_venta = ${req.body.cod_venta}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------VENTA_PRODUCTO------------------------------

app.post('/ventaproducto', (req, res) => {
  connection.query(`insert into VENTA_PRODUCTO (cod_venta,sku) values (${req.body.cod_venta},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarventaproducto', (req, res) => {
  connection.query(`delete from VENTA_PRODUCTO where cod_venta = ${req.body.cod_venta} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//--------------------------------LOG_INVENTARIO-----------------------------

app.get('/loginventario', (req, res) => {
  connection.query('select * from LOG_INVENTARIO', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/loginventarioid', (req, res) => {
  connection.query(`select * from LOG_INVENTARIO where cod_log = ${req.body.cod_log}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/loginventario', (req, res) => {
  connection.query(`insert into LOG_INVENTARIO ( cod_log, cantidad_antigua,cantidad_nueva,motivo,fecha,cod_usuario,sku) values ( ${req.body.cod_log},${req.body.cantidad_antigua},${req.body.cantidad_nueva},'${req.body.motivo}',str_to_date('${req.body.fecha}', '%d/%m/%Y' ),${req.body.cod_usuario},'${req.body.sku}')`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editarloginventario', (req, res) => {
  connection.query(`update LOG_INVENTARIO set cantidad_antigua = ${req.body.cantidad_antigua}, cantidad_nueva = ${req.body.cantidad_nueva}, motivo = '${req.body.motivo}', fecha = str_to_date('${req.body.fecha}', '%d/%m/%Y' ), cod_usuario = ${req.body.cod_usuario}, sku = '${req.body.sku}' where cod_log = ${req.body.cod_log}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarloginventario', (req, res) => {
  connection.query(`delete from LOG_INVENTARIO where cod_log = ${req.body.cod_log}`, function(err, rows, fields) {
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
  connection.query('select * from TRANSFERENCIA', function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/transferenciaid', (req, res) => {
  connection.query(`select * from TRANSFERENCIA where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send(rows)
    } 
    else{
      throw err;
    }
  });
});

app.post('/transferencia', (req, res) => {
  connection.query(`insert into TRANSFERENCIA ( cod_transferencia, estado_aceptacion,tipo_transf,estado_entrega,cod_repartidor,cod_solicitante) values ( ${req.body.cod_transferencia},${req.body.estado_aceptacion},${req.body.tipo_transf},${req.body.estado_entrega},${req.body.cod_repartidor},${req.body.cod_solicitante})`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/editartransferencia', (req, res) => {
  connection.query(`update TRANSFERENCIA set cod_transferencia = ${req.body.cod_transferencia}, estado_aceptacion = ${req.body.estado_aceptacion},tipo_transf = ${req.body.tipo_transf},estado_entrega = ${req.body.estado_entrega},cod_repartidor = ${req.body.cod_repartidor},cod_solicitante = ${req.body.cod_solicitante} where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminartransferencia', (req, res) => {
  connection.query(`delete from TRANSFERENCIA where cod_transferencia = ${req.body.cod_transferencia}`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

//----------------------LISTA_PRODUCTOS------------------------------

app.post('/listaproductos', (req, res) => {
  connection.query(`insert into LISTA_PRODUCTOS (cantidad,cod_transferencia,sku) values (${req.body.cantidad}, ${req.body.cod_transferencia},'${req.body.sku}' )`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});

app.post('/eliminarlistaproductos', (req, res) => {
  connection.query(`delete from LISTA_PRODUCTOS where cod_transferencia = ${req.body.cod_transferencia} and sku = '${req.body.sku}'`, function(err, rows, fields) {
    if (!err){
      res.send('OK!')
    } 
    else{
      throw err;
    }
  });
});


app.listen(3000, () => console.log('server started'));
