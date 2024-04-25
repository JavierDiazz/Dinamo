const mongoose = require('mongoose');

const rolSchema = new mongoose.Schema({
  nombreRol: String
});

const Rol = mongoose.model('Rol', rolSchema);

module.exports = Rol;
