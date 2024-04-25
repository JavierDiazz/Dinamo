const express = require('express');
const router = express.Router();
const Auto = require('../models/auto');

// Obtener todos los autos
router.get('/', async (req, res) => {
  try {
    const autos = await Auto.find();
    res.json(autos);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Obtener un auto por ID
router.get('/:id', getAuto, (req, res) => {
  res.json(res.auto);
});

// Crear un nuevo auto
router.post('/', async (req, res) => {
  const auto = new Auto({
    _id: req.body.id,
    modelo: req.body.modelo,
    color: req.body.color,
    precio: req.body.precio,
    año: req.body.año,
    descripcion: req.body.descripcion,
    foto: req.body.foto
  });

  try {
    const nuevoAuto = await auto.save();
    res.status(201).json(nuevoAuto);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Actualizar un auto por ID
router.patch('/:id', getAuto, async (req, res) => {
  if (req.body.modelo != null) {
    res.auto.modelo = req.body.modelo;
  }
  if (req.body.color!= null) {
    res.auto.color = req.body.color;
  }
  if (req.body.precio != null) {
    res.auto.precio = req.body.precio;
  }
  if (req.body.año != null) {
    res.auto.año = req.body.año;
  }
  if (req.body.descripcion != null) {
    res.auto.descripcion = req.body.descripcion;
  }
  if (req.body.foto != null) {
    res.auto.foto = req.body.foto;
  }

  try {
    const autoActualizado = await res.auto.save();
    res.json(autoActualizado);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Eliminar un auto por ID
router.delete('/:id', getAuto, async (req, res) => {
  try {
    await res.auto.remove();
    res.json({ message: 'Auto eliminado' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

async function getAuto(req, res, next) {
  try {
    auto = await Auto.findById(req.params.id);
    if (auto == null) {
      return res.status(404).json({ message: 'Auto no encontrado' });
    }
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }

  res.auto = auto;
  next();
}

module.exports = router;
