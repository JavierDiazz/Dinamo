const mongoose = require('mongoose');

const sedeSchema = new mongoose.Schema({
  nombreSede: String
});

const Sede = mongoose.model('Sede', sedeSchema);

module.exports = Sede;
