const mongoose = require('mongoose');

const usuarioSchema = new mongoose.Schema({
  nombre: String,
  apellido: String,
  telefono: String,
  email: String,
  nombreSede: { type: mongoose.Schema.Types.ObjectId, ref: 'Sede' },
  contraseña: String,
  nombreRol: { type: mongoose.Schema.Types.ObjectId, ref: 'Rol' }
});

const Usuario = mongoose.model('Usuario', usuarioSchema);

module.exports = Usuario;
