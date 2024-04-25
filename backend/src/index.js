//libs
const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const bodyParser = require('body-parser');
require('./db');
const usuariosRouter = require('./routes/usuario');
const autosRouter = require('./routes/auto');

//inicializaciones
const app = express();

app.use(express.static('frontend'));

//Puerto para el despliegue en producción
const { PORT } = process.env;

//configuraciones
app.set('port', 3700);

//rutas
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/frontend/index.html');
});
app.use('/api/usuario', usuariosRouter);
app.use('/api/auto', autosRouter);


//middlewares
app.use(morgan('dev'));
app.use(express.json());
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.urlencoded({ extended: false }));

//despliegue del servidor
app.listen(app.get('port'), () =>
{
    console.log('Server on port', app.get('port'));
});
