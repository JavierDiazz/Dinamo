const mongoose = require('mongoose');

const autoSchema = new mongoose.Schema({
  modelo: String,
  color: String,
  precio: Number,
  año: Number,
  descripcion: String,
  foto: String // URL de la imagen
});

const Auto = mongoose.model('Auto', autoSchema);

module.exports = Auto;
